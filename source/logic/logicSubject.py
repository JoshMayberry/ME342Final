from ..views import Frm_Subject
from .logicThermoSetup import LogicThermoSetup

#Builds the GUI and handels events
class LogicSubject(Frm_Subject):
	def __init__(self,parent):
		Frm_Subject.__init__(self,parent)
		self.parent = parent

	def onBtnClick_ContinueToSetup( self, event ):
		LogicThermoSetup(self.parent).Show()
		self.Destroy()
		event.Skip()

