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
		x = 510
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
			valName = wx.TextCtrl( self, id = valId, value = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0  )
			sz_TI_State1.Add( valName, 0, wx.ALL, 5 )

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
			self.valName = wx.TextCtrl( self, id = valId, value = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )
			sz_TI_State2.Add( self.valName, 0, wx.ALL, 5 )

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
			self.valName = wx.TextCtrl( self, id = valId, value = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )
			sz_TI_Other.Add( self.valName, 0, wx.ALL, 5 )

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