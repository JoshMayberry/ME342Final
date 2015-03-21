import wx
from ..views import Frm_ThermoInput #Needed to communicate with the frame
from .logicThermoCalculator import LogicThermoCalculator #Needed to do the calculations before showing the next screen.
import numpy as np

class LogicThermoInput(Frm_ThermoInput):
	def __init__(self, parent,*args):
		#Set variables
		self.inputList = args #This is a list used to generate the text boxes
		#self.nameList = [] #This is a list of the generated text boxes so events can be created for them.
		#Build GUI
		print ("Building ", self.__class__)
		Frm_ThermoInput.__init__(self, parent)

	def setSize(self):
		"""
			This dynamically sets the window size according to how many inputs the longets list has.
		"""
		lengthList = [len(self.inputList[0]),len(self.inputList[1]),len(self.inputList[2])]
		Lmax = np.array(lengthList).argmax()
		n = lengthList[Lmax] #The length of the longest column
		x = 850
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
			txtName = 'txt_TI_'+ str(self.inputList[0][i])
			self.txtName = wx.StaticText( self, wx.ID_ANY, self.inputList[0][i], wx.DefaultPosition, wx.DefaultSize, 0  )
			self.txtName.Wrap( -1 )
			sz_TI_State1.Add( self.txtName, 0, wx.ALL, 5 )

			#Make the input box
			valName = 'self.val_TI_'+ str(self.inputList[0][i])
			valId = 500 + i #This is so I can find it later
			valName = wx.TextCtrl( self, valId, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0  )
			sz_TI_State1.Add( valName, 0, wx.ALL, 5 )

			#Make the unit dropdown list
			unitName = 'self.unit_TI_'+ str(self.inputList[0][i])
			unit_Choices = self.findUnits(self.inputList[0][i])
			unitName = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, unit_Choices, 0 )
			unitName.SetSelection( 0 )
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
			txtName = 'txt_TI_'+ str(self.inputList[1][i])
			self.txtName = wx.StaticText( self, wx.ID_ANY, self.inputList[1][i], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.txtName.Wrap( -1 )
			sz_TI_State2.Add( self.txtName, 0, wx.ALL, 5 )

			#Make the input box
			valName = 'val_TI_'+ str(self.inputList[1][i])
			valId = 1000 + i
			self.valName = wx.TextCtrl( self, valId, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			sz_TI_State2.Add( self.valName, 0, wx.ALL, 5 )

			#Make the unit dropdown list
			unitName = 'self.unit_TI_'+ str(self.inputList[1][i])
			unit_Choices = self.findUnits(self.inputList[1][i])
			unitName = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, unit_Choices, 0 )
			unitName.SetSelection( 0 )
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
			txtName = 'txt_TI_'+ str(self.inputList[2][i])
			self.txtName = wx.StaticText( self, wx.ID_ANY, self.inputList[2][i], wx.DefaultPosition, wx.DefaultSize, 0  )
			self.txtName.Wrap( -1 )
			sz_TI_Other.Add( self.txtName, 0, wx.ALL, 5 )

			#Make the input box
			valName = 'val_TI_'+ str(self.inputList[2][i])
			valId = 1500 + i
			self.valName = wx.TextCtrl( self, valId, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
			sz_TI_Other.Add( self.valName, 0, wx.ALL, 5 )

			#Make the unit dropdown list
			unitName = 'self.unit_TI_'+ str(self.inputList[2][i])
			unit_Choices = self.findUnits(self.inputList[2][i])
			unitName = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, unit_Choices, 0 )
			unitName.SetSelection( 0 )
			sz_TI_Other.Add( unitName, 0, wx.ALL, 5 )
			#self.nameList.append(valName)
			#print(valId)

	def CreateEvents(self):
		x = 1
		print('\n','hi')
		#Add an event to that box
		#self.FindWindowById(999).Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_P1 )
		for i in range(len(self.inputList[0])):
			#print(500+i)
			eventName = 'onVal_TI_'+ str(self.inputList[0][i])
			self.FindWindowById(500+i).Bind( wx.EVT_TEXT_ENTER, getattr(self,eventName))
		for i in range(len(self.inputList[1])):
			#print(1000+i)
			eventName = 'onVal_TI_'+ str(self.inputList[1][i])
			self.FindWindowById(1000+i).Bind( wx.EVT_TEXT_ENTER, getattr(self,eventName))
		for i in range(len(self.inputList[2])):
			#print(1500+i)
			eventName = 'onVal_TI_'+ str(self.inputList[2][i])
			self.FindWindowById(1500+i).Bind( wx.EVT_TEXT_ENTER, getattr(self,eventName))

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

		return answer

	def findUnits(self,var):
		"""
			This finds the appropriate units to display for the given variable
		"""
		if var in 'a':
			#Acceleration Units (Metric)
			unitList = ['m/s','cm/s']

			#Acceleration Units (English)
			unitList = ['ft/s','in/s']

		elif 'A' in var:
			#Area Units (Metric)
			unitList = ['m2','cm2','mm2','km2']

			#Area Units (English)
			unitList = ['ft2','in2']

		elif 'roe' in var:
			#Density Units (Metric)
			unitList = ['kg/m3','g/cm3','kg/L']

			#Density Units (English)
			unitList = ['lbm/ft3','lbm/in3']

		elif ('W' in var) or ('Q' in var) or ('u' in var) or ('h' in var):
			#Energy Units (Metric)
			unitList = ['kJ','J','N*m','kWh','kPa*m3','kJ/kg','kJ/kmol','m2/s2','cal','Cal']

			#Energy Units (English)
			unitList = ['Btu','MMBTU','psia*ft3','lbf*ft','Btu/lbm','ft2/s2','therm']
#?
		elif 'F' in var:
			#Force Units (Metric)
			unitList = ['N','kg*m/s2','dyne','kgf']

			#Force Units (English)
			unitList = ['lbf','lbm*ft/s2']
#?
		elif 'HF' in var:
			#Heat Flux Units (Metric)
			unitList = ['W/cm2','W/m2']

			#Heat Flux Units (English)
			unitList = ['Btu/h*ft2']
#?
		elif 'HT' in var:
			#Heat Transfer Coefficient Units (Metric)
			unitList = ['W/m2*C','W/m2*K']

			#Heat Transfer Coefficient Units (English)
			unitList = ['Btu/h*ft2*F','Btu/h*ft2*R']
#?
		elif 'L' in var:
			#Length Units (Metric)
			unitList = ['m','cm','mm','nm','km']

			#Length Units (English)
			unitList = ['ft','in','yd','mile']

		elif 'm' in var:
			#Mass Units (Metric)
			unitList = ['kg','g','metric_ton']

			#Mass Units (English)
			unitList = ['lbm','oz','slug','short_ton']
#?
		elif 'Pow' in var:
			#Power Units (Metric)
			unitList = ['W','kW','J/s','hp']

			#Power Units (English)
			unitList = ['Btu/h','Btu/min','Btu/s','lbf*ft/s','hp','boiler_hp','ton_of_ref']

		elif 'P' in var:
			#Pressure Units (Metric)
			unitList = ['Pa','kPa','MPa','N/m2','atm','bars','mm_Hg','kgf/cm2']

			#Pressure Units (Englsih)
			unitList = ['psi','psia','ksi','lbf/ft2','in Hg']

		elif ('q' in var) or ('s' in var):
			#Specific Heat Units (Metric)
			unitList = ['kJ/kmol*C','kJ/kmol*K','kJ/kg*C','kJ/kg*K','J/g*C','J/g*K']

			#Specific Heat Units (English)
			unitList = ['Btu/lbm*F','Btu/lbm*R','Btu/lbmol*F','Btu/lbmol*R']

		elif ('v' in var) and ('_' not in var): #The _ accounts for kenetic energy
			#Specific Volume Units (Metric)
			unitList = ['m3/kg','L/kg','cm3/g']

			#Specific Volume Units (English)
			unitList = ['ft3/lbm']

		elif 'T' in var:
			#Temperature Units (Metric)
			unitList = ['C','K']

			#Temperature Units (English)
			unitList = ['F','R']
#?
		elif 'TC' in var:
			#Thermal Conductivity Units (Metric)
			unitList = ['W/m*C','W/m*K']

			#Thermal Conductivity Units (English)
			unitList = ['Btu/h*ft*F','Btu/h*ft*R']

		elif '_v' in var:
			#Velocity Units (Metric)
			unitList = ['m/s','km/h']

			#Velocity Units (English)
			unitList = ['ft/s','mi/h']

		elif 'V' in var:
			#Volume Units (Metric)
			unitList = ['L','m3','cm3','cc']

			#Volume Units (English)
			unitList = ['in3','ft3','US_gal','fl_oz']

		elif 'Vdot' in var:
			#Volume Flow Rate Units (Metric)
			unitList = ['m3/s','cm3/s','L/min','L/s']

			#Volume Flow Rate Units (English)
			unitList = ['gal/s','gal/min','ft3/s','ft3/min']
		else:
			unitList = ['unitless']

		return unitList

#The State 1 Variable Controllers
	def onVal_TI_P1( self, event ):
		#This will edit an internal variable whenever the text in the box is changed and enter is pressed.
		myId = self.findWhich('P1')
		self.P1 = self.FindWindowById(myId).GetLineText(0)
		print('P1',self.P1)
		event.Skip()
	
	def onVal_TI_V1( self, event ):
		myId = self.findWhich('V1')
		self.V1 = self.FindWindowById(myId).GetLineText(0)
		print('V1',self.V1)
		event.Skip()

	def onVal_TI_v1( self, event ):
		myId = self.findWhich('v1')
		self.v1 = self.FindWindowById(myId).GetLineText(0)
		print('v1',self.v1)
		event.Skip()

	def onVal_TI_T1( self, event ):
		myId = self.findWhich('T1')
		self.T1 = self.FindWindowById(myId).GetLineText(0)
		print('T1',self.T1)
		event.Skip()

	def onVal_TI_u1( self, event ):
		myId = self.findWhich('u1')
		self.u1 = self.FindWindowById(myId).GetLineText(0)
		print('u1',self.u1)
		event.Skip()

	def onVal_TI_hi( self, event ):
		myId = self.findWhich('hi')
		self.hi = self.FindWindowById(myId).GetLineText(0)
		print('hi',self.hi)
		event.Skip()

	def onVal_TI_s1( self, event ):
		myId = self.findWhich('s1')
		self.s1 = self.FindWindowById(myId).GetLineText(0)
		print('s1',self.s1)
		event.Skip()

	def onVal_TI_si( self, event ):
		myId = self.findWhich('si')
		self.si = self.FindWindowById(myId).GetLineText(0)
		print('si',self.si)
		event.Skip()

	def onVal_TI_x1( self, event ):
		myId = self.findWhich('x1')
		self.x1 = self.FindWindowById(myId).GetLineText(0)
		print('x1',self.x1)
		event.Skip()

	def onVal_TI_m1( self, event ):
		myId = self.findWhich('m1')
		self.m1 = self.FindWindowById(myId).GetLineText(0)
		print('m1',self.m1)
		event.Skip()

	def onVal_TI_mi( self, event ):
		myId = self.findWhich('mi')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		print('mi',self.mi)
		event.Skip()

	def onVal_TI_pi_h( self, event ):
		myId = self.findWhich('pi_h')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		print('pi_h',self.mi)
		event.Skip()

	def onVal_TI_p1_h( self, event ):
		myId = self.findWhich('p1_h')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		print('p1_h',self.mi)
		event.Skip()

	def onVal_TI_ki_v( self, event ):
		myId = self.findWhich('ki_v')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		print('ki_v',self.mi)
		event.Skip()

	def onVal_TI_k1_v( self, event ):
		myId = self.findWhich('k1_v')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		print('k1_v',self.mi)
		event.Skip()

#The State 2 Variable Conrollers
	def onVal_TI_P2( self, event ):
		myId = self.findWhich('P2')
		self.P2 = self.FindWindowById(myId).GetLineText(0)
		print('P2',self.P2)
		event.Skip()
	
	def onVal_TI_V2( self, event ):
		myId = self.findWhich('V2')
		self.V2 = self.FindWindowById(myId).GetLineText(0)
		print('V2',self.V2)
		event.Skip()

	def onVal_TI_v2( self, event ):
		myId = self.findWhich('v2')
		self.v2 = self.FindWindowById(myId).GetLineText(0)
		print('v2',self.v2)
		event.Skip()

	def onVal_TI_T2( self, event ):
		myId = self.findWhich('T2')
		self.T2  = self.FindWindowById(myId).GetLineText(0)
		print('T2',self.T2)
		event.Skip()

	def onVal_TI_u2( self, event ):
		myId = self.findWhich('u2')
		self.u2 = self.FindWindowById(myId).GetLineText(0)
		print('u2',self.u2)
		event.Skip()

	def onVal_TI_he( self, event ):
		myId = self.findWhich('he')
		self.he = self.FindWindowById(myId).GetLineText(0)
		print('he',self.he)
		event.Skip()

	def onVal_TI_s2( self, event ):
		myId = self.findWhich('s2')
		self.s2 = self.FindWindowById(myId).GetLineText(0)
		print('s2',self.s2)
		event.Skip()

	def onVal_TI_se( self, event ):
		myId = self.findWhich('se')
		self.se = self.FindWindowById(myId).GetLineText(0)
		print('se',self.se)
		event.Skip()

	def onVal_TI_x2( self, event ):
		myId = self.findWhich('x2')
		self.x2 = self.FindWindowById(myId).GetLineText(0)
		print('x2',self.x2)
		event.Skip()

	def onVal_TI_m2( self, event ):
		myId = self.findWhich('m2')
		self.m2 = self.FindWindowById(myId).GetLineText(0)
		print('m2',self.m2)
		event.Skip()

	def onVal_TI_me( self, event ):
		myId = self.findWhich('me')
		self.me = self.FindWindowById(myId).GetLineText(0)
		print('me',self.me)
		event.Skip()

	def onVal_TI_pe_h( self, event ):
		myId = self.findWhich('pe_h')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		print('pe_h',self.mi)
		event.Skip()

	def onVal_TI_p2_h( self, event ):
		myId = self.findWhich('p2_h')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		print('p2_h',self.mi)
		event.Skip()

	def onVal_TI_ke_v( self, event ):
		myId = self.findWhich('ke_v')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		print('ke_v',self.mi)
		event.Skip()

	def onVal_TI_k2_v( self, event ):
		myId = self.findWhich('k2_v')
		self.mi = self.FindWindowById(myId).GetLineText(0)
		print('k2_v',self.mi)
		event.Skip()

#The Other Variable Controllers
	def onVal_TI_W( self, event ):
		myId = self.findWhich('W')
		self.W = self.FindWindowById(myId).GetLineText(0)
		print('W',self.W)
		event.Skip()
	
	def onVal_TI_Q( self, event ):
		myId = self.findWhich('Q')
		self.Q = self.FindWindowById(myId).GetLineText(0)
		print('Q',self.Q)
		event.Skip()

	def onVal_TI_k( self, event ):
		myId = self.findWhich('k')
		self.k = self.FindWindowById(myId).GetLineText(0)
		print('k',self.k)
		event.Skip()

	def onVal_TI_Cp( self, event ):
		myId = self.findWhich('Cp')
		self.Cp = self.FindWindowById(myId).GetLineText(0)
		print('Cp',self.Cp)
		event.Skip()

	def onVal_TI_Cv( self, event ):
		myId = self.findWhich('Cv')
		self.Cv = self.FindWindowById(myId).GetLineText(0)
		print('Cv',self.Cv)
		event.Skip()

	def onVal_TI_Cavg( self, event ):
		myId = self.findWhich('Cavg')
		self.Cv = self.FindWindowById(myId).GetLineText(0)
		print('Cavg',self.Cv)
		event.Skip()

	def onVal_TI_roe( self, event ):
		myId = self.findWhich('roe')
		self.roe = self.FindWindowById(myId).GetLineText(0)
		print('roe',self.roe)
		event.Skip()

	def onVal_TI_R( self, event ):
		myId = self.findWhich('R')
		self.R = self.FindWindowById(myId).GetLineText(0)
		print('R',self.R)
		event.Skip()

#The button at the end controller
	def onBtnClick_ContinueToResults( self, event ):
		print('continue')
		#The args are split up for ease of reading it and ease of changing it.
		args = [self.P1,self.V1,self.v1,self.T1,self.u1,self.hi,self.si,self.s1,self.x1,self.m1,self.mi]
		args.extend([self.P2,self.V2,self.v2,self.T2,self.u2,self.he,self.se,self.s2,self.x2,self.m2,self.me])
		args.extend([self.W,self.Q,self.k,self.Cp,self.Cv,self.roe,self.R])
		LogicThermoEquations(self.parent,*args).Show()
		#after the calculator runs, show the next frame and destroy this one.
		event.Skip()

if __name__ == '__main__':
	app = wx.App()
	frame = LogicThermoInput(None)
	frame.Show()
	app.MainLoop()