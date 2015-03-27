
from ..views import Frm_Subject #Needed to communicate with the frame
from .logicThermoSetup import LogicThermoSetup #Needed to go to the next frame of thermo
from .logicUnitConverter import LogicUnitConverter #Needed to go to the frame of Unit Conversion

#Builds the GUI and handels events
class LogicSubject(Frm_Subject):
	def __init__(self,parent):
		Frm_Subject.__init__(self,parent)
		self.parent = parent

	def onBtnClick_ContinueToThermoSetup( self, event ):
		LogicThermoSetup(self.parent).Show()
		self.Destroy()
		event.Skip()

	def onBtnClick_ContinueToUnitConverter( self, event ):
		LogicUnitConverter(self.parent).Show()
		self.Hide()
		event.Skip()

