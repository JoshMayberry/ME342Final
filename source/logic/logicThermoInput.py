import wx
from ..views import Frm_ThermoInput #Needed to communicate with the frame

class LogicThermoInput(Frm_ThermoInput):
	def __init__(self, parent,*args):
		#Set variables
		self.inputList = args #This is a list used to generate the text boxes
		self.nameList = [] #This is a list of the generated text boxes so events can be created for them.
		#Build GUI
		print ("Building ", self.__class__)
		Frm_ThermoInput.__init__(self, parent)

	def onVal_TI_P1( self, event ):
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

	def CreateState1(self,sz_TI_State1):
		"""
			This populates all of State 1 with the necissary variables.
			What is necissary was decided in the previous frame.
		"""
		print('Setting up State 1')
		for i in range(len(self.inputList[0])):
			#Make the text label
			txtName = 'txt_TI_'+ str(self.inputList[0][i])
			self.txtName = wx.StaticText( self, wx.ID_ANY, self.inputList[0][i], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.txtName.Wrap( -1 )
			sz_TI_State1.Add( self.txtName, 0, wx.ALL, 5 )

			#Make the input box
			valName = 'val_TI_'+ str(self.inputList[0][i])
			self.valName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			sz_TI_State1.Add( self.valName, 0, wx.ALL, 5 )

			self.nameList.append([txtName,valName])

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
			self.valName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			sz_TI_State2.Add( self.valName, 0, wx.ALL, 5 )

			self.nameList.append([txtName,valName])

	def CreateOther(self,sz_TI_Other):
		"""
			This populates all of Other with the necissary variables.
			What is necissary was decided in the previous frame.
		"""
		print('Setting up Other')
		for i in range(len(self.inputList[2])):
			#Make the text label
			txtName = 'txt_TI_'+ str(self.inputList[0][i])
			self.txtName = wx.StaticText( self, wx.ID_ANY, self.inputList[2][i], wx.DefaultPosition, wx.DefaultSize, 0 )
			self.txtName.Wrap( -1 )
			sz_TI_Other.Add( self.txtName, 0, wx.ALL, 5 )

			#Make the input box
			valName = 'val_TI_'+ str(self.inputList[2][i])
			self.valName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
			sz_TI_Other.Add( self.valName, 0, wx.ALL, 5 )

			self.nameList.append([txtName,valName])

	def CreateEvents(self):
		#Add an event to that box
		for i in range(len(self.nameList)):
			self.eventName = 'onVal_TI_'+ str(self.inputList[0][i])
			valName = self.nameList[i][1]
			self.valName.Bind( wx.EVT_TEXT_ENTER, self.eventName )

if __name__ == '__main__':
	app = wx.App()
	frame = LogicThermoInput(None)
	frame.Show()
	app.MainLoop()