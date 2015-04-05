import wx
from ..views import Frm_ThermoTableLookup
#from ..views import Frm_ThermoTableShow
from xlrd import open_workbook, cellname
from xlrd import XL_CELL_TEXT, XL_CELL_NUMBER, XL_CELL_EMPTY, XL_CELL_BLANK
class LogicThermoTableLookup(Frm_ThermoTableLookup):
	def __init__(self,parent):
		Frm_ThermoTableLookup.__init__(self, parent)
		self.table_utils = TableUtilities()

	def onChoiceMedium( self, event): #Setup the rest of the enteries
		self.input[1][1] = self.choice_TT_Medium.GetString(self.choice_TT_Medium.GetSelection())
		if self.input[1][1] in ['Water','R134a']: choices = ['','N/A','Temperature','Sat Pressure','x','vf','vg','uf','ufg','ug','hf','hfg','hg','sf','sfg','sg']
		else: choices = ['','N/A','Temperature','Molar Mass','Gas Constant R','Cp','Cv','k','Critical Temperature','Critical Pressure','Critical Volume'] #It is an ideal Gas
		self.choice_TT_Goal_ColOf.Clear()
		self.choice_TT_Goal_ColOf.Append(choices)
		self.choice_TT_Goal_ColOf.SetSelection(0)
		self.choice_TT_Ref_ColOf.Clear()
		self.choice_TT_Ref_ColOf.Append(choices)
		self.choice_TT_Ref_ColOf.SetSelection(0)
		self.choice_TT_Ref2_ColOf.Clear()
		self.choice_TT_Ref2_ColOf.Append(choices)
		self.choice_TT_Ref2_ColOf.SetSelection(0)
		event.Skip()
	
	def onChoiceGoalColOf( self, event ):
		self.input[1][0] = self.choice_TT_Goal_ColOf.GetString(self.choice_TT_Goal_ColOf.GetSelection())
		event.Skip()
	
	def onChoiceRefColOf( self, event ):
		temp = self.choice_TT_Ref_ColOf.GetString(self.choice_TT_Ref_ColOf.GetSelection())
		if temp == 'N/A': 
			self.input[1][2] = temp
			self.txtCtrl_TT_Ref_RowOf.SetValue(self.input[1][2])
			self.txtCtrl_TT_Ref2_RowOf.SetValue(self.input[1][2])
		else: 
			self.input[1][2][0][0] = temp
		event.Skip()
	
	def onTxtRefRowOf( self, event ):
		temp = self.choice_TT_Ref_ColOf.GetString(self.choice_TT_Ref_ColOf.GetSelection())
		if temp == 'N/A': 
			self.input[1][2] = 'N/A'
			self.txtCtrl_TT_Ref_RowOf.SetValue('N/A')
		else: self.input[1][2][0][1] = eval(self.txtCtrl_TT_Ref_RowOf.GetLineText(0))
		event.Skip()

	def onChoiceRef2ColOf( self, event ):
		temp = self.choice_TT_Ref_ColOf.GetString(self.choice_TT_Ref_ColOf.GetSelection())
		temp2 = self.choice_TT_Ref2_ColOf.GetString(self.choice_TT_Ref2_ColOf.GetSelection())
		if self.input[1][1] in ['Water','R134a']: #Get this working
			pass
		else:
			if temp == 'N/A': 
				self.input[1][2] = 'N/A'
				self.txtCtrl_TT_Ref2_RowOf.SetValue('N/A')
			if temp2 == 'N/A': 
				self.input[1][2][1] = ['N/A']
				self.txtCtrl_TT_Ref2_RowOf.SetValue('N/A')
			else: self.input[1][2][1][0] = temp2
		event.Skip()
	
	def onTxtRef2RowOf( self, event ):
		temp = self.choice_TT_Ref_ColOf.GetString(self.choice_TT_Ref_ColOf.GetSelection())
		temp2 = self.choice_TT_Ref2_ColOf.GetString(self.choice_TT_Ref2_ColOf.GetSelection())
		if self.input[1][1] in ['Water','R134a']:
			pass
		else:
			if temp == 'N/A': 
				self.input[1][2] = 'N/A'
				self.txtCtrl_TT_Ref2_RowOf.SetValue('N/A')
			if temp2 == 'N/A': 
				self.input[1][2][1] = ['N/A']
				self.txtCtrl_TT_Ref2_RowOf.SetValue('N/A')
			else: self.input[1][2][1][1] = eval(self.txtCtrl_TT_Ref2_RowOf.GetLineText(0))
		event.Skip()

	def onBtnClickGo( self, event ):
		"""
			A1 - Molar mass, gas constant & critical point properties
			A2 - Ideal-gas specific heats of various common gases
				(a) At 300 K
				(b) At various tmeperatures
			A3 - Properties of common liquids, solids, and foods
				(a) Liquids
				(b) Solids
			A4 - Saturated water - Temperature table
			A5 - Saturated water - Pressure table
			A6 - Superheated water
			A11 - Saturated refrigerant 134a - Temperature table
			A12 - Saturated refrigerant 134a - Pressure table
			A13 - Superheated refrigerant 134a
			To access the english tables, tag an 'E' on the end.

			Row0: Full Title
			Row2: Column Variables
			Row3: Column Units

			self.input Syntax: ['WhichTable',['In the col of','In the rows of',[['Reference col','Reference value'],['Reference2 col','Reference2 value']]]]
		"""
		#print(self.input)
		if self.input[0] == -1:
			self.input = self.table_utils.TableInquiry(self.input)
		value = self.table_utils.TableDecider(self.input)
		#args = [given,value]					##This is for when it has an option to display All
		#Frm_ThermoTableShow(self,*args).Show() ##This is for when it has an option to display All
		self.txt_TT_AnswerValue.SetLabel(str(value)) ##DELETE THIS when it can support the display All option
		event.Skip()

class TableUtilities:
	def __init__(self):
		self.myBook = open_workbook('source/logic/thermoTable.xlsx')
	
	def TableEnough(self,unknown,known,medium):
		""" This checks if there are enough known variables to look up values in the table."""
		given, passed, temperatureCheck = [-1,[-1,medium,[[-1,-1],[-1,-1]]]], 0, False
		if 'T1' in known: #Finds if you know the temperature or not. Assumes that T1 determines the Cp. CHANGE THIS so it is smarter.
			temperatureCheck = True

		for item in known.items():
			#print('known',item)
			if medium in ['Water','R134a']: #FIX THIS: Make it smart with the criteria for the tables A4, A5, & A6.
				pass
			else: #It is an ideal gas [-1,['Cp','Air',[['Temperature',300],['N/A']]]]
				if temperatureCheck == True:
					if item[0] in ['Cp','Cv','n']:
						given[1][2][0] = ['Temperature',self.known['T1'][1]]

			for item in unknown.items(): #Find the unknowns that can be found.
				#print('unknown',item)
				if 'T' in item[0]: given[1][0] = 'Temperature'
				elif 'Cp' in item[0]: given[1][0] = 'Cp'
				elif 'Cv' in item[0]: given[1][0] = 'Cv'
				elif 'n' in item[0]: given[1][0] = 'k'
				elif 'P' in item[0]: given[1][0] = 'Pressure'
				#elif 'x' in item[0]: #make the rest of the cirteria for Water and R134a.
				given = self.TableInquiry(given) #Which table should be used?

	def TableInquiry(self,given):
		""" This decides which table should be used."""
		if given[1][1] in ['Water','R134a']:
			pass #Make criteria for finding wether it is super heated or not.
		else:
			if given[1][0] in ['Molar Mass','Gas Constant R','Critical']:
				given[0] = 'A1'
				if given[1][2][0] == ['Temperature', 300]: given[1][2] = 'N/A'
			elif given[1][2][0] == ['Temperature', 300]: given[0] = 'A2a'
			else: given[0] = 'A2b'
		return given

	def TableDecider(self,given):
		"""
			This determines first determines which table to use.
			It then determines if interpolation is necissary. It is also the first step.

			Example Input: TableDecider(['A1',['Molar Mass','Air','N/A']]) Answer: 28.97
			Example Input: TableDecider(['A2a',['Gas Constant R','Air',[['Temperature',300],['N/A']]]]) Answer: ['Gas Constant R', 0.2870, 'kJ/kg-K']
			Example Input: TableDecider(['A2b',['Cp','Carbon dioxide',[['Temperature',250],['N/A']]]]) Answer: 0.791
			Example Input: TableDecider(['A2b',['Cp','Air',[['Temperature',275],['N/A']]]]) Answer: 1.004
			Example Input: TableDecider(['A4',['vf','Water',[['Temperature',40],['x',0.5]]]])
			Example Input: TableDecider(['A4',['vf','Water',['Temp',37.5]]])
		"""
		if given[0] == -1: 
			given = self.TableInquiry(given) #Find which sheet, if not specified

		self.mySheet = self.myBook.sheet_by_name(given[0]) #Load the needed sheet
		exists = True
		if isinstance(given[1][2][0], list): #Don't use "if type(given[1][2][0]) == list:"" #Interpolation is possibly needed
			exists = self.TableLookup(given)[1]
		if exists == True: #No interpolation is needed
			answer = self.TableLookup(given)[3]
		else: #Interpolation IS needed
			answer = self.TableInterpolation(given)
		return answer

	def TableLookup(self,given):
		""" 
			This finds values on the tables.
			Those that call it take what they need from the return statement and ignore the rest of what is returned.
		"""
		#print('TableLookup',given)
		rowRef, exists, between, answer = -1, False, [-1,-1], -1
		for i in range(self.mySheet.ncols): #The variable I am looking up
			if self.mySheet.cell(2,i).value == given[1][0]: 
				col = i
				break
		for i in range(self.mySheet.nrows): #What I am using to choose that variable's value
				if self.mySheet.cell(i+4,0).value == given[1][1]:
					rowStart = i+4 #The row where I start counting
					break
		if type(given[1][2][0]) != list: answer = self.mySheet.cell(rowStart,col).value #Meaning there are not multiple enteries
		else: #Meaning there ARE multiple Enteries
			for i in range(self.mySheet.ncols): #The variable I am using to choose which of the mutiple enteries to take a value from.
				if self.mySheet.cell(2,i).value == given[1][2][0][0]: 
					colRef = i
					break
			
			for i in range(self.mySheet.nrows): #What I am using to choose my goal variable's value
				check = type(self.mySheet.cell(i+rowStart,colRef).value) 
				if check in [int,float,complex]:
					if self.mySheet.cell(i+rowStart,colRef).value < given[1][2][0][1]:
						if self.mySheet.cell(i+5,colRef).value > given[1][2][0][1]: #Account for which direction the row increments
							between = [self.mySheet.cell(i+rowStart,colRef).value, self.mySheet.cell(i+5,colRef).value]
						else: between = [self.mySheet.cell(i+3,colRef).value, self.mySheet.cell(i+rowStart,colRef).value]
					elif self.mySheet.cell(i+rowStart,colRef).value == given[1][2][0][1]:
						exists = True
						rowRef = i+rowStart
						answer = self.mySheet.cell(rowRef,col).value
						break
				else: break #At the end of the list 

		return rowRef,exists,between,answer

	def TableInterpolation(self,given):
		""" 
			This interpolates using the tables. It supports quality.

			Example Input: TableLookup(['A2b',['Cp','Air',[['Temperature',275],['N/A']]]])
			Example Input: TableLookup(['A4',['vf','Water',[['Temperature',40],['x',0.5]]]])
		"""
		between = self.TableLookup(given)[2]	#Get the spots between
		x1 = given[1][2][0][1]					#The current reference spot 
		given[1][2][0][1] = between[0]			#Set the value of before to temp
		x0 = between [0]						#The reference spot before
		y0 = self.TableLookup(given)[3]			#The goal spot before
		given[1][2][0][1] = between[1]			#Set the value of after to temp
		x2 = between[1]							#The refernce spot after
		y2 = self.TableLookup(given)[3]			#The goal spot after
		#print('(',x1,'-',x0,')/(',x2,'-',x0,')=(y1-',y0,')/(',y2,'-',y0,')')
		if given[1][2][1][0] == 'x': return y0-(y0-y2)*given[1][2][1][1]
		else: return (x1-x2)*(y0-y2)/(x0-x2)+y2 #The current goal spot