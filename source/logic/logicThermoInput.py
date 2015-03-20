import wx
from ..views import Frm_ThermoInput #Needed to communicate with the frame
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
			txtName = 'txt_TI_'+ str(self.inputList[0][i])
			self.txtName = wx.StaticText( self, wx.ID_ANY, self.inputList[0][i], wx.DefaultPosition, wx.DefaultSize, 0  )
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
		print('\n')
		#Add an event to that box
		#self.FindWindowById(999).Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_P1 )
		for i in range(len(self.inputList[0])):
			#print(500+i)
			self.eventName = 'onVal_TI_'+ str(self.inputList[0][i])
			self.FindWindowById(500+i).Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_P1)#self.eventName )
		for i in range(len(self.inputList[1])):
			#print(1000+i)
			self.eventName = 'onVal_TI_'+ str(self.inputList[1][i])
			self.FindWindowById(1000+i).Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_P1)#self.eventName )
		for i in range(len(self.inputList[2])):
			#print(1500+i)
			self.eventName = 'onVal_TI_'+ str(self.inputList[2][i])
			self.FindWindowById(1500+i).Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_P1)#self.eventName )

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

	def onVal_TI_P1( self, event ):
		#This will edit an internal variable whenever the text in the box is changed and enter is pressed.
		myId = self.findWhich('P2')
		print(self.FindWindowById(myId).GetLineText(0)) #This is to test if it works
		event.Skip()
	
	def onVal_TI_V1( self, event ):
		event.Skip()
	
	def onVal_TI_P2( self, event ):
		event.Skip()
	
	def onVal_TI_V2( self, event ):
		event.Skip()
	
	def onVal_TI_W( self, event ):
		event.Skip()
	
	def onVal_TI_Q( self, event ):
		event.Skip()

	def onBtnClick_ContinueToResults( self, event ):
		event.Skip()

if __name__ == '__main__':
	app = wx.App()
	frame = LogicThermoInput(None)
	frame.Show()
	app.MainLoop()