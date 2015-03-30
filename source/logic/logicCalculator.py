import wx
import numpy as np #For the argmax() functionality
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
		self.equationFinder(self)

	#Solve the equations
#		self.solver(self,self.equations)

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

	def equationFinder(self):
		"""
		What needs to happen is that a path must be generated for Gauss-Sidel.

		Psudocode:
			- Import all the equations as a matrix.
			- Start at an equation with your goal.
			- Go to the cell of an unknown var in that eqn.
			- Go dowin the column to that same var in anotehr eqn.
			- Go to the cell of a different unknown var in that eqn.
			- 



			- What is the best equation that contains what I know?
			- What are the best equations that contain my goals?

			Loop until all the equations flow into and back from eachother.
				Move them around to see if that makes them work.
				If they all get back to their origonal position, you need another equation.
					Search for one that contains a variable from the first and a variable from the second.
						If you find it, then lock that in place.
						If you don't, then just look for one with a variable from the first. Choose the best one.

			- Once the path is complete, return a list of just the eqn names as a list in the order they are to be done.


		'myEqns' is a growing list where each element contains a list for each level of analysis.

		Note: Equations come in as turples of (eqnName,List of what vars are in it)
		"""
		print('Finding Equations')






























































	#Make known variables constants.

	#What is the best equation that contains what I know?
#		self.myEqns = {} #The equations I will use
#		self.eqnDatabaseContains(self,self.known,self.goal)

	#What are the best equations that contain my goals?
#		self.eqnDatabaseContains(self,self.goal,self.known)

	##The current Equation order is [One with what I know, One for my goals]
		#We need to see if it can flow from one variable in the first equation to the next equation, and back to the frist.
#		print(self.myEqns)		

	#Move them around to see if that makes them work.
	
	#If they all get back to their origonal position, you need another equation.
	
	#Search for one that contains a variable from the first and a variable from the second.
	
	#If you find it, then lock that in place.
	
	#If you don't, then just look for one with a variable from the first. Choose the best one.
















#	#What variables within those eqns do I not know?
#		for j in range(len(self.goal)): #Look at each goal in turn
#			for eqnVar in self.myEqns.values(): #Look at each equation in turn
#				for i in range(len(eqnVar)): #Look at each variable in turn
#					if eqnVar[i] not in self.known.keys(): #If this equation variable is unknown
#						self.unknown.update({eqnVar[i]:'unknown'})

	#Start Loop Here
	#What equations contain a variable I do not yet know?
#		possibleEqns = {} #This is a dictionary of the possible equations to choose
#		j,i = 0,0
#		for var in self.unknown.keys(): #Look for each unknown variable in the current database equation in turn
#			j+=1
#			for eqn in self.eqnDatabase.items(): #Look at each database equation in turn
#				i+=1
#				if var in eqn[1]: #If the unknown variable is in the current equation
#					#print(eqn[0],possibleEqns.keys())
#					if eqn[0] not in possibleEqns.keys():
#						#print('yes')
#						setattr(self,var + 'dict',{})
#						getattr(self,var + 'dict').update({eqn[0]:eqn[1]}) #Put it into the temp dict for that var
#						#print(getattr(self,var + 'dict'))
#			if hasattr(self,var + 'dict'): possibleEqns.update(getattr(self,var + 'dict')) #Put all those eqns into a list as [var, eqns it is in]
#			if hasattr(self,var + 'dict'): possibleEqns.append([var, getattr(self,var + 'dict')]) #Put all those eqns into a list as [var, eqns it is in]
	##Compare the dictionaries for each unknown variables and choose the one that has the most unknowns in it
		#How many vars from self.unknown are in each?
#		i,countList,countEqnList = 0,[],[]
#		for eqn in possibleEqns.items():
#			i+=1
#			count = 0
#			for var in self.unknown.keys(): #Count how many of the unknowns the equation contains
#				#print(var,eqn)
#				if var in eqn[1]:
#					#print('yes')
#					count+=1
#			countList.extend([count]) #[how many vars eqn1 contains, how many vars eqn2 contains,...]
#			countEqnList.extend([eqn[0]])
#		n = np.array(countList).argmax() #The index of the one that contains the most
#		self.myEqns.update({countEqnList[n]:self.eqnDatabase[countEqnList[n]]}) #Add this equation to self.myEqns.
#
#		#we're done now, so free up the memory
#		for var in self.unknown.keys():
#			if hasattr(self,var + 'dict'): delattr(self,var + 'dict')
#			del possibleEqns,countList,countEqnList,i,j

	#What is the arrangement of these equations?

		#Set the order at random.

		#If the equation after one of them has the same unknown in it, lock it in place.
		
	#This is only to be done once for an equation.
		
	#else: Shift it down to the next break in the path. Check if it works
		
	#If it does not work, shift it again.
		
	#If it returns t it's origonal position
		
	#Find a new eqn that contains that unknown and one in the next eqn.
		
	#If this doesn't work, have it shift to the next break and try again.
		
	#If it returns to it's origonal position, just find a new eqn that contains that unknown.
		
	#Lock the new eqn to after this eqn.
	
	#If it runs out of possible new eqns, remove all locks and randomly mix the eqns. Do it all agian.
		
	#If this still doesn't work, start over from the start.

	#Once the path is complete, return a list of just the eqn names as a list in the order they are to be done.
#		self.equations = 
	


	def solver(self,eqns):
		"""
		This takes all the equations given to it and does Gauss-Sidel until it finds an answer.
		If it diverges, it re-arranges the equations using sympy.
		It returns all the variables.
		"""
		print('Solving')

	def f(self,fn,var):
		return fn(var)

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

			count,var = count + 1,varNew[:]
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
		return varNew,count,error
