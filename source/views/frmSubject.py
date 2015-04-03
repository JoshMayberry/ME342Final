import wx

class Frm_Subject ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Problem Solver", pos = wx.DefaultPosition, size = wx.Size( 340,165), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		sz_Subject = wx.BoxSizer( wx.VERTICAL )
		
		self.txt_subject = wx.StaticText( self, wx.ID_ANY, u"Choose Your Subject", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_subject.Wrap( -1 )
		self.txt_subject.SetFont( wx.Font( 25, 70, 90, 90, True, wx.EmptyString ) )
		self.txt_subject.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		sz_Subject.Add( self.txt_subject, 0, wx.ALL, 5 )
		
		sz_btns = wx.FlexGridSizer( 0, 2, 0, 0 )
		sz_btns.SetFlexibleDirection( wx.BOTH )
		sz_btns.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btn_Thermo = wx.Button( self, wx.ID_ANY, u"Thermodynamics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_Thermo.SetDefault() 
		sz_btns.Add( self.btn_Thermo, 0, wx.ALL, 5 )

		self.btn_UC = wx.Button( self, wx.ID_ANY, u"Unit Conversion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_UC.SetDefault() 
		sz_btns.Add( self.btn_UC, 0, wx.ALL, 5 )

		self.btn_TT = wx.Button( self, wx.ID_ANY, u"Thermo Tables", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_TT.SetDefault() 
		sz_btns.Add( self.btn_TT, 0, wx.ALL, 5 )
		
		
		sz_Subject.Add( sz_btns, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sz_Subject )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_Thermo.Bind( wx.EVT_BUTTON, self.onBtnClick_ContinueToThermoSetup )
		self.btn_UC.Bind( wx.EVT_BUTTON, self.onBtnClick_ContinueToUnitConverter )
		self.btn_TT.Bind( wx.EVT_BUTTON, self.onBtnClick_ContinueToThermoTableLookup )
	
	def __del__( self ):
		pass

	def setup_events(self):
		self.Bind(wx.EVT_BUTTON, self.onBtnClick, self.thermoBtn)

if __name__ == '__main__':
	app = wx.App()
	frame = MyApp(None)
	frame.Show()
	app.MainLoop()

