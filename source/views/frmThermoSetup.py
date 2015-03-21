import wx

class Frm_ThermoSetup ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 304,307 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		sz_ThermoSetup = wx.BoxSizer( wx.VERTICAL )
		
		self.tit_TS_Setup = wx.StaticText( self, wx.ID_ANY, u"Thermodynamics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tit_TS_Setup.Wrap( -1 )
		sz_ThermoSetup.Add( self.tit_TS_Setup, 0, wx.ALL|wx.EXPAND, 5 )
		
		sz_TS_Setups = wx.FlexGridSizer( 0, 3, 0, 0 )
		sz_TS_Setups.SetFlexibleDirection( wx.BOTH )
		sz_TS_Setups.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sz_TS_Medium = wx.FlexGridSizer( 0, 1, 0, 0 )
		sz_TS_Medium.SetFlexibleDirection( wx.BOTH )
		sz_TS_Medium.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_TS_Medium = wx.StaticText( self, wx.ID_ANY, u"Medium", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TS_Medium.Wrap( -1 )
		sz_TS_Medium.Add( self.txt_TS_Medium, 0, wx.ALL, 5 )
		
		self.btn_TS_Medium1 = wx.RadioButton( self, wx.ID_ANY, u"Ideal Gas", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.btn_TS_Medium1.SetValue( True ) 
		sz_TS_Medium.Add( self.btn_TS_Medium1, 0, wx.ALL, 5 )
		
		self.btn_TS_Medium2 = wx.RadioButton( self, wx.ID_ANY, u"Water", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TS_Medium.Add( self.btn_TS_Medium2, 0, wx.ALL, 5 )
		
		self.btn_TS_Medium3 = wx.RadioButton( self, wx.ID_ANY, u"R-132a", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TS_Medium.Add( self.btn_TS_Medium3, 0, wx.ALL, 5 )
		
		self.txt_TS_System = wx.StaticText( self, wx.ID_ANY, u"System", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TS_System.Wrap( -1 )
		sz_TS_Medium.Add( self.txt_TS_System, 0, wx.ALL, 5 )
		
		self.btn_TS_System1 = wx.RadioButton( self, wx.ID_ANY, u"Closed", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.btn_TS_System1.SetValue( True ) 
		sz_TS_Medium.Add( self.btn_TS_System1, 0, wx.ALL, 5 )
		
		self.btn_TS_System2 = wx.RadioButton( self, wx.ID_ANY, u"Steady", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TS_Medium.Add( self.btn_TS_System2, 0, wx.ALL, 5 )
		
		self.btn_TS_System3 = wx.RadioButton( self, wx.ID_ANY, u"Unsteady", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TS_Medium.Add( self.btn_TS_System3, 0, wx.ALL, 5 )
		
		
		sz_TS_Setups.Add( sz_TS_Medium, 1, wx.EXPAND, 5 )
		
		sz_TS_Container = wx.FlexGridSizer( 0, 1, 0, 0 )
		sz_TS_Container.SetFlexibleDirection( wx.BOTH )
		sz_TS_Container.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_TS_Container = wx.StaticText( self, wx.ID_ANY, u"Container", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TS_Container.Wrap( -1 )
		sz_TS_Container.Add( self.txt_TS_Container, 0, wx.ALL, 5 )
		
		self.btn_TS_Container1 = wx.RadioButton( self, wx.ID_ANY, u"Rigid", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.btn_TS_Container1.SetValue( True ) 
		sz_TS_Container.Add( self.btn_TS_Container1, 0, wx.ALL, 5 )
		
		self.btn_TS_Container2 = wx.RadioButton( self, wx.ID_ANY, u"Piston", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TS_Container.Add( self.btn_TS_Container2, 0, wx.ALL, 5 )
		
		self.btn_TS_Container3 = wx.RadioButton( self, wx.ID_ANY, u"Membrane", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TS_Container.Add( self.btn_TS_Container3, 0, wx.ALL, 5 )
		
		self.btn_TS_Container4 = wx.RadioButton( self, wx.ID_ANY, u"Nozzle", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TS_Container.Add( self.btn_TS_Container4, 0, wx.ALL, 5 )
		
		self.btn_TS_Container5 = wx.RadioButton( self, wx.ID_ANY, u"Turbine", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TS_Container.Add( self.btn_TS_Container5, 0, wx.ALL, 5 )
		
		self.btn_TS_Container6 = wx.RadioButton( self, wx.ID_ANY, u"Heat Exchanger", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TS_Container.Add( self.btn_TS_Container6, 0, wx.ALL, 5 )
		
		self.btn_TS_Container7 = wx.RadioButton( self, wx.ID_ANY, u"Mixing Chaimber", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TS_Container.Add( self.btn_TS_Container7, 0, wx.ALL, 5 )
		
		
		sz_TS_Setups.Add( sz_TS_Container, 1, wx.EXPAND, 5 )
		
		sz_TI_Etc = wx.FlexGridSizer( 0, 1, 0, 0 )
		sz_TI_Etc.SetFlexibleDirection( wx.BOTH )
		sz_TI_Etc.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_TS_Etc = wx.StaticText( self, wx.ID_ANY, u"Etc", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TS_Etc.Wrap( -1 )
		sz_TI_Etc.Add( self.txt_TS_Etc, 0, wx.ALL, 5 )
		
		self.btn_TS_Adiabadic = wx.CheckBox( self, wx.ID_ANY, u"Adiabadic", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TI_Etc.Add( self.btn_TS_Adiabadic, 0, wx.ALL, 5 )
		
		self.btn_TS_Isothermal = wx.CheckBox( self, wx.ID_ANY, u"Isothermal", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TI_Etc.Add( self.btn_TS_Isothermal, 0, wx.ALL, 5 )
		
		self.btn_TS_Reversable = wx.CheckBox( self, wx.ID_ANY, u"Reversable", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TI_Etc.Add( self.btn_TS_Reversable, 0, wx.ALL, 5 )
		
		self.btn_TS_Polytropic = wx.CheckBox( self, wx.ID_ANY, u"Polytropic", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TI_Etc.Add( self.btn_TS_Polytropic, 0, wx.ALL, 5 )
		
		self.btn_TS_Valve = wx.CheckBox( self, wx.ID_ANY, u"Valve", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TI_Etc.Add( self.btn_TS_Valve, 0, wx.ALL, 5 )
		
		self.txt_TS_Units = wx.StaticText( self, wx.ID_ANY, u"Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TS_Units.Wrap( -1 )
		sz_TI_Etc.Add( self.txt_TS_Units, 0, wx.ALL, 5 )
		
		units_TS_ChooseChoices = ['Metric','English']
		self.units_TS_Choose = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), units_TS_ChooseChoices, 0 )
		self.units_TS_Choose.SetSelection( 0 )
		sz_TI_Etc.Add( self.units_TS_Choose, 0, wx.ALL, 5 )
		
		
		sz_TS_Setups.Add( sz_TI_Etc, 1, wx.EXPAND, 5 )
		
		
		sz_ThermoSetup.Add( sz_TS_Setups, 1, wx.EXPAND, 5 )
		
		self.btn_TS_Continue = wx.Button( self, wx.ID_ANY, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btn_TS_Continue.SetDefault() 
		sz_ThermoSetup.Add( self.btn_TS_Continue, 0, wx.ALL, 5 )
		
		
		self.SetSizer( sz_ThermoSetup )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_TS_Medium1.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_Medium_IdealGas )
		self.btn_TS_Medium2.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_Medium_Water )
		self.btn_TS_Medium3.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_Medium_R132 )
		self.btn_TS_System1.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_System_Closed )
		self.btn_TS_System2.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_System_Steady )
		self.btn_TS_System3.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_System_Unsteady )
		self.btn_TS_Container1.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_Container_Rigid )
		self.btn_TS_Container2.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_Container_Piston )
		self.btn_TS_Container3.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_Container_Membrane )
		self.btn_TS_Container4.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_Container_Nozzle )
		self.btn_TS_Container5.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_Container_Turbine )
		self.btn_TS_Container6.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_Container_HeatExch )
		self.btn_TS_Container7.Bind( wx.EVT_RADIOBUTTON, self.onBtnClick_Container_Mixing )
		self.btn_TS_Adiabadic.Bind( wx.EVT_CHECKBOX, self.onBtnClick_Etc_Adiabadic )
		self.btn_TS_Isothermal.Bind( wx.EVT_CHECKBOX, self.onBtnClick_Etc_Isothermal )
		self.btn_TS_Reversable.Bind( wx.EVT_CHECKBOX, self.onBtnClick_Etc_Reversable )
		self.btn_TS_Polytropic.Bind( wx.EVT_CHECKBOX, self.onBtnClick_Etc_Polytropic )
		self.btn_TS_Valve.Bind( wx.EVT_CHECKBOX, self.onBtnClick_Etc_Valve )
		self.btn_TS_Continue.Bind( wx.EVT_BUTTON, self.onBtnClick_ContinueToInput )
	
	def __del__( self ):
		pass

if __name__ == '__main__':
	app = wx.App()
	frame = ThermoSetup(None)
	frame.Show()
	app.MainLoop()

