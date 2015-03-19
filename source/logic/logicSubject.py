from ..views import frm_Subject
from ..logic import LogicThermoSetup

#Builds the GUI and handels events
class LogicSubject(frm_Subject):
	def __init__(self,parent):
		frm_Subject.__init__(self,parent)
		self.parent = parent

	def onBtnClick_ContinueToSetup( self, event ):
		#print ("Hi from Logic Subject")
		LogicThermoSetup(self.parent).Show()
		self.Destroy()
		event.Skip()

