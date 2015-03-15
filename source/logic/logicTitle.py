from ..views import Title
from ..logic import LogicThermoSetup

#Builds the GUI and handels events
class LogicTitle(Title):
	def __init__(self,parent):
		Title.__init__(self,parent)
		self.parent = parent

	def onBtnClick( self, event ):
		print ("Hi from Logic Title")
		l = LogicThermoSetup(self.parent)
		l.Show()

		self.Destroy()
		event.Skip()

