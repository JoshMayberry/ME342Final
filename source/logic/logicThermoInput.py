import wx
from ..views import Frm_ThermoInput #Needed to communicate with the frame
from .logicCalculator import LogicCalculator #Needed to do the calculations before showing the next screen.
import numpy as np

class LogicThermoInput(Frm_ThermoInput):
	"""
		In the GUI, you fill in what variables you know.
		Any variables you do not know, type a '-'. For your goal, type an '@'.
	"""
	def __init__(self, parent,*args):
		#Set variables
		self.inputList = args[0] #This is a list used to generate the text boxes
		self.units = args[1] #This is wether the problem is in Metric or English Units
		self.zeroList = args[2] #This is a list of all the units that are zero by default.
		#self.nameList = [] #This is a list of the generated text boxes so you know the order the units are listed in.
			#Every 'nameList' thing can be deleted if this does not show a use later on.

			#Also, get the box to inteligently pick which unit should be the default.

		#print(self.inputList)
		#print(self.zeroList)

		#Build GUI
		print ("Building ", self.__class__)
		Frm_ThermoInput.__init__(self, parent)

		#Store Defaults in the system.
		for j in range(3):
			for i in range(len(self.inputList[j])):
				#Set the default for the vars on the screen
				setattr(self,self.inputList[j][i],'unknown')
				#Set the units for the vars on the screen.
				unitEvent = 'self.onUnits_TI_'+self.inputList[j][i]+'(wx.EVT_CHOICE)'
				exec(unitEvent)
#		for i in range(len(self.zeroList)):
			#Set the zero vars as zero
#			setattr(self,self.zeroList[i],0)				#Let's try it without the zeroList
			#Set default units for all zero vars
#			setattr(self,'U'+self.zeroList[i],'unitless')

	def setSize(self):
		"""
			This dynamically sets the window size according to how many inputs the longets list has.
		"""
		lengthList = [len(self.inputList[0]),len(self.inputList[1]),len(self.inputList[2])]
		Lmax = np.array(lengthList).argmax()
		n = lengthList[Lmax] #The length of the longest column
		x = 650
		y = 36*(n+3) #n +2 for the title and +1 for the button
		return [x,y]

	def CreateState1(self,sz_TI_State1):
		"""
			This populates all of State 1 with the necissary variables.
			What is necissary was decided in the previous frame.
		"""
		print('Setting up State 1')
		for i in range(len(self.inputList[0])):
			#Make the text label
			#txtName = 'txt_TI_'+ str(self.inputList[0][i])
			self.txtName = wx.StaticText( self, wx.ID_ANY, self.inputList[0][i], wx.DefaultPosition, wx.DefaultSize, 0  )
			self.txtName.Wrap( -1 )
			sz_TI_State1.Add( self.txtName, 0, wx.ALL, 5 )

			#Make the input box
			#valName = 'self.val_TI_'+ str(self.inputList[0][i])
			valId = 500 + i #This is so I can find it later
			valName = wx.TextCtrl( self, valId, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0  )
			sz_TI_State1.Add( valName, 0, wx.ALL, 5 )

			#Make the unit dropdown list
			#unitName = 'self.unit_TI_'+ str(self.inputList[0][i])
			unit_Choices,defaultIndex = self.findUnits(self.inputList[0][i])
			valId += 2000
			unitName = wx.Choice( self, valId, wx.DefaultPosition, wx.DefaultSize, unit_Choices, 0 )
			unitName.SetSelection( defaultIndex )
			sz_TI_State1.Add( unitName, 0, wx.ALL, 5 )
			#self.nameList.append(valName)
			#print(valId)

		#print('\n',self.FindWindowById(999))

	def CreateState2(self,sz_TI_State2):
		"""
			This populates all of State 2 with the necissary variables.
			What is necissary was decided in the previous frame.
		"""
		print('Setting up State 2')
		for i in range(len(self.inputList[1])):
			#Make the text label
			#txtName = 'txt_TI_'+ str(self.inputList[1][i])
			self.txtName = wx.StaticText( self, wx.ID_ANY, self.inputList[1][i], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.txtName.Wrap( -1 )
			sz_TI_State2.Add( self.txtName, 0, wx.ALL, 5 )

			#Make the input box
			#valName = 'val_TI_'+ str(self.inputList[1][i])
			valId = 1000 + i
			self.valName = wx.TextCtrl( self, valId, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
			sz_TI_State2.Add( self.valName, 0, wx.ALL, 5 )

			#Make the unit dropdown list
			#unitName = 'self.unit_TI_'+ str(self.inputList[1][i])
			unit_Choices,defaultIndex = self.findUnits(self.inputList[1][i])
			valId += 2000
			unitName = wx.Choice( self, valId, wx.DefaultPosition, wx.DefaultSize, unit_Choices, 0 )
			unitName.SetSelection( defaultIndex )
			sz_TI_State2.Add( unitName, 0, wx.ALL, 5 )
			#self.nameList.append(valName)
			#print(valId)

	def CreateOther(self,sz_TI_Other):
		"""
			This populates all of Other with the necissary variables.
			What is necissary was decided in the previous frame.
		"""
		print('Setting up Other')
		for i in range(len(self.inputList[2])):
			#Make the text label
			#txtName = 'txt_TI_'+ str(self.inputList[2][i])
			self.txtName = wx.StaticText( self, wx.ID_ANY, self.inputList[2][i], wx.DefaultPosition, wx.DefaultSize, 0  )
			self.txtName.Wrap( -1 )
			sz_TI_Other.Add( self.txtName, 0, wx.ALL, 5 )

			#Make the input box
			#valName = 'val_TI_'+ str(self.inputList[2][i])
			valId = 1500 + i
			self.valName = wx.TextCtrl( self, valId, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
			sz_TI_Other.Add( self.valName, 0, wx.ALL, 5 )

			#Make the unit dropdown list
			#unitName = 'self.unit_TI_'+ str(self.inputList[2][i])
			unit_Choices,defaultIndex = self.findUnits(self.inputList[2][i])
			valId += 2000
			unitName = wx.Choice( self, valId, wx.DefaultPosition, wx.DefaultSize, unit_Choices, 0 )
			unitName.SetSelection( defaultIndex )
			sz_TI_Other.Add( unitName, 0, wx.ALL, 5 )
			#self.nameList.append(valName)
			#print(valId)

	def CreateEvents(self):
		x = 1
		print('Creating Events')
		#Add an event to that box
		#self.FindWindowById(999).Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_P1 )
		for i in range(len(self.inputList[0])):
			#print(500+i)
			eventName = 'onVal_TI_'+ str(self.inputList[0][i])
			self.FindWindowById(500+i).Bind( wx.EVT_TEXT, getattr(self,eventName))
			unitsName = 'onUnits_TI_'+ str(self.inputList[0][i])
			self.FindWindowById(2500+i).Bind( wx.EVT_CHOICE, getattr(self,unitsName))
		
		for i in range(len(self.inputList[1])):
			#print(1000+i)
			eventName = 'onVal_TI_'+ str(self.inputList[1][i])
			self.FindWindowById(1000+i).Bind( wx.EVT_TEXT, getattr(self,eventName))
			unitsName = 'onUnits_TI_'+ str(self.inputList[1][i])
			self.FindWindowById(3000+i).Bind( wx.EVT_CHOICE, getattr(self,unitsName))
		
		for i in range(len(self.inputList[2])):
			#print(1500+i)
			eventName = 'onVal_TI_'+ str(self.inputList[2][i])
			self.FindWindowById(1500+i).Bind( wx.EVT_TEXT, getattr(self,eventName))
			unitsName = 'onUnits_TI_'+ str(self.inputList[2][i])
			self.FindWindowById(3500+i).Bind( wx.EVT_CHOICE, getattr(self,unitsName))

	def findWhich(self,item):
		"""
			This finds which id corresponds to your variable.
			First, it finds where in the list your variable is located, and in which column.
			Then, it uses that knowledge to give you the correct id.
		"""
		#Find where the variable is in the list
		if item in np.array(self.inputList[0]).flatten().tolist():
			for i in range(len(self.inputList[0])):
				if item == self.inputList[0][i]: 
					answer = 500+i
					break

		elif item in np.array(self.inputList[1]).flatten().tolist():
			for i in range(len(self.inputList[1])):
				if item == self.inputList[1][i]: 
					answer = 1000+i
					break

		elif item in np.array(self.inputList[2]).flatten().tolist():
			for i in range(len(self.inputList[2])):
				if item == self.inputList[2][i]: 
					answer = 1500+i
					break
		#print(answer)
		return answer

	def findUnits(self,var):
		"""
			This finds the appropriate units to display for the given variable
		"""
		if var in 'a': #Acceleration Units
			if self.units == 0: unitList = ['m/s','cm/s']
			else: unitList = ['ft/s','in/s']
			defaultIndex = 0

		elif 'A' in var: #Area Units
			if self.units == 0: unitList = ['m2','cm2','mm2','km2']
			else: unitList = ['ft2','in2']
			defaultIndex = 0

		elif 'roe' in var: #Density Units
			if self.units == 0: unitList = ['kg/m3','g/cm3','kg/L']
			else: unitList = ['lbm/ft3','lbm/in3']
			defaultIndex = 0

		elif ('W' in var) or ('Q' in var) or ('u' in var) or ('h' in var): #Energy Units
			if self.units == 0: unitList = ['kJ','J','N*m','kWh','kPa*m3','kJ/kg','kJ/kmol','m2/s2','cal','Cal']
			else: unitList = ['Btu','MMBTU','psia*ft3','lbf*ft','Btu/lbm','ft2/s2','therm']
			if ('W' in var) or ('Q' in var): defaultIndex = 1
			if ('u' in var) or ('h' in var): defaultIndex = 5
#?
		elif 'F' in var: #Force Units
			if self.units == 0: unitList = ['N','kg*m/s2','dyne','kgf']
			else: unitList = ['lbf','lbm*ft/s2']
			defaultIndex = 0
#?
		elif 'HF' in var: #Heat Flux Units
			if self.units == 0: unitList = ['W/cm2','W/m2']
			else: unitList = ['Btu/h*ft2']
			defaultIndex = 0
#?
		elif 'HT' in var: #Heat Transfer Coefficient Units
			if self.units == 0: unitList = ['W/m2*C','W/m2*K']
			else: unitList = ['Btu/h*ft2*F','Btu/h*ft2*R']
			defaultIndex = 0
#?
		elif 'L' in var: #Length Units
			if self.units == 0: unitList = ['m','cm','mm','nm','km']
			else: unitList = ['ft','in','yd','mile']
			defaultIndex = 0

		elif 'm' in var: #Mass Units
			if self.units == 0: unitList = ['kg','g','metric_ton']
			else: unitList = ['lbm','oz','slug','short_ton']
			defaultIndex = 0
#?
		elif 'Pow' in var: #Power Units
			if self.units == 0: unitList = ['W','kW','J/s','hp']
			else: unitList = ['Btu/h','Btu/min','Btu/s','lbf*ft/s','hp','boiler_hp','ton_of_ref']
			defaultIndex = 0

		elif 'P' in var: #Pressure Units
			if self.units == 0: unitList = ['Pa','kPa','MPa','N/m2','atm','bars','mm_Hg','kgf/cm2']
			else: unitList = ['psi','psia','ksi','lbf/ft2','in Hg']
			defaultIndex = 1

		elif ('q' in var) or ('s' in var): #Specific Heat Units
			if self.units == 0: unitList = ['kJ/kmol*C','kJ/kmol*K','kJ/kg*C','kJ/kg*K','J/g*C','J/g*K']
			else: unitList = ['Btu/lbm*F','Btu/lbm*R','Btu/lbmol*F','Btu/lbmol*R']
			defaultIndex = 1

		elif ('v' in var) and ('_' not in var): #Specific Volume Units. The _ accounts for kenetic energy
			if self.units == 0: unitList = ['m3/kg','L/kg','cm3/g']
			else: unitList = ['ft3/lbm']
			defaultIndex = 0

		elif 'T' in var: #Temperature Units
			if self.units == 0: unitList = ['C','K']
			else: unitList = ['F','R']
			defaultIndex = 0
#?
		elif 'TC' in var: #Thermal Conductivity Units
			if self.units == 0: unitList = ['W/m*C','W/m*K']
			else: unitList = ['Btu/h*ft*F','Btu/h*ft*R']
			defaultIndex = 1

		elif '_v' in var: #Velocity Units
			if self.units == 0: unitList = ['m/s','km/h']
			else: unitList = ['ft/s','mi/h']
			defaultIndex = 0

		elif 'V' in var: #Volume Units
			if self.units == 0: unitList = ['L','m3','cm3','cc']
			else: unitList = ['in3','ft3','US_gal','fl_oz']
			defaultIndex = 0

		elif 'Vdot' in var: #Volume Flow Rate Units
			if self.units == 0: unitList = ['m3/s','cm3/s','L/min','L/s']
			else: unitList = ['ft3/s','ft3/min','gal/s','gal/min']
			defaultIndex = 0
		else: unitList, defaultIndex = ['unitless'], 0

		return unitList, defaultIndex

#The State 1 Variable Controllers
	def onVal_TI_P1( self, event ):
		#This will edit an internal variable whenever the text in the box is changed and enter is pressed.
		myId = self.findWhich('P1')
		self.P1 = self.FindWindowById(myId).GetLineText(0)
		#print('P1',self.P1)
		event.Skip()
	def onUnits_TI_P1( self, event ):
		myId = self.findWhich('P1') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UP1 = self.FindWindowById(myId).GetString(n)
		#print('P1 Units',self.UP1)
		#event.Skip()
	
	def onVal_TI_V1( self, event ):
		myId = self.findWhich('V1')
		self.V1 = self.FindWindowById(myId).GetLineText(0)
		#print('V1',self.V1)
		event.Skip()
	def onUnits_TI_V1( self, event ):
		myId = self.findWhich('V1') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UV1 = self.FindWindowById(myId).GetString(n)
		#print('V1 Units',self.UV1)
		#event.Skip()

	def onVal_TI_v1( self, event ):
		myId = self.findWhich('v1')
		self.v1 = self.FindWindowById(myId).GetLineText(0)
		#print('v1',self.v1)
		event.Skip()
	def onUnits_TI_v1( self, event ):
		myId = self.findWhich('v1') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uv1 = self.FindWindowById(myId).GetString(n)
		#print('v1 Units',self.Uv1)
		#event.Skip()

	def onVal_TI_T1( self, event ):
		myId = self.findWhich('T1')
		self.T1 = self.FindWindowById(myId).GetLineText(0)
		#print('T1',self.T1)
		event.Skip()
	def onUnits_TI_T1( self, event ):
		myId = self.findWhich('T1') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UT1 = self.FindWindowById(myId).GetString(n)
		#print('T1 Units',self.UT1)
		#event.Skip()

	def onVal_TI_u1( self, event ):
		myId = self.findWhich('u1')
		self.u1 = self.FindWindowById(myId).GetLineText(0)
		#print('u1',self.u1)
		event.Skip()
	def onUnits_TI_u1( self, event ):
		myId = self.findWhich('u1') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uu1 = self.FindWindowById(myId).GetString(n)
		#print('u1 Units',self.Uu1)
		#event.Skip()

	def onVal_TI_hi( self, event ):
		myId = self.findWhich('hi')
		self.hi = self.FindWindowById(myId).GetLineText(0)
		#print('hi',self.hi)
		event.Skip()
	def onUnits_TI_hi( self, event ):
		myId = self.findWhich('hi') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uhi = self.FindWindowById(myId).GetSelection(n)
		#print(' Units',self.Uhi)
		#event.Skip()

	def onVal_TI_s1( self, event ):
		myId = self.findWhich('s1')
		self.s1 = self.FindWindowById(myId).GetLineText(0)
		#print('s1',self.s1)
		event.Skip()
	def onUnits_TI_s1( self, event ):
		myId = self.findWhich('s1') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Us1 = self.FindWindowById(myId).GetString(n)
		#print('s1 Units',self.Us1)
		#event.Skip()

	def onVal_TI_si( self, event ):
		myId = self.findWhich('si')
		self.si = self.FindWindowById(myId).GetLineText(0)
		#print('si',self.si)
		event.Skip()
	def onUnits_TI_si( self, event ):
		myId = self.findWhich('si') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Usi = self.FindWindowById(myId).GetString(n)
		#print('si Units',self.Usi)
		#event.Skip()

	def onVal_TI_x1( self, event ):
		myId = self.findWhich('x1')
		self.x1 = self.FindWindowById(myId).GetLineText(0)
		#print('x1',self.x1)
		event.Skip()
	def onUnits_TI_x1( self, event ):
		myId = self.findWhich('x1') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Ux1 = self.FindWindowById(myId).GetString(n)
		#print('x1 Units',self.Ux1)
		#event.Skip()

	def onVal_TI_m1( self, event ):
		myId = self.findWhich('m1')
		self.m1 = self.FindWindowById(myId).GetLineText(0)
		#print('m1',self.m1)
		event.Skip()
	def onUnits_TI_m1( self, event ):
		myId = self.findWhich('m1') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Um1 = self.FindWindowById(myId).GetString(n)
		#print('m1 Units',self.Um1)
		#event.Skip()

	def onVal_TI_mi( self, event ):
		myId = self.findWhich('mi')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		#print('mi',self.mi)
		event.Skip()
	def onUnits_TI_mi( self, event ):
		myId = self.findWhich('mi') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Umi = self.FindWindowById(myId).GetString(n)
		#print('mi Units',self.Umi)
		#event.Skip()

	def onVal_TI_pi_h( self, event ):
		myId = self.findWhich('pi_h')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		#print('pi_h',self.mi)
		event.Skip()
	def onUnits_TI_pi_h( self, event ):
		myId = self.findWhich('pi_h') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Upi_h = self.FindWindowById(myId).GetString(n)
		#print('pi_h Units',self.Upi_h)
		#event.Skip()

	def onVal_TI_p1_h( self, event ):
		myId = self.findWhich('p1_h')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		#print('p1_h',self.mi)
		event.Skip()
	def onUnits_TI_p1_h( self, event ):
		myId = self.findWhich('p1_h') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Up1_h = self.FindWindowById(myId).GetString(n)
		#print('p1_h Units',self.Up1_h)
		#event.Skip()

	def onVal_TI_ki_v( self, event ):
		myId = self.findWhich('ki_v')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		#print('ki_v',self.mi)
		event.Skip()
	def onUnits_TI_ki_v( self, event ):
		myId = self.findWhich('ki_v') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uki_v = self.FindWindowById(myId).GetString(n)
		#print('ki_v Units',self.Uki_v)
		#event.Skip()

	def onVal_TI_k1_v( self, event ):
		myId = self.findWhich('k1_v')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		#print('k1_v',self.mi)
		event.Skip()
	def onUnits_TI_k1_v( self, event ):
		myId = self.findWhich('k1_v') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uk1_v = self.FindWindowById(myId).GetString(n)
		#print('k1_v Units',self.Uk1_v)
		#event.Skip()

#The State 2 Variable Conrollers
	def onVal_TI_P2( self, event ):
		myId = self.findWhich('P2')
		self.P2 = self.FindWindowById(myId).GetLineText(0)
		#print('P2',self.P2)
		event.Skip()
	def onUnits_TI_P2( self, event ):
		myId = self.findWhich('P2') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UP2 = self.FindWindowById(myId).GetString(n)
		#print('P2 Units',self.UP2)
		#event.Skip()
	
	def onVal_TI_V2( self, event ):
		myId = self.findWhich('V2')
		self.V2 = self.FindWindowById(myId).GetLineText(0)
		#print('V2',self.V2)
		event.Skip()
	def onUnits_TI_V2( self, event ):
		myId = self.findWhich('V2') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UV2 = self.FindWindowById(myId).GetString(n)
		#print('V2 Units',self.UV2)
		#event.Skip()

	def onVal_TI_v2( self, event ):
		myId = self.findWhich('v2')
		self.v2 = self.FindWindowById(myId).GetLineText(0)
		#print('v2',self.v2)
		event.Skip()
	def onUnits_TI_v2( self, event ):
		myId = self.findWhich('v2') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uv2 = self.FindWindowById(myId).GetString(n)
		#print('v2 Units',self.Uv2)
		#event.Skip()

	def onVal_TI_T2( self, event ):
		myId = self.findWhich('T2')
		self.T2  = self.FindWindowById(myId).GetLineText(0)
		#print('T2',self.T2)
		event.Skip()
	def onUnits_TI_T2( self, event ):
		myId = self.findWhich('T2') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UT2 = self.FindWindowById(myId).GetString(n)
		#print('T2 Units',self.UT2)
		#event.Skip()

	def onVal_TI_u2( self, event ):
		myId = self.findWhich('u2')
		self.u2 = self.FindWindowById(myId).GetLineText(0)
		#print('u2',self.u2)
		event.Skip()
	def onUnits_TI_u2( self, event ):
		myId = self.findWhich('u2') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uu2 = self.FindWindowById(myId).GetString(n)
		#print('u2 Units',self.Uu2)
		#event.Skip()

	def onVal_TI_he( self, event ):
		myId = self.findWhich('he')
		self.he = self.FindWindowById(myId).GetLineText(0)
		#print('he',self.he)
		event.Skip()
	def onUnits_TI_he( self, event ):
		myId = self.findWhich('he') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uhe = self.FindWindowById(myId).GetString(n)
		#print('he Units',self.Uhe)
		#event.Skip()

	def onVal_TI_s2( self, event ):
		myId = self.findWhich('s2')
		self.s2 = self.FindWindowById(myId).GetLineText(0)
		#print('s2',self.s2)
		event.Skip()
	def onUnits_TI_s2( self, event ):
		myId = self.findWhich('s2') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Us2 = self.FindWindowById(myId).GetString(n)
		#print('s2 Units',self.Us2)
		#event.Skip()

	def onVal_TI_se( self, event ):
		myId = self.findWhich('se')
		self.se = self.FindWindowById(myId).GetLineText(0)
		#print('se',self.se)
		event.Skip()
	def onUnits_TI_se( self, event ):
		myId = self.findWhich('se') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Use = self.FindWindowById(myId).GetString(n)
		#print('se Units',self.Use)
		#event.Skip()

	def onVal_TI_x2( self, event ):
		myId = self.findWhich('x2')
		self.x2 = self.FindWindowById(myId).GetLineText(0)
		#print('x2',self.x2)
		event.Skip()
	def onUnits_TI_x2( self, event ):
		myId = self.findWhich('x2') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Ux2 = self.FindWindowById(myId).GetString(n)
		#print('x2 Units',self.Ux2)
		#event.Skip()

	def onVal_TI_m2( self, event ):
		myId = self.findWhich('m2')
		self.m2 = self.FindWindowById(myId).GetLineText(0)
		#print('m2',self.m2)
		event.Skip()
	def onUnits_TI_m2( self, event ):
		myId = self.findWhich('m2') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Um2 = self.FindWindowById(myId).GetString(n)
		#print('m2 Units',self.Um2)
		#event.Skip()

	def onVal_TI_me( self, event ):
		myId = self.findWhich('me')
		self.me = self.FindWindowById(myId).GetLineText(0)
		#print('me',self.me)
		event.Skip()
	def onUnits_TI_me( self, event ):
		myId = self.findWhich('me') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Ume = self.FindWindowById(myId).GetString(n)
		#print('me Units',self.Ume)
		#event.Skip()

	def onVal_TI_pe_h( self, event ):
		myId = self.findWhich('pe_h')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		#print('pe_h',self.mi)
		event.Skip()
	def onUnits_TI_pe_h( self, event ):
		myId = self.findWhich('pe_h') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Upe_h = self.FindWindowById(myId).GetString(n)
		#print('pe_h Units',self.Upe_h)
		#event.Skip()

	def onVal_TI_p2_h( self, event ):
		myId = self.findWhich('p2_h')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		#print('p2_h',self.mi)
		event.Skip()
	def onUnits_TI_p2_h( self, event ):
		myId = self.findWhich('p2_h') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Up2_h = self.FindWindowById(myId).GetString(n)
		#print('p2_h Units',self.Up2_h)
		#event.Skip()

	def onVal_TI_ke_v( self, event ):
		myId = self.findWhich('ke_v')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		#print('ke_v',self.mi)
		event.Skip()
	def onUnits_TI_ke_v( self, event ):
		myId = self.findWhich('ke_v') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uke_v = self.FindWindowById(myId).GetString(n)
		#print('ke_v Units',self.Uke_v)
		#event.Skip()

	def onVal_TI_k2_v( self, event ):
		myId = self.findWhich('k2_v')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		#print('k2_v',self.mi)
		event.Skip()
	def onUnits_TI_k2_v( self, event ):
		myId = self.findWhich('k2_v') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uk2_v = self.FindWindowById(myId).GetString()
		#print('k2_v Units',self.Uk2_v)
		#event.Skip()

#The Other Variable Controllers
	def onVal_TI_W( self, event ):
		myId = self.findWhich('W')
		self.W = self.FindWindowById(myId).GetLineText(0)
		#print('W',self.W)
		event.Skip()
	def onUnits_TI_W( self, event ):
		myId = self.findWhich('W') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UW = self.FindWindowById(myId).GetString(n)
		#print('W Units',self.UW)
		#event.Skip()
	
	def onVal_TI_Q( self, event ):
		myId = self.findWhich('Q')
		self.Q = self.FindWindowById(myId).GetLineText(0)
		#print('Q',self.Q)
		event.Skip()
	def onUnits_TI_Q( self, event ):
		myId = self.findWhich('Q') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UQ = self.FindWindowById(myId).GetString(n)
		#print('Q Units',self.UQ)
		#event.Skip()

	def onVal_TI_k( self, event ):
		myId = self.findWhich('k')
		self.k = self.FindWindowById(myId).GetLineText(0)
		#print('k',self.k)
		event.Skip()
	def onUnits_TI_k( self, event ):
		myId = self.findWhich('k') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uk = self.FindWindowById(myId).GetString(n)
		#print('k Units',self.Uk)
		#event.Skip()

	def onVal_TI_Cp( self, event ):
		myId = self.findWhich('Cp')
		self.Cp = self.FindWindowById(myId).GetLineText(0)
		#print('Cp',self.Cp)
		event.Skip()
	def onUnits_TI_Cp( self, event ):
		myId = self.findWhich('Cp') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UCp = self.FindWindowById(myId).GetString(n)
		#print('Cp Units',self.UCp)
		#event.Skip()

	def onVal_TI_Cv( self, event ):
		myId = self.findWhich('Cv')
		self.Cv = self.FindWindowById(myId).GetLineText(0)
		#print('Cv',self.Cv)
		event.Skip()
	def onUnits_TI_Cv( self, event ):
		myId = self.findWhich('Cv') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UCv = self.FindWindowById(myId).GetString(n)
		#print('Cv Units',self.UCv)
		#event.Skip()

	def onVal_TI_Cavg( self, event ):
		myId = self.findWhich('Cavg')
		self.Cv = self.FindWindowById(myId).GetLineText(0)
		#print('Cavg',self.Cv)
		event.Skip()
	def onUnits_TI_Cavg( self, event ):
		myId = self.findWhich('Cavg') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UCavg = self.FindWindowById(myId).GetString(n)
		#print('Cavg Units',self.UCavg)
		#event.Skip()

	def onVal_TI_roe( self, event ):
		myId = self.findWhich('roe')
		self.roe = self.FindWindowById(myId).GetLineText(0)
		#print('roe',self.roe)
		event.Skip()
	def onUnits_TI_roe( self, event ):
		myId = self.findWhich('roe') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.Uroe = self.FindWindowById(myId).GetString(n)
		#print('roe Units',self.Uroe)
		#event.Skip()

	def onVal_TI_R( self, event ):
		myId = self.findWhich('R')
		self.R = self.FindWindowById(myId).GetLineText(0)
		#print('R',self.R)
		event.Skip()
	def onUnits_TI_R( self, event ):
		myId = self.findWhich('R') + 2000
		n = self.FindWindowById(myId).GetSelection()
		self.UR = self.FindWindowById(myId).GetString(n)
		#print('R Units',self.UR)
		#event.Skip()

#The button at the end controller
	def onBtnClick_ContinueToResults( self, event ):
		"""
		The args are split up for ease of reading it and ease of changing it.
		args = [[goal]]
		kwargs is a dictionary of values and units.
		"""
		#print('continue')
		kwargs = {}
		#print(self.inputList)
		for j in range(len(self.inputList)):
			for i in range(len(self.inputList[j])):	#This will generate the kwargs to have just the values shown on the input screen.
				kwargs.update({self.inputList[j][i]:getattr(self,self.inputList[j][i])})
#		kwargs = {'P1':self.P1,'V1':self.V1,'v1':self.v1,'T1':self.T1,'u1':self.u1,'hi':self.hi,'si':self.si,'s1':self.s1,'x1':self.x1,'m1':self.m1,'mi':self.mi,'p1_h':self.p1_h,'pi_h':self.pi_h,'k1_v':self.k1_v,'ki_v':self.ki_v}
#		kwargs.update({'P2':self.P2,'V2':self.V2,'v2':self.v2,'T2':self.T2,'u2':self.u2,'he':self.he,'se':self.se,'s2':self.s2,'x2':self.x2,'m2':self.m2,'m2':self.me,'p2_h':self.p2_h,'pe_h':self.pe_h,'k2_v':self.k2_v,'ke_v':self.ke_v})
#		kwargs.update({'W':self.W,'Q':self.Q,'k':self.k,'Cp':self.Cp,'Cv':self.Cv,'roe':self.roe,'R':self.R})
	
#		kwargs.update({'UP1':self.P1,'UV1':self.V1,'Uv1':self.v1,'UT1':self.T1,'Uu1':self.u1,'Uhi':self.hi,'Usi':self.si,'Us1':self.s1,'Ux1':self.x1,'Um1':self.m1,'Umi':self.mi,'Up1_h':self.p1_h,'Upi_h':self.pi_h,'Uk1_v':self.k1_v,'Uki_v':self.ki_v})
#		kwargs.update({'UP2':self.P2,'UV2':self.V2,'Uv2':self.v2,'UT2':self.T2,'Uu2':self.u2,'Uhe':self.he,'Use':self.se,'Us2':self.s2,'Ux2':self.x2,'Um2':self.m2,'Um2':self.me,'Up2_h':self.p2_h,'Upe_h':self.pe_h,'Uk2_v':self.k2_v,'Uke_v':self.ke_v})
#		kwargs.update({'UW':self.W,'UQ':self.Q,'Uk':self.k,'UCp':self.Cp,'UCv':self.Cv,'Uroe':self.roe,'UR':self.R})

		args = [['thermo'],{}]
		#Create a dictionary of the goals
		#print(kwargs.items())
		for eqn in kwargs.items():
			if '@' in eqn:
				if eqn[0][0] != 'U':  #Weeds out the unit turples that get added for some reason.
					args[1].update({eqn[0]:'unknown'})

		LogicCalculator.__init__(self,*args,**kwargs)
		#after the calculator runs, show the next frame and destroy this one.
		#self.destroy()
		event.Skip()

if __name__ == '__main__':
	app = wx.App()
	frame = LogicThermoInput(None)
	frame.Show()
	app.MainLoop()