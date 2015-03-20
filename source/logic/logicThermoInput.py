import wx
from ..views import Frm_ThermoInput

class LogicThermoInput(Frm_ThermoInput):
	def __init__(self, parent):
		print ("Building GUI~")
		print ("Building ", self.__class__)
		# build gui
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

if __name__ == '__main__':
	app = wx.App()
	frame = LogicThermoInput(None)
	frame.Show()
	app.MainLoop()