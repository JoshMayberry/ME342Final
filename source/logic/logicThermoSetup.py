import wx
from ..views import ThermoSetup

class LogicThermoSetup(ThermoSetup):
	def __init__(self, parent):

		print ("Building GUI~")
		# build gui
		ThermoSetup.__init__(self, parent)

if __name__ == '__main__':
	app = wx.App()
	frame = LogicThermoSetup(None)
	frame.Show()
	app.MainLoop()