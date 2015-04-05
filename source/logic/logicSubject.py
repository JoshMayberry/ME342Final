from ..views import Frm_Subject #Needed to communicate with the frame
from .logicThermoSetup import LogicThermoSetup #Needed to go to the next frame of thermo
from .logicUnitConverter import LogicUnitConverter #Needed to go to the frame of Unit Conversion
from .logicThermoTableLookup import LogicThermoTableLookup #Needed to go to the frame of Thermo Table Lookup

#Builds the GUI and handels events
class LogicSubject(Frm_Subject):
	def __init__(self,parent):
		Frm_Subject.__init__(self,parent)
		self.parent = parent

	def onBtnClick_ContinueToThermoSetup( self, event ):
		lts = LogicThermoSetup(self)
		lts.Show()
		self.Hide()
		event.Skip()

	def onBtnClick_ContinueToUnitConverter( self, event ):
		luc = LogicUnitConverter(self)
		luc.Show()
		self.Hide()
		event.Skip()

	def onBtnClick_ContinueToThermoTableLookup( self, event ):
		ltt = LogicThermoTableLookup(self)
		ltt.Show()
		self.Hide()
		event.Skip()

