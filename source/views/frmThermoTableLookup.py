import wx

class Frm_ThermoTableLookup ( wx.Frame ):
	
	def __init__( self, parent ):
		self.input = [-1,[-1,-1,[[-1,-1],[-1,-1]]]]
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 435,209 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		sz_TT_Main = wx.FlexGridSizer( 0, 1, 0, 0 )
		sz_TT_Main.SetFlexibleDirection( wx.BOTH )
		sz_TT_Main.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sz_TT_Medium = wx.FlexGridSizer( 0, 4, 0, 0 )
		sz_TT_Medium.SetFlexibleDirection( wx.BOTH )
		sz_TT_Medium.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_TT_Title = wx.StaticText( self, wx.ID_ANY, u"Thermo Lookup", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_Title.Wrap( -1 )
		self.txt_TT_Title.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		sz_TT_Medium.Add( self.txt_TT_Title, 0, wx.ALL, 5 )
		
		self.txt_TT_Spacer = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_Spacer.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_Spacer, 0, wx.ALL, 5 )
		
		self.txt_TT_MediumInput = wx.StaticText( self, wx.ID_ANY, u"Medium", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_MediumInput.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_MediumInput, 0, wx.ALL, 5 )
		
		choice_TT_MediumChoices = ['','Water','R134a','Air','Ammonia','Argon','Benzene','Bromine','n-Butane','Carbon dioxide','Carbon monoxide','Carbon tetrachloride','Chlorine','Chloroform','R12','R21','Ethane','Ethyl alcohol','Ethylene','Helium','n-Hexane','Hydrogen','Krypton','Methane','Methyl alcohol','Methyl chloride','Neon','Nitrogen','Nitrous oxide','Oxygen','Propane','Propylene','Sulfur dioxide','R11','Xenon']
		self.choice_TT_Medium = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_TT_MediumChoices, 0 )
		self.choice_TT_Medium.SetSelection( 0 )
		sz_TT_Medium.Add( self.choice_TT_Medium, 0, wx.ALL, 5 )

		self.txt_TT_Goal_ColOf = wx.StaticText( self, wx.ID_ANY, u"I want to know", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_Goal_ColOf.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_Goal_ColOf, 0, wx.ALL, 5 )
		
		medium, choices = [],[]
		self.choice_TT_Goal_ColOf = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choices, 0 )
		self.choice_TT_Goal_ColOf.SetSelection( 1 )
		sz_TT_Medium.Add( self.choice_TT_Goal_ColOf, 0, wx.ALL, 5 )
		
		self.txt_TT_Goal_RowOf = wx.StaticText( self, wx.ID_ANY, u"of", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_Goal_RowOf.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_Goal_RowOf, 0, wx.ALL, 5 )

		mediumValue = self.choice_TT_Medium.GetString(self.choice_TT_Medium.GetSelection())
		self.txt_TT_Goal_RowOf = wx.StaticText( self, wx.ID_ANY, mediumValue, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_Goal_RowOf.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_Goal_RowOf, 0, wx.ALL, 5 )
		
		self.txt_TT_Ref_ColOf = wx.StaticText( self, wx.ID_ANY, u"Using a", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_Ref_ColOf.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_Ref_ColOf, 0, wx.ALL, 5 )
		
		self.choice_TT_Ref_ColOf = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choices, 0 )
		self.choice_TT_Ref_ColOf.SetSelection( 1 )
		sz_TT_Medium.Add( self.choice_TT_Ref_ColOf, 0, wx.ALL, 5 )
		
		self.txt_TT_Ref_RowOf = wx.StaticText( self, wx.ID_ANY, u"of", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_Ref_RowOf.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_Ref_RowOf, 0, wx.ALL, 5 )
		
		self.txtCtrl_TT_Ref_RowOf = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TT_Medium.Add( self.txtCtrl_TT_Ref_RowOf, 0, wx.ALL, 5 )

		self.txt_TT_Ref_ColOf = wx.StaticText( self, wx.ID_ANY, u"And a", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_Ref_ColOf.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_Ref_ColOf, 0, wx.ALL, 5 )
		
		self.choice_TT_Ref2_ColOf = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choices, 0 )
		self.choice_TT_Ref2_ColOf.SetSelection( 1 )
		sz_TT_Medium.Add( self.choice_TT_Ref2_ColOf, 0, wx.ALL, 5 )
		
		self.txt_TT_Ref2_RowOf = wx.StaticText( self, wx.ID_ANY, u"of", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_Ref2_RowOf.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_Ref2_RowOf, 0, wx.ALL, 5 )
		
		self.txtCtrl_TT_Ref2_RowOf = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TT_Medium.Add( self.txtCtrl_TT_Ref2_RowOf, 0, wx.ALL, 5 )

		self.btn_TT_Go = wx.Button( self, wx.ID_ANY, u"Go!", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_TT_Medium.Add( self.btn_TT_Go, 0, wx.ALL, 5 )
		
		self.txt_TT_Spacer2 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_Spacer2.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_Spacer2, 0, wx.ALL, 5 )
		
		self.txt_TT_Answer = wx.StaticText( self, wx.ID_ANY, u"Answer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_Answer.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_Answer, 0, wx.ALL, 5 )
		
		self.txt_TT_AnswerValue = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TT_AnswerValue.Wrap( -1 )
		sz_TT_Medium.Add( self.txt_TT_AnswerValue, 0, wx.ALL, 5 )
		
		
		sz_TT_Main.Add( sz_TT_Medium, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sz_TT_Main )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.choice_TT_Medium.Bind( wx.EVT_CHOICE, self.onChoiceMedium )
		self.choice_TT_Goal_ColOf.Bind( wx.EVT_CHOICE, self.onChoiceGoalColOf )
		self.choice_TT_Ref_ColOf.Bind( wx.EVT_CHOICE, self.onChoiceRefColOf )
		self.txtCtrl_TT_Ref_RowOf.Bind( wx.EVT_TEXT, self.onTxtRefRowOf )
		self.choice_TT_Ref2_ColOf.Bind( wx.EVT_CHOICE, self.onChoiceRef2ColOf )
		self.txtCtrl_TT_Ref2_RowOf.Bind( wx.EVT_TEXT, self.onTxtRef2RowOf )
		self.btn_TT_Go.Bind( wx.EVT_BUTTON, self.onBtnClickGo )
	
	def __del__( self ):
		pass
	

