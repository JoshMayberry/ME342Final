import wx
import numpy as np #For the argmax() functionality
import copy #This is needed because sometimes the temp lists modify their parent lists. So, deep copies are made.
#from .logicThermoInput import LogicThermoInput

class LogicCalculator(wx.Process):#LogicThermoInput):
	"""
	This is the main class for the calculator function.

	First, it determines what functions to use. It does this by seeing what variables you gave it.
	By seeing what variables you gave it, it can determine which equations are available.
	New variables can be gained by solving simple equations. Thsi will gain acess to new equations to use.

	Equations with one unknown are solved using a root finder.
	Multiple Equations with multiple unknowns are solved using Gauss-Sidel.

	Once the equations have been solved, it returns all the information it found. This is displayed on a new screen.

	Psudocode:
		- What have I been given? What do I need to find?
		- What equations contain what I need to find?
		- Which of those equations include the variables I have been given?
		- What equations can I use to get the variables that I still need?
		Note: Up till this point, no equations have been run. Just an analysis of what variables they contain.
		- Solve the equations, and return your answer.
	"""
	def __init__(self,*args,**kwargs):
		"""
		'subject' is what subject you are solving for. It is a string.
		'args' is [subject,goal]. There can be multiple goals, because goals is a list
		'kwargs' is a dictionary containing all the variables, known and unknown.
		"""
		print('Begin Calculation')
		self = LogicCalculator
	#What have I been given?
		self.subject = args[0][0]
		#print('\n',self.subject)

	#What is known? What is not known?
		self.unknown,self.known = {},{} #Blank dictionaries
		for i in kwargs.items():
			if '@' not in i:
				if ('unknown' in i) or ('' in i): 
					if i[0][0] != 'U': self.unknown.update({i[0]:i[1]})
				else: 
					if i[0][0] != 'U': self.known.update({i[0]:i[1]})
		#print('unknown',self.unknown)
		#print('known',self.known)

	#What do  I need to find?
		self.goal = args[1]
		#print(self.goal)

	#Get everything in SI units

	#Equations
	##Retrieve the correct Equation Database
		print('Loading Database')
		if self.subject == 'thermo':
			from .logicThermoEquations import LogicThermoEquations
			self.eqnDatabase = LogicThermoEquations.eqnDatabase(self)
			print('    ~ Thermo Database Loaded')
#		elif self.subject == 'statics': 		#This is to show how to add another subject.
#			from .logicStaticsEquations import LogicStaticsEquations
#			self.eqnDatabase = LogicStaticsEquations.eqnDatabase(self)

	##Search through that Database for the relevant equations
		temp = self.unknownGoalSetup(self)
		self.equationFinder(self,temp)

	#Solve the equations
		self.solver(self,self.equations)

	#Return your answer
		#Have it go through the answers and return only the ones that we want.

	def eqnDatabaseContains(self,varsSearch,varsAfter):
		"""
			This simply searches for what equations in the database contain the given variables.
			It then chooses the best one.
			'varsSearch' is the variables to search for
			'varsAfter' is the variables contained in the equation after the one before this new one.
		"""
		possibleEqns,possibleNames = {},[]
		for var in varsSearch.items(): #Look at each variable in turn
#			if var[1] != 0: #Don't waste time on the zero value variables  				(Remove this part?)
			for eqn in self.eqnDatabase.items():
				for after in varsAfter:
					if (var[0] in eqn[1]) and (after in eqn[1]): #If it contains somthing I am looking for & a var from after
						possibleEqns.update({eqn[0]:eqn[1]}) #Add that equation to possibleEqns
						possibleNames.append(eqn[0])

		if possibleEqns == {}: #There was nothing that fit the joint criteria above, just focus on the varsSearch.
			for var in varsSearch.items(): #Look at each variable in turn
				for eqn in self.eqnDatabase.items():
					if var[0] in eqn[1]: #If it contains somthing I am looking for
						possibleEqns.update({eqn[0]:eqn[1]}) #Add that equation to possibleEqns
						possibleNames.append(eqn[0])

		#Analyze each one.
		countList = [[],[]]
		self.varsAfter = varsAfter
		for eqn in possibleEqns.items(): #Look at each possible equation in turn
			nameList = ['unknown','varsAfter']
			for i in range(2):
				count = 0
				for var in getattr(self,nameList[i]).keys(): #How many of each does it have?
					if var in eqn[1]: count +=1
				countList[i].append(count)

		##Best: Has the most varAfter. If no varsAfter: Has the least unknowns, but atleast 2
		indexList = [np.array(countList[0]).argmax(),np.array(countList[1]).argmin()]#Most varsAfter or least unknown
		if countList[1][indexList[1]] > 0: self.myEqns.update({possibleNames[indexList[1]]:self.eqnDatabase[possibleNames[indexList[1]]]})
		else: self.myEqns.update({possibleNames[indexList[0]]:self.eqnDatabase[possibleNames[indexList[0]]]})

	def unknownGoalSetup(self):
		"""
			This creates a list of all the unknowns, with the goal tagged onto the end.
		"""
		goal = goalList[0] #CHANGE THIS when teh function equationFinder can support more than one goal.
		temp = copy.deepcopy(self.unknown)
		temp.append(goal)

	def equationFinder(self,unknownList):
		"""
			This searches through the equation database for which equations can be used.
			It then follows every pathway possible to get to the goal, and puts it in a dictionary.
			The pathways that do not work are deleted from the dictionary.
			It returns the equations with the variable you solve it for as a list that is in the order to be solved.

			Limitations: This does not setup to solve 2 equations with 2 unknowns. 
			It sets up o solve solves 1 equation with 1 unknown, then another equation with 2 unknowns,
			where one of the unknowns happens to be the same as the one that was just solved for.
		"""
		print('Searching the database')
		n = (len(dataBase))
		col,row = -1,-1
		earlyPaths = {} #These are the pathways that were completed before all unknowns were used up.
		temp = {} #A dictionary of all the ways
		wayCount = 0 #How many ways there are to solve it
		myMatrix = [[],[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]

		#First, have it search for the 1 step solutions.
		for j in range(len(goalList)):
			for eqn in dataBase.items():
				row += 1
				myMatrix[0].append(eqn[0])
				col = 0
				for var in unknownList:
					col += 1
					if var in eqn[1]: myMatrix[1][row].append(1)
					else: myMatrix[1][row].append(0)
				if (1 not in myMatrix[1][row][0:-1]) and (myMatrix[1][row][-1] == 1): #Delete all that contain only my goal & store them (which is the last one in the list. Always.)   
					wayCount += 1
					earlyPaths.update({'way'+str(wayCount):[[],[],[],[myMatrix[0][row],unknownList[-1]]]})
					del myMatrix[1][row],myMatrix[0][row]
					row -= 1
				elif 1 not in myMatrix[1][row]: #Delete all that contain pure zeros  
					del myMatrix[1][row],myMatrix[0][row]
					row -= 1

		#{way1: [[eqnsLeft],[[varAvailable],[varToSolveFor]],[eqnsPathway]], way2: ...
					#eqnsPathway: [[eqn1,var1],[eqn2,var2],...


		#Re-order it so that one with just one 1 is at the top
			##How many contain just 1 on the top? Make a separate matrix for each of those. Delete the others from eachother's matrix. This means that Each matrix will start with a differet eqn.
		for i in range(len(myMatrix[1])):
			if (sum(myMatrix[1][i][0:-1]) == 1) and (myMatrix[1][i][-1] != 1):
				wayCount += 1
				j = 0
				for element in myMatrix[1][i]: #find which unknown is being solved for
					j+=1
					if element == 1: n = j #where the 1 is located
				#print(unknownList[n])
				unknownListTemp = copy.deepcopy(unknownList)
				del unknownListTemp[n]
				temp.update({'way'+str(wayCount):[[myMatrix[0]],[unknownListTemp],[],[[myMatrix[0][i],unknownList[n]]]]})
				myMatrix[1][i] = 'used'
		while 'used' in myMatrix[1]: #Remove the used rows from the matrix
			n = myMatrix[1].index('used')
			del myMatrix[0][n], myMatrix[1][n]
		for item in temp.items():
			newList = item[1]
			newList[2] = myMatrix[1]
			newList[1] = [unknownList,newList[1][0]]
			newList[0] = newList[0][0]
			temp.update({item[0]:newList})

		#Loop until just the goal var remains:
			#Get one that contains that one and another one below it. This can be done by searching for a line that has that var and another 1.
				##After this is done, delete the entire column of the previous variable. Add the name of that variable to another list.
		for k in range(len(unknownList)-1):#This loop will end just before only the goal var remains
			tempNew = copy.deepcopy(temp)
			#print('Iteration', k)
			for item in temp.items(): #Look at each way
				#print(item,'\n')
				unknownHaveList = copy.deepcopy(item[1][1][1]) #Vars to solve for
				unknownNeedList = copy.deepcopy(item[1][1][0]) #Vars available.
				tempMatrix = copy.deepcopy([item[1][0],item[1][2]])
				eqnPath = copy.deepcopy(item[1][3])
				for var in unknownNeedList: #Lets remove the variable that is solved in this way.
					if var not in unknownHaveList:
						n = unknownNeedList.index(var)
						for row in tempMatrix[1]:
							del row[n]
							unknownNeedListTemp = copy.deepcopy(unknownNeedList) #And record which variable was solved
							unknownNeedListTemp.remove(var)
							
				passed,i = False,0 #For if there is another way that branches off of this way.
				for i in range(len(tempMatrix[1])):
					eqnPathTemp = copy.deepcopy(eqnPath)
					if (sum(tempMatrix[1][i][0:-1]) == 1) and (tempMatrix[1][i][-1] != 1):
						j = 0
						for element in tempMatrix[1][i]: #find which unknown is being solved for
							j+=1
							if element == 1: n = j #where the 1 is located
						unknownListTemp = copy.deepcopy(unknownHaveList)
						eqnPathTemp.append([tempMatrix[0][i],unknownListTemp[n]])
						del unknownListTemp[n] #Remove the column that has been solved for already           
						tempMatrix[1][i] = 'used' #Set the eqn up to be removed
						if passed == True: #If there is another way
							wayCount += 1
							tempNew.update({'way'+str(wayCount):[tempMatrix[0],[unknownNeedListTemp,unknownListTemp],tempMatrix[1],eqnPathTemp]})
						else: tempNew.update({item[0]:[tempMatrix[0],[unknownNeedListTemp,unknownListTemp],tempMatrix[1],eqnPathTemp]}) #If this is the first way of the many or just the only way.
						passed = True

					elif (1 not in tempMatrix[1][i][0:-1]) and (tempMatrix[1][i][-1] == 1): #This is for the case that it can be solved early
						tempMatrix[1][i] = 'used'
						eqnPathTemp.append([tempMatrix[0][i],unknownHaveList[-1]])
						if passed == True: #If there is another way
							wayCount += 1
							earlyPaths.update({'way'+str(wayCount):[[],[],[],[eqnPathTemp]]})
						else:earlyPaths.update({item[0]:[[],[],[],[tempMatrix[0][i],unknownList[-1]]]}) #If this is the first way of the many or just the only way.
						passed = True
						
					elif (len(unknownHaveList) == 1) and (tempMatrix[1][i][0] == 1): #This runs instead for the last run.
						tempMatrix[1][i] = 'used'
						eqnPathTemp.append([tempMatrix[0][i],unknownHaveList[0]])
						if passed == True: #If there is another way
							wayCount += 1
							tempNew.update({'way'+str(wayCount):[tempMatrix[0],[unknownNeedListTemp,unknownListTemp],tempMatrix[1],eqnPathTemp]})
						else: tempNew.update({item[0]:[tempMatrix[0],[unknownNeedListTemp,unknownListTemp],tempMatrix[1],eqnPathTemp]}) #If this is the first way of the many or just the only way.
						passed = True
					
				if passed != True: #There were none that could follow it.
					del tempNew[item[0]] #This means that this path cannot continue. So, let's get rid of it.
			for item in tempNew.items():
				while 'used' in item[1][2]: #Remove the used rows from the matrix
					n = item[1][2].index('used')
					del item[1][0][n], item[1][2][n]
			temp = copy.deepcopy(tempNew) #update the new myMatrix

	#Once the path is complete, return a list of just the eqn names as a list in the order they are to be done. Return all possibilities
			temp.update(earlyPaths) #Include the pathways that were found early
			self.equations = []
			for item in temp.items():
				self.equations.append(item[1][3])

	def solver(self,eqns):
		"""
		This takes all the equations given to it and does either 'Linear Solve' or 'Gauss-Sidel' until it finds an answer.
		If it diverges during Gauss-Sidel, it re-arranges the equations using sympy.
		It saves all the variables to the class function.

		If there are multiple ways to solve the problem, it chooses one at random, and if that doesn't work it deletes it.
		It then tries the next way. Theoretically, any way that is provided it should work. This is just a precaution.
			~~~ A future update could handle requests for alternative ways to solve it.
			Note: This does not handle gaussSidel equations yet.
			~~~ For the goal, it would be nice if it returned (1) a rounded answer, and (2) in the units your goal is in.

		"""
		print('Solving')

		for item in self.equations:
			answer = ridder(self,item[0]+'Eqn',item[1])
			setattr('self',item[1],answer[0])
			if item != self.equations[-1]:
				print('I used equation ',item[0],' and solved for ',item[1],'. The answer was ',answer[0],' with a percent error of ',answer[1])
			else:
				print('I used equation ',item[0],' and solved for ',item[1],', your goal. The answer was ',answer[0],' with a percent error of ',answer[1])
		print('Thank You for using our program.')

	def f(self,fn):
		"""
			This function simply runs a function and returns the answer.
		"""
		if self.subject == 'thermo':
			return LogicThermoEquations.fn(self)
#		elif self.subject == 'statics':
#			return LogicStaticsEquations.fn(self)

	def ri(self,eq,var,guess=[-10*10**90,10*10**90],erdes=0.00001):
		"""
			Solves one equation for one unknown using ridder's methood.
			'eq' is the equation to be solved.
			'var' is the variable that is being solved for.
			'guess' is the bounds which the answer is in.
			'erdes' is the desired error
		"""
		x1, x2, erdes = guess[0], guess[1], erdes/100
		n = math.ceil(math.log(abs(x1-x2)/erdes)/math.log(2))
		for i in range(int(n)):
			setattr('self',var,x1)
			f1 = f(eq)
			setattr('self',var,x2)
			f2 = f(eq)
			x3 = (x1+x2)/2
			setattr('self',var,x3)
			f3 = f(eq)
			x4 = x3+(x3-x1)*np.sign(f1-f2)*f3/math.sqrt(f3**2-f1*f2)
			setattr('self',var,x4)
			f4 = f(eq)
			if f3*f4<0: x1,x2 = x3,x4
			elif f1*f4<0: x2 = x4
			elif f2*f4<0: x1 = x4
			else: break
		error = abs((x1-x2)/x2)*100
		return x4,error

	def gauss(self,eqns,erdes=0.00001):
		"""
		'eqns' is the equation names. [eq1,eq2,eq3]. They are solved in that order.
		'erdes' is the desired error.

		Example Input: gauss([f1,f2],0.01)
		"""
		noFun = len(eqns)
		var = [3.14688]*noFun
		varNew = var[:]
		error = [10000]*noFun
		varDif=[3.14688]*noFun
		nHistory =[]
		count = 0

		while max(error) > erdes:
			for i in range(noFun): varNew[i] = f(eqns[i],var) #solve each function

			for i in range(noFun): error[i],varDif[i] = abs((varNew[i]-var[i])/varNew[i]),(abs(varNew[i]-var[i])/2)

			for i in range(noFun):
				if varDif[i]==max(varDif):
					n=i
					nHistory.append(varNew[n])

			count,var = count + 1,copy.deepcopy(varNew)
			if count == 10: #This Must always be an even Number. #It hasn't begun to converge within 10 iterations. So, Is it diverging?
				var = [3.14688]*noFun 
				varNew = var[:]
				halfLength = len(nHistory)/2
				firstHalf = 0
				secondHalf = 0
				for i in range(int(halfLength)):
					firstHalf = firstHalf + nHistory[i]
					secondHalf = secondHalf + nHistory[i+int(halfLength)]
				half1 = firstHalf/halfLength
				half2 = secondHalf/halfLength
				if abs(half1) < abs(half2):
					print('This function Diverges. Re-do.')
					sys.exit(0)
			#    else:
			#        print('It converges. I shall continue.')
		return varNew,error