# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class MyApp
###########################################################################

class Title ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Problem Solver", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		bSizerMain = wx.BoxSizer( wx.VERTICAL )
		
		self.stTitle = wx.StaticText( self, wx.ID_ANY, u"Choose Your Subject", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTitle.Wrap( -1 )
		self.stTitle.SetFont( wx.Font( 25, 70, 90, 90, True, wx.EmptyString ) )
		self.stTitle.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		bSizerMain.Add( self.stTitle, 0, wx.ALL, 5 )
		
		fgSizerBtn = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizerBtn.SetFlexibleDirection( wx.BOTH )
		fgSizerBtn.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.thermoBtn = wx.Button( self, wx.ID_ANY, u"Thermodynamics", wx.DefaultPosition, wx.DefaultSize )
		self.thermoBtn.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		fgSizerBtn.Add( self.thermoBtn, 0, wx.EXPAND, 5 )
		
		self.extraBtn = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizerBtn.Add( self.extraBtn, 0, wx.ALL, 5 )
		
		
		bSizerMain.Add( fgSizerBtn, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizerMain )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.setup_events()
	
	def __del__( self ):
		pass

	def setup_events(self):
		self.Bind(wx.EVT_BUTTON, self.onBtnClick, self.thermoBtn)

	# Virtual event handlers, overide them in your derived class
	def onBtnClick( self, event):
		print ("Hi from Title")
		event.Skip()




if __name__ == '__main__':
	app = wx.App()
	frame = MyApp(None)
	frame.Show()
	app.MainLoop()

