import wx
import numpy as np #For the argmax() functionality
import math
import copy #This is needed because sometimes the temp lists modify their parent lists. So, deep copies are made.


class LogicCalculator:
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
		print('\nsubject: ',self.subject, '\nmedium: ',self.medium)

	#What is known? What is not known?
		self.unknown,self.known = {},{} #Blank dictionaries
		for i in kwargs.items():
			if '@' not in i:
				if ('unknown' in i) or ('' in i): 
					if i[0][0] != 'U': self.unknown.update({i[0]:i[1]})
				else: 
					if i[0][0] != 'U':  self.known.update({i[0]:i[1]})
		#For now, we will not worry about these.			
		self.unknown.update({'MM':'unknown','R':'unknown','Tcr':'unknown','Pcr':'unknown','Vcr':'unknown'})
		print('\nknown: ',self.known,'\nunknown: ',self.unknown)

	#What do  I need to find?
		self.goal = args[1]
		print('\ngoal: ',self.goal)

		for element in ['known','unknown','goal']: #Set the values in the system
			for item in getattr(self,element).items(): 
				setattr(self,item[0],item[1])

	#Equations
	##Retrieve the correct Equation Database & other things pertaining to the subject.
		print('Loading Database')
		if self.subject == 'thermo':
			from .logicThermoEquations import LogicThermoEquations
			from .logicThermoTableLookup import TableUtilities
			self.medium = args[2]
			constants = LogicThermoEquations.constants()
			for item in constants.items():
				setattr(self,item[0],item[1]) #Record the constants
			self.eqnDatabase = LogicThermoEquations.eqnDatabase(self)
			print('    ~ Thermo Database Loaded')

			table_utils = TableUtilities()

			##Lookup all unknown values that can be gotten from the Thermo Tables
			if self.medium in ['Water', 'R134a']:
				pass #Get this working
			else:
				if 'MM' in self.unknown: 
					self.MM = table_utils.TableDecider(['A1',['Molar Mass',self.medium,'N/A']])
				if 'R' in self.unknown: 
					self.R = table_utils.TableDecider(['A1',['Gas Constant R',self.medium,'N/A']])
				if 'Tcr' in self.unknown: 
					self.Tcr = table_utils.TableDecider(['A1',['Critical Temperature',self.medium,'N/A']])
				if 'Pcr' in self.unknown: 
					self.Pcr = table_utils.TableDecider(['A1',['Critical Pressure',self.medium,'N/A']])
				if 'Vcr' in self.unknown: 
					self.Vcr = table_utils.TableDecider(['A1',['Critical Volume',self.medium,'N/A']])
				for element in ['MM','R','Tcr','Pcr','Vcr']:
					if element in self.unknown: 
						del self.unknown[element] #Remove found values from the unknown list
					self.known.update({element:getattr(self,element)}) #Add found values to the known list

			self.interThermoPassed = False #This will be true once it has been able to do a full table lookup.
			self.intermediateStep(self)

#		elif self.subject == 'statics': 		#This is to show how to add another subject.
#			from .logicStaticsEquations import LogicStaticsEquations
#			self.eqnDatabase = LogicStaticsEquations.eqnDatabase(self)

	##Search through that Database for the relevant equations
			temp = self.unknownGoalSetup(self)
			self.equationFinder(self,temp)

	#Solve the equations
			self.solver(self,self.equations) #Find any others that can be found

	#Return your answer
		#Have it go through the answers and return only the ones that we want.

	def intermediateStep(self):
		"""
			This does things that must be checked between steps of gauss sidel or linear solver.

			For thermo, this is a check if the values of the tables can be/have been found.
			Once self.interThermoPassed == True, then this doesn't run any more, because all values have been gotten from the tables.
		"""
		if self.subject == 'thermo':
			if self.interThermoPassed == False:
				table_utils = TableUtilities()
				answer = table_utils.TableEnough(self.unknown, self.known, self.medium)
				if answer != []: #There was enough
					self.interThermoPassed = True
					for element in answer:
						setattr(self,element[0],element[1])
						del self.unknown[element[0]]
						self.known.update({element[0]:element[1]})

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
		temp = []
		for item in self.unknown.items():
			temp.append(item[0])
		for item in self.goal.items():
			temp.append(item[0])
		return temp

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
		n = (len(self.eqnDatabase))
		col,row = -1,-1
		earlyPaths = {} #These are the pathways that were completed before all unknowns were used up.
		temp = {} #A dictionary of all the ways
		wayCount = 0 #How many ways there are to solve it
		myMatrix = [[],[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]


		###This is still undr development. 
		#Input 
		known =  {'T1': 453.15, 'P1': 130.0, 'V1': 0.07, 'P2': 80.0} 
		unknown =  {'MM': 'unknown', 'x1': 'unknown', 'Cp': 'unknown', 'u2': 'unknown', 's1': 'unknown', 'V2': 'unknown', 'x2': 'unknown', 'R': 'unknown', 's2': 'unknown', 'v1': '', 'Q': 'unknown', 'v2': 'unknown', 'Pcr': 'unknown', 'T2': 'unknown', 'Cv': 'unknown', 'k': 'unknown', 'Cavg': 'unknown', 'Tcr': 'unknown', 'm2': 'unknown', 'roe': 'unknown', 'u1': 'unknown', 'Vcr': 'unknown', 'm1': 'unknown'}
		goal =  {'W': 'unknown'} 

		n = (len(dataBase))
		col,row = 0,0
		earlyPaths = {} #These are the pathways that were completed before all unknowns were used up.
		paths = {} #A dictionary of all the ways
		wayCount = 0 #How many ways there are to solve it
		myMatrix = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]



		for endVar in goal.items(): #First, label which variable is for which column
			for var in unknown.items():
				myMatrix[0].append(var[0])
			myMatrix[0].append(endVar[0])
		for eqn in dataBase.items(): #Second, label which equation is for which row
			row += 1
			myMatrix[row].append(eqn[0])
			for item in unknown.items(): #Fill in the 1 and 0
				if item[0] in eqn[1]:
					myMatrix[row].append(1)
				else:
					myMatrix[row].append(0)
		row = 0
		for eqn in myMatrix[1:]: #Third, have it search for the 1 step solutions & non-useable equations.
			row += 1
			print(eqn[1:])
			if sum(eqn[1:]) == 0:  #Weed out the eqns that are pure 0
				print('    =0')
				del myMatrix[row]
				row -= 1
			if (1 not in eqn[1:-1]) and (eqn[-1] == 1): #Delete all that contain only my goal & store them (which is the last one in the list. Always.)   
				print('    Only Goal')
				wayCount += 1
				col = np.argmax(np.array(eqn[1:])) + 1 #Get the positio of the 1
				temp = [myMatrix,myMatrix[row][0],myMatrix[0][col]] #[current myMatrix, eqn, var to solve for]
				del myMatrix[row]
				earlyPaths.update({'way'+str(wayCount):temp})
				row -= 1
			if sum(eqn[1:]) == 1:
				print('    =1')
				wayCount += 1
				col = np.argmax(np.array(eqn[1:])) + 1 #Get the positio of the 1
				temp = [-1,myMatrix[row][0],myMatrix[0][col]] #[current myMatrix, eqn, var to solve for]
				myMatrixTemp = copy.deepcopy(myMatrix)
				del myMatrixTemp[row] #Delete the row
				temp[0] = myMatrixTemp
				for i in range(len(myMatrix)): #Delete the column
					del myMatrix[i][col]
				paths.update({'way'+str(wayCount):temp})
				row -= 1
		row, passedAlready = 0, False
		print(stop)

		for k in range(len(unknown)-1):#Fourth. This loop will end just before only the goal var remains
			for item in paths.items():
				myMatrix = item[1][0][:]
				for eqn in myMatrix[1:]: #Find the equations with 1 unknown.
					row += 1
					if sum(eqn[1:]) == 1:
						col = np.argmax(np.array(eqn[1:])) + 1 #Get the positio of the 1
						temp[1].append(myMatrix[row][0]) #Add eqn
						temp[2].append(myMatrix[0][col]) #Add var
						del myMatrix[row] #Delete the row
						for i in range(len(myMatrix)): #Delete the column
							del myMatrix[i][col]
						temp[0] = myMatrix #Update current myMatrix
						row -= 1
						if passedAlready == False:
							paths.update({item[0]:temp})
						else: #There is another way that branches off of this one.
							wayCount += 1
							paths.update({'way'+str(wayCount):temp})
							passedAlready = True
		print(myMatrix)
		print('\n','early',earlyPaths)
		print('\n','paths',paths)
		print(stop)


		#{way1: [[eqnsLeft],[[varAvailable],[varToSolveFor]],[eqnsPathway]], way2: ...
					#eqnsPathway: [[eqn1,var1],[eqn2,var2],...



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
		print(self.equations)

		for item in self.equations:
			answer = self.ridder(self,item[0]+'Eqn',item[1])
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

	def ridder(self,eq,var,guess=[-10*10**90,10*10**90],erdes=0.00001):
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