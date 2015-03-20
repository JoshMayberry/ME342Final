import wx
from ..views import Frm_ThermoSetup
from .logicThermoInput import LogicThermoInput

class LogicThermoSetup(Frm_ThermoSetup):
	def __init__(self, parent):

		print ("Building ", self.__class__)
		# build gui
		Frm_ThermoSetup.__init__(self, parent)

	def onBtnClick_Medium_IdealGas( self, event ):
		event.Skip()
	
	def onBtnClick_Medium_R132( self, event ):
		event.Skip()
	
	def onBtnClick_System_Closed( self, event ):
		event.Skip()
	
	def onBtnClick_System_Steady( self, event ):
		event.Skip()
	
	def onBtnClick_System_Unsteady( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Rigid( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Piston( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Membrane( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Nozzle( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Turbine( self, event ):
		event.Skip()
	
	def onBtnClick_Container_HeatExch( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Mixing( self, event ):
		event.Skip()
	
	def onBtnClick_Etc_Adiabadic( self, event ):
		event.Skip()
	
	def onBtnClick_Etc_Isothermal( self, event ):
		event.Skip()
	
	def onBtnClick_Etc_Isotropic( self, event ):
		event.Skip()
	
	def onBtnClick_Etc_Polytropic( self, event ):
		event.Skip()
	
	def onBtnClick_Etc_Nozzle( self, event ):
		event.Skip()
	
	def onBtnClick_ContinueToInput( self, event ):
		LogicThermoInput(self).Show()
		self.Destroy()
		event.Skip()

if __name__ == '__main__':
	app = wx.App()
	frame = LogicThermoSetup(None)
	frame.Show()
	app.MainLoop()