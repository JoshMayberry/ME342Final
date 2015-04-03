#goalMatrix = [['m2','V2','k','wb'],
#              [1, 0, 0, 0],
#              [1, 1, 0, 0],
#              [0, 1, 1, 0],
#              [1, 0, 1, 1]]

          
#Delete all that contain only my goal (which is the last one in the list. Always.)
#Delete any that conatin all variables?
#Look for a flow.
    #Re-order it so that one with just one 1 is at the top
    #Get one that contains that one and another one below it.

#Bug: Replace all n with k in main program.
#Bug: Add v2 and v1 to the places that have v. Same for T and P, etc.
import numpy as np
import copy

#Input
givenList = ['V1','P1','T1','P2','T2']
goalList = ['Wb']
#unknownList = ['m1','V2','n','Wb']
unknownList = ['m1','V1','n','Wb']
#unknownList = ['R']

#Program
dataBase = {'roeVA1': ['mdot1','roe','Velo1','A1'], 'roeVdot1': ['mdot1','roe','Vdot1'],
	    'vRoe1': ['v1','roe'], 'hupv1': ['hi','u1','P1','v1'], 'pvrt1': ['P1','v1','R','T1'],
            'pvmrt1': ['P1','V1','m1','R','T1'],         
            'roeVA2': ['mdot2','roe','Velo2','A2'], 'roeVdot2': ['mdot2','roe','Vdot2'],
	    'vRoe': ['v2','roe'], 'hupv': ['he','u2','P2','v2'], 'pvrt': ['P2','v2','R','T2'],
            'pvmrt': ['P2','V2','m2','R','T2'],
            'Tconst': ['T1','T2'], 'Pconst': ['P1','P2'], 'hconst': ['hi','he'], 'uconst':['u1','u2'], 'vconst':['v1','v2'],
            'Vconst': ['V1','V2'], 'mconst': ['m1','m2'], 'kcpcv': ['n','Cp','Cv'],
            'cpcvr': ['Cp','Cv','R'], 'deltaU': ['u2','u1','Cv','T2','T1'],
            'deltaH': ['he','hi','Cp','T2','T1'], 'deltaHIncom1': ['he','hi','Cp','v1','T2','T1','P2','P1'],
            'wbIntEqn': ['Wb','P1','V2','V1'], 'wbDeltaVEqn': ['Wb','P1','V2','V1'],
            'wbn': ['Wb','P2','P1','V2','V1','n'], 'wbnmr': ['Wb','T2','T1','m1','R','n'],
            'wbnm': ['Wb','P2','P1','v2','v1','m1','R','n'], 'wbn1v': ['Wb','P1','V2','V1'],
            'wbn1p': ['Wb','P2','P1','V1'], 'wbn1mrv': ['Wb','V2','V1','m1','R','T1'],
            'wbn1mrp': ['Wb','P2','P1','m1','R','T1'],
            'wbTotal': ['W','Wb','We','Ws'],
            'we': [], 'ws': [],
            'EnergyBalance': ['Q','Wb','mi','me','hi','he','ki_v','ke_v','pi_h','pe_h','m2','m1','u2','u1','k2_v','k1_v','p2_h','p1_h'],
            'effThWQh': ['effTh','Wb','Qh'], 'effThQhQl': ['effTh','Qh','Ql'],
            'effThWQhQl': ['Wb','Qh','Ql'], 'copHpWQh': ['copHp','Qh','Wb'],
            'copRefWQh': ['copRef','Ql','Wb'], 'copRefQhQl': ['copRef','Qh','Ql'],
            'copRefWQhQl': ['Wb','Qh','Ql'], 'copHpRef': ['copHp','copRef']
            } #Remove all the b from the Wb after EnergyBalance eventually.
n = (len(dataBase))
col,row = -1,-1
myMatrix = [[],[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]]

for j in range(len(goalList)):
    for eqn in dataBase.items():
        row += 1
        myMatrix[0].append(eqn[0])
        col = 0
        for var in unknownList:
            col += 1
            if var in eqn[1]: myMatrix[1][row].append(1)
            else: myMatrix[1][row].append(0)
        if 1 not in myMatrix[1][row][0:-1]: #Delete all that contain only my goal (which is the last one in the list. Always.)   
            del myMatrix[1][row],myMatrix[0][row]
            row -= 1

print('Analyzing...')
temp = {} #A dictionary of all the ways
wayCount = 0 #How many ways there are to solve it

#Re-order it so that one with just one 1 is at the top
    ##How many contain just 1 on the top? Make a separate matrix for each of those. Delete the others from eachother's matrix. This means that Each matrix will start with a differet eqn.
for i in range(len(myMatrix[1])):
    if (sum(myMatrix[1][i][0:-1]) == 1) and (myMatrix[1][i][-1] != 1):
        wayCount += 1
        j = 0
        for element in myMatrix[1][i]: #find which unknown is being solved for
            j+=1
            if element == 1: n = j #where the 1 is located
        unknownListTemp = unknownList[:]
        del unknownListTemp[n]
        temp.update({'way'+str(wayCount):[[myMatrix[0]],[unknownListTemp],[]]}) #{way1: [[eqnTitles],[varToSolveFor],[eqnsLeft]],
        myMatrix[0][i],myMatrix[1][i] = ('used',)*2
while 'used' in myMatrix[0]: #Remove the used rows from the matrix
    n = myMatrix[0].index('used')
    del myMatrix[0][n], myMatrix[1][n]
for item in temp.items():
    newList = item[1]
    newList[2] = myMatrix[1]
    newList[1] = newList[1][0]
    newList[0] = newList[0][0]
    temp.update({item[0]:newList})
#print(temp)
#Loop until just the goal var remains:
    #Get one that contains that one and another one below it. This can be done by searching for a line that has that var and another 1.
        ##After this is done, delete the entire column of the previous variable. Add the name of that variable to another list.
for k in range(len(unknownList)-1):#This loop will end when just the goal var remains
    tempNew = copy.deepcopy(temp)
    print('Iteration ',k)
    for item in temp.items(): #Look at each way
        print(item,'\n')
        newUnknownList = copy.deepcopy(item[1][1])
        tempMatrix = copy.deepcopy([item[1][0],item[1][2]])
        print(unknownList)
        nextUnknownListTemp = []
        for var in nextUnknownList: #Lets remove the variable that is solved in this way.
            if var not in newUnknownList:
                n = unknownList.index(var)
                if n != 'used':
                    for row in tempMatrix[1]:
                        del row[n]
                    nextUnknownListTemp.append(var)

#            print(nextUnknownListTemp)  
        passed,i = False,0 #For if there is another way that branches off of this way.
        for i in range(len(tempMatrix[1])):
            if (sum(tempMatrix[1][i][0:-1]) == 1) and (tempMatrix[1][i][-1] != 1):  
                j = 0
                for element in tempMatrix[1][i]: #find which unknown is being solved for
                    j+=1
                    if element == 1: n = j #where the 1 is located
                unknownListTemp = copy.deepcopy(newUnknownList)
                del unknownListTemp[n] #Remove the column that has been solved for already           
                tempMatrix[0][i],tempMatrix[1][i] = 'used','used' #Set the eqn up to be removed
                if passed == True: #If there is another way
                    wayCount += 1
                    tempNew.update({'way'+str(wayCount):[[tempMatrix[0]],[unknownListTemp],[tempMatrix[1]]]}) #{way1: [[eqnTitles],[varToSolveFor],[eqnsLeft]],
                else:
                    tempNew.update({item[0]:[tempMatrix[0],unknownListTemp,tempMatrix[1]]}) #If this is the first way of the many or just the only way.
                passed = True
        if passed != True: #There were none that could follow it.
            #tempNew.update({item[0]:[['failed'],['failed'],['failed']]}) #This means that this path way did not work.
            del tempNew[item[0]] #This means that this path cannot continue. So, let's get rid of it.
    for item in tempNew.items():
        while 'used' in item[1][0]: #Remove the used rows from the matrix
            n = item[1][0].index('used')
            del item[1][0][n], item[1][2][n]
    temp = copy.deepcopy(tempNew) #update the new myMatrix
    #print('\n',temp)

#This is another function (What it passes them to):
#Pass the remaining ways to the solver function and have it solve each pathway. Have it rturn the answer that is most common. If all answers are close to eachotehr, return an average.
    ##The solver will solve the first eqn for the first variable, then it will write that value to the variable. Then, on to the next eqn.








    
