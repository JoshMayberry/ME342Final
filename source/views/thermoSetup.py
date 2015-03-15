import wx

###########################################################################
## Class MyFrame2
###########################################################################

class ThermoSetup ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 368,307 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
				
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.stThermo = wx.StaticText( self, wx.ID_ANY, u"Thermodynamics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stThermo.Wrap( -1 )
		bSizer2.Add( self.stThermo, 0, wx.ALL|wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer2 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Medium", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_radioBtn1 = wx.RadioButton( self, wx.ID_ANY, u"Ideal Gas", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.m_radioBtn1.SetValue( True ) 
		fgSizer2.Add( self.m_radioBtn1, 0, wx.ALL, 5 )
		
		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"Water", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_radioBtn2, 0, wx.ALL, 5 )
		
		self.m_radioBtn4 = wx.RadioButton( self, wx.ID_ANY, u"R-132a", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_radioBtn4, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"System", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer2.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_radioBtn5 = wx.RadioButton( self, wx.ID_ANY, u"Closed", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.m_radioBtn5.SetValue( True ) 
		fgSizer2.Add( self.m_radioBtn5, 0, wx.ALL, 5 )
		
		self.m_radioBtn6 = wx.RadioButton( self, wx.ID_ANY, u"Steady", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_radioBtn6, 0, wx.ALL, 5 )
		
		self.m_radioBtn3 = wx.RadioButton( self, wx.ID_ANY, u"Unsteady", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_radioBtn3, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Container", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_radioBtn7 = wx.RadioButton( self, wx.ID_ANY, u"Rigid", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.m_radioBtn7.SetValue( True ) 
		fgSizer4.Add( self.m_radioBtn7, 0, wx.ALL, 5 )
		
		self.m_radioBtn8 = wx.RadioButton( self, wx.ID_ANY, u"Piston", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_radioBtn8, 0, wx.ALL, 5 )
		
		self.m_radioBtn9 = wx.RadioButton( self, wx.ID_ANY, u"Membrane", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_radioBtn9, 0, wx.ALL, 5 )
		
		self.m_radioBtn10 = wx.RadioButton( self, wx.ID_ANY, u"Nozzle", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_radioBtn10, 0, wx.ALL, 5 )
		
		self.m_radioBtn11 = wx.RadioButton( self, wx.ID_ANY, u"Turbine", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_radioBtn11, 0, wx.ALL, 5 )
		
		self.m_radioBtn12 = wx.RadioButton( self, wx.ID_ANY, u"Heat Exchanger", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_radioBtn12, 0, wx.ALL, 5 )
		
		self.m_radioBtn13 = wx.RadioButton( self, wx.ID_ANY, u"Mixing Chaimber", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_radioBtn13, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		fgSizer5 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Etc", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_radioBtn14 = wx.RadioButton( self, wx.ID_ANY, u"Adiabadic", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		fgSizer5.Add( self.m_radioBtn14, 0, wx.ALL, 5 )
		
		self.m_radioBtn15 = wx.RadioButton( self, wx.ID_ANY, u"Isothermal", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_radioBtn15, 0, wx.ALL, 5 )
		
		self.m_radioBtn16 = wx.RadioButton( self, wx.ID_ANY, u"Isotropic", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_radioBtn16, 0, wx.ALL, 5 )
		
		self.m_radioBtn17 = wx.RadioButton( self, wx.ID_ANY, u"Polytropic", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_radioBtn17, 0, wx.ALL, 5 )
		
		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Nozzle", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer5, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetDefault() 
		bSizer2.Add( self.m_button5, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
		
	# Virtual event handlers, overide them in your derived class
	def onBtnClick( self, event ):
		event.Skip()

if __name__ == '__main__':
	app = wx.App()
	frame = ThermoSetup(None)
	frame.Show()
	app.MainLoop()

