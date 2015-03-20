# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Frm_Subject
###########################################################################

class Frm_Subject ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Problem Solver", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sz_Subject = wx.BoxSizer( wx.VERTICAL )
		
		self.txt_subject = wx.StaticText( self, wx.ID_ANY, u"Choose Your Subject", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_subject.Wrap( -1 )
		self.txt_subject.SetFont( wx.Font( 25, 70, 90, 90, True, wx.EmptyString ) )
		self.txt_subject.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		sz_Subject.Add( self.txt_subject, 0, wx.ALL, 5 )
		
		sz_btns = wx.FlexGridSizer( 0, 2, 0, 0 )
		sz_btns.SetFlexibleDirection( wx.BOTH )
		sz_btns.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btn_Thermo = wx.Button( self, wx.ID_ANY, u"Thermodynamics", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.btn_Thermo.SetDefault() 
		self.btn_Thermo.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		
		sz_btns.Add( self.btn_Thermo, 0, wx.EXPAND, 5 )
		
		
		sz_Subject.Add( sz_btns, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sz_Subject )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btn_Thermo.Bind( wx.EVT_BUTTON, self.onBtnClick_ContinueToSetup )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onBtnClick_ContinueToSetup( self, event ):
		event.Skip()
	

###########################################################################
## Class Frm_ThermoSetup
###########################################################################

class Frm_ThermoSetup ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 368,307 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
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
	
	
	# Virtual event handlers, overide them in your derived class
	def onBtnClick_Medium_IdealGas( self, event ):
		event.Skip()
	
	def onBtnClick_Medium_Water( self, event ):
		event.Skip()
	
	def onBtnClick_Medium_R132( self, event ):
		event.Skip()
	
	def onBtnClick_System_Closed( self, event ):
		event.Skip()
	
	def onBtnClick_System_Steady( self, event ):
		event.Skip()
	
	def onBtnClick_System_Unsteady( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Rigid( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Piston( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Membrane( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Nozzle( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Turbine( self, event ):
		event.Skip()
	
	def onBtnClick_Container_HeatExch( self, event ):
		event.Skip()
	
	def onBtnClick_Container_Mixing( self, event ):
		event.Skip()
	
	def onBtnClick_Etc_Adiabadic( self, event ):
		event.Skip()
	
	def onBtnClick_Etc_Isothermal( self, event ):
		event.Skip()
	
	def onBtnClick_Etc_Reversable( self, event ):
		event.Skip()
	
	def onBtnClick_Etc_Polytropic( self, event ):
		event.Skip()
	
	def onBtnClick_Etc_Valve( self, event ):
		event.Skip()
	
	def onBtnClick_ContinueToInput( self, event ):
		event.Skip()
	

###########################################################################
## Class Frm_ThermoInput
###########################################################################

class Frm_ThermoInput ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		siz_ThermoInput_Title = wx.BoxSizer( wx.VERTICAL )
		
		self.tit_TI_Input = wx.StaticText( self, wx.ID_ANY, u"Inputs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tit_TI_Input.Wrap( -1 )
		siz_ThermoInput_Title.Add( self.tit_TI_Input, 0, wx.ALL, 5 )
		
		sz_ThermoInput_Inputs = wx.FlexGridSizer( 0, 3, 0, 0 )
		sz_ThermoInput_Inputs.SetFlexibleDirection( wx.BOTH )
		sz_ThermoInput_Inputs.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sz_TI_State1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sz_TI_State1.SetFlexibleDirection( wx.BOTH )
		sz_TI_State1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_TI_State1 = wx.StaticText( self, wx.ID_ANY, u"State 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_State1.Wrap( -1 )
		sz_TI_State1.Add( self.txt_TI_State1, 0, wx.ALL, 5 )
		
		self.txt_TI_spacer1 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_spacer1.Wrap( -1 )
		sz_TI_State1.Add( self.txt_TI_spacer1, 0, wx.ALL, 5 )
		
		self.txt_TI_P1 = wx.StaticText( self, wx.ID_ANY, u"P1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_P1.Wrap( -1 )
		sz_TI_State1.Add( self.txt_TI_P1, 0, wx.ALL, 5 )
		
		self.val_TI_P1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TI_State1.Add( self.val_TI_P1, 0, wx.ALL, 5 )
		
		self.txt_TI_V1 = wx.StaticText( self, wx.ID_ANY, u"V1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_V1.Wrap( -1 )
		sz_TI_State1.Add( self.txt_TI_V1, 0, wx.ALL, 5 )
		
		self.val_TI_V1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TI_State1.Add( self.val_TI_V1, 0, wx.ALL, 5 )
		
		
		sz_ThermoInput_Inputs.Add( sz_TI_State1, 1, wx.EXPAND, 5 )
		
		sz_TI_State2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		sz_TI_State2.SetFlexibleDirection( wx.BOTH )
		sz_TI_State2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_TI_State2 = wx.StaticText( self, wx.ID_ANY, u"State 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_State2.Wrap( -1 )
		sz_TI_State2.Add( self.txt_TI_State2, 0, wx.ALL, 5 )
		
		self.txt_TI_spacer2 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_spacer2.Wrap( -1 )
		sz_TI_State2.Add( self.txt_TI_spacer2, 0, wx.ALL, 5 )
		
		self.txt_TI_P2 = wx.StaticText( self, wx.ID_ANY, u"P2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_P2.Wrap( -1 )
		sz_TI_State2.Add( self.txt_TI_P2, 0, wx.ALL, 5 )
		
		self.val_TI_P2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TI_State2.Add( self.val_TI_P2, 0, wx.ALL, 5 )
		
		self.txt_TI_V2 = wx.StaticText( self, wx.ID_ANY, u"V2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_V2.Wrap( -1 )
		sz_TI_State2.Add( self.txt_TI_V2, 0, wx.ALL, 5 )
		
		self.val_TI_V2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TI_State2.Add( self.val_TI_V2, 0, wx.ALL, 5 )
		
		
		sz_ThermoInput_Inputs.Add( sz_TI_State2, 1, wx.EXPAND, 5 )
		
		sz_TI_Other = wx.FlexGridSizer( 0, 2, 0, 0 )
		sz_TI_Other.SetFlexibleDirection( wx.BOTH )
		sz_TI_Other.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_TI_Other = wx.StaticText( self, wx.ID_ANY, u"Other", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_Other.Wrap( -1 )
		sz_TI_Other.Add( self.txt_TI_Other, 0, wx.ALL, 5 )
		
		self.txt_TI_spacer3 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_spacer3.Wrap( -1 )
		sz_TI_Other.Add( self.txt_TI_spacer3, 0, wx.ALL, 5 )
		
		self.txt_TI_W = wx.StaticText( self, wx.ID_ANY, u"W", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_W.Wrap( -1 )
		sz_TI_Other.Add( self.txt_TI_W, 0, wx.ALL, 5 )
		
		self.val_TI_W = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TI_Other.Add( self.val_TI_W, 0, wx.ALL, 5 )
		
		self.txt_TI_Q = wx.StaticText( self, wx.ID_ANY, u"Q", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_Q.Wrap( -1 )
		sz_TI_Other.Add( self.txt_TI_Q, 0, wx.ALL, 5 )
		
		self.val_TI_Q = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TI_Other.Add( self.val_TI_Q, 0, wx.ALL, 5 )
		
		
		sz_ThermoInput_Inputs.Add( sz_TI_Other, 1, wx.EXPAND, 5 )
		
		
		siz_ThermoInput_Title.Add( sz_ThermoInput_Inputs, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( siz_ThermoInput_Title )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.val_TI_P1.Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_P1 )
		self.val_TI_V1.Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_V1 )
		self.val_TI_P2.Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_P2 )
		self.val_TI_V2.Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_V2 )
		self.val_TI_W.Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_W )
		self.val_TI_Q.Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_Q )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onVal_TI_P1( self, event ):
		event.Skip()
	
	def onVal_TI_V1( self, event ):
		event.Skip()
	
	def onVal_TI_P2( self, event ):
		event.Skip()
	
	def onVal_TI_V2( self, event ):
		event.Skip()
	
	def onVal_TI_W( self, event ):
		event.Skip()
	
	def onVal_TI_Q( self, event ):
		event.Skip()
	

