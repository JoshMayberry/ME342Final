import wx
#from ..logic import LogicThermoInput

class Frm_ThermoInput ( wx.Frame ):
	#Note: Most of this frame is built by logic, because it needs to determine what is to be shown.
	
	def __init__( self, parent ):
		windowSize = self.setSize()
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( windowSize[0],windowSize[1] ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		siz_ThermoInput_Title = wx.BoxSizer( wx.VERTICAL )
		
		#The Main Title
		self.tit_TI_Input = wx.StaticText( self, wx.ID_ANY, u"Inputs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tit_TI_Input.Wrap( -1 )
		siz_ThermoInput_Title.Add( self.tit_TI_Input, 0, wx.ALL, 5 )
		
		sz_ThermoInput_Inputs = wx.FlexGridSizer( 0, 3, 0, 0 )
		sz_ThermoInput_Inputs.SetFlexibleDirection( wx.BOTH )
		sz_ThermoInput_Inputs.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		#This is the spacer
			#You Cannot add the same spacer to the same sizer twice, so you need multiple ones.
			#These are not being added yet. they will be added later on.
		self.txt_TI_spacer1 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_spacer1.Wrap( -1 )
		self.txt_TI_spacer2 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_spacer2.Wrap( -1 )
		
#The inputs
	#The input for State 1 sizer starts here
		##Setup the title
		sz_TI_State1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		sz_TI_State1.SetFlexibleDirection( wx.BOTH )
		sz_TI_State1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_TI_State1 = wx.StaticText( self, wx.ID_ANY, u"State 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_State1.Wrap( -1 )
		sz_TI_State1.Add( self.txt_TI_State1, 0, wx.ALL, 5 )
		
		#Setup the spacers
		sz_TI_State1.Add( self.txt_TI_spacer1, 0, wx.ALL, 5 )
		sz_TI_State1.Add( self.txt_TI_spacer2, 0, wx.ALL, 5 )
		
		##Generate all the State 1 input boxes
		self.CreateState1(sz_TI_State1)		
		sz_ThermoInput_Inputs.Add( sz_TI_State1, 1, wx.EXPAND, 5 )

	#The input for State 2 sizer starts here
		##Setup the title
		sz_TI_State2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		sz_TI_State2.SetFlexibleDirection( wx.BOTH )
		sz_TI_State2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_TI_State2 = wx.StaticText( self, wx.ID_ANY, u"State 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_State2.Wrap( -1 )
		sz_TI_State2.Add( self.txt_TI_State2, 0, wx.ALL, 5 )
		
		#Setup the spacers
		sz_TI_State2.Add( self.txt_TI_spacer1, 0, wx.ALL, 5 )
		sz_TI_State2.Add( self.txt_TI_spacer2, 0, wx.ALL, 5 )
		
		##Generate all the State 2 input boxes
		self.CreateState2(sz_TI_State2)		
		sz_ThermoInput_Inputs.Add( sz_TI_State2, 1, wx.EXPAND, 5 )
		
	#The input for Other sizer starts here
		sz_TI_OtherMain = wx.FlexGridSizer( 0, 1, 0, 0 )
		sz_TI_OtherMain.SetFlexibleDirection( wx.BOTH )
		sz_TI_OtherMain.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sz_TI_OtherTitle = wx.FlexGridSizer( 0, 2, 0, 0 )
		sz_TI_OtherTitle.SetFlexibleDirection( wx.BOTH )
		sz_TI_OtherTitle.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		##Setup the title
		self.txt_TI_Other = wx.StaticText( self, wx.ID_ANY, u"Other", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_TI_Other.Wrap( -1 )
		sz_TI_OtherTitle.Add( self.txt_TI_Other, 0, wx.ALL, 5 )
		
		#Setup the spacer
		sz_TI_OtherTitle.Add( self.txt_TI_spacer1, 0, wx.ALL, 5 )

		if self.medium == 'IdealGas':
			#Make the text label
			temp = wx.StaticText( self, wx.ID_ANY, 'Ideal Gas', wx.DefaultPosition, wx.DefaultSize, 0  )
			temp.Wrap( -1 )
			sz_TI_OtherTitle.Add( temp, 0, wx.ALL, 5 )

			#Make the ideal gas dropdown list
			unit_Choices = ['Air','Ammonia','Argon','Benzene','Bromine','n-Butane','Carbon dioxide','Carbon monoxide','Carbon tetrachloride','Chlorine','Chloroform','R12','R21','Ethane','Ethyl alcohol','Ethylene','Helium','n-Hexane','Hydrogen','Krypton','Methane','Methyl alcohol','Methyl chloride','Neon','Nitrogen','Nitrous oxide','Oxygen','Propane','Propylene','Sulfur dioxide','R11','Xenon']
			unitName = wx.Choice( self, 4000, wx.DefaultPosition, wx.DefaultSize, unit_Choices, 0 )
			unitName.SetSelection(0)
			self.medium = 'Air'
			sz_TI_OtherTitle.Add( unitName, 0, wx.ALL, 5 )

		sz_TI_OtherMain.Add( sz_TI_OtherTitle, 1, wx.EXPAND, 5 )
		
		sz_TI_Other = wx.FlexGridSizer( 0, 3, 0, 0 )
		sz_TI_Other.SetFlexibleDirection( wx.BOTH )
		sz_TI_Other.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		##Generate all the Other input boxes
		self.CreateOther(sz_TI_Other)

		sz_TI_OtherMain.Add( sz_TI_Other, 1, wx.EXPAND, 5 )		
		sz_ThermoInput_Inputs.Add( sz_TI_OtherMain, 1, wx.EXPAND, 5 )	

	#The button sizer starts here
		siz_ThermoInput_Title.Add( sz_ThermoInput_Inputs, 1, wx.EXPAND, 5 )
		
		self.btn_TI_Continue = wx.Button( self, wx.ID_ANY, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
		siz_ThermoInput_Title.Add( self.btn_TI_Continue, 0, wx.ALL, 5 )
		
		
		self.SetSizer( siz_ThermoInput_Title )
		self.Layout()
		self.Centre( wx.BOTH )
		
	# Connect Events

		self.CreateEvents()
		#self.val_TI_P1.Bind( wx.EVT_TEXT_ENTER, self.onVal_TI_P1 )
		self.btn_TI_Continue.Bind( wx.EVT_BUTTON, self.onBtnClick_ContinueToResults )
	
	def __del__( self ):
		pass