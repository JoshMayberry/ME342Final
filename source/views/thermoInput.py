import wx

class frm_ThermoInput ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
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
		
		
		sz_TI_State1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
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
		
		
		sz_TI_State2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
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
		
		
		sz_TI_Other.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
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