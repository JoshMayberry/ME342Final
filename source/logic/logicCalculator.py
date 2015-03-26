import wx
#from .logicThermoInput import LogicThermoInput

class LogicCalculator:#LogicThermoInput):
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
	#What have I been given?
		self.subject = args[0]

	#What is known? What is not known?
		self.unknown,self.known = {},{} #Blank dictionaries
		for i in kwargs.items():
			if '@' not in i:
				if ('unknown' in i) or ('' in i): 
					if i[0][0] != 'U': self.unknown.update({i[0]:i[1]})
				else: 
					if i[0][0] != 'U': self.known.update({i[0]:i[1]})

	#What do  I need to find?
		self.goal = args[1]

	#Equations
	##Retrieve the correct Equation Database
		if self.subject == 'thermo':
			from .logicThermoEquations import LogicThermoEquations
			self.eqnDatabase = LogicThermoEquations.eqnDatabase(self)
#		elif self.subject == 'statics': 		#This is to show how to add another subject.
#			from .logicStaticsEquations import LogicStaticsEquations
#			self.eqnDatabase = LogicStaticsEquations.eqnDatabase(self)

	##Search through that Database for the relevant equations
		equations = self.equationFinder()

	#Solve the equations
		solved = self.solver(equations)

	#Return your answer
		#Have it go through the answers and return only the ones that we want.

	def equationFinder:
		"""
		What needs to happen is that a path must be generated for Gauss-Sidel.
		Known variables constants

		Psudocode:
			- Make known variables constants.
			- What equations contain what I need to find?
				(These equations are the base that our path is built off of.)
			- What variables within those eqns do I not know?
			- loop: for each unknown in the eqn:
				- What equations contain a variable I do not yet know?
					~ If there is more than one, which has the most known variables in it?
						~ If they have the same amount, choose one at random.

			- What is the arrangement of these equations?
				~ Set the order at random.
				~ If the equation after one of them has the same unknown in it, lock it in place.
					~ This is only to be done once for an equation.
				~ else: Shift it down to the next break in the path. Check if it works
					~ If it does not work, shift it again.
					~ If it returns t it's origonal position
						~ Find a new eqn that contains that unknown and one in the next eqn.
							~ If this doesn't work, have it shift to the next break and try again.
							~ If it returns to it's origonal position, just find a new eqn that contains that unknown.
						~ Lock the new eqn to after this eqn.
					~ If it runs out of possible new eqns, remove all locks and randomly mix the eqns. Do it all agian.
					~ If this still doesn't work, start over from the start.

			- Once the path is complete, return a list of just the eqn names as a list in the order they are to be done.


		'myEqns' is a growing list where each element contains a list for each level of analysis.

		Note: Equations come in as turples of (eqnName,List of what vars are in it)
		"""
		print('Finding Equations')
	#Make known variables constants.


	#What equations contain what I need to find?
		self.myEqns = {} #The equations I will use
		for j in range(len(goal)): #There can be multiple goals
			for i in self.eqnDatabase.items():
				if goal[j] in i[1]: #If it contains somthing I am looking for
					self.myEqns.update({i[0]:i[1]}) #Add that equation to myEqns.

	#Which of those equations include the variables I have been given?
		for eqn in self.myEqns.items(): #Look at each equation in turn
			j+=1
			for i in range(len(eqn[1][j])): #Look at each variable the equation has in it in turn
				var = eqn[1][j] #This makes it easier to understand the code
				if self.known.has_key(var[i]) == False: #If it has a variable that is 'unknown'	
					self.unknown.update({var[i]}:'unknown') #Add this to my list of unknown variables (or affirm it's continued existance)
				else: #If that variable is present in the eqns:


	#What equations can I use to get the variables that I still need? (This will be a loop)


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
