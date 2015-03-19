## This is your main file


import source.views as views
import source.logic as logic
import wx

app = wx.App()
print ("Modules logic: ", dir(logic))
print ("Modules views: ", dir(views))
frame = logic.LogicSubject(None)
#frame = logic.LogicThermoSetup(None)
#frame = views.title.MyApp(None)
frame.Show()
app.MainLoop()