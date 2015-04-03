import wx
import wx.xrc

class Frm_UnitConverter ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 542,224 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		sz_UnitConverter = wx.FlexGridSizer( 0, 1, 0, 0 )
		sz_UnitConverter.SetFlexibleDirection( wx.BOTH )
		sz_UnitConverter.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_UC_Title = wx.StaticText( self, wx.ID_ANY, u"Enter Expression Here", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_UC_Title.Wrap( -1 )
		sz_UnitConverter.Add( self.txt_UC_Title, 0, wx.ALL, 5 )
		
		sz_UC_Expression = wx.FlexGridSizer( 0, 2, 0, 0 )
		sz_UC_Expression.SetFlexibleDirection( wx.BOTH )
		sz_UC_Expression.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_UC_Expression = wx.TextCtrl( self, 1001, wx.EmptyString, wx.DefaultPosition, wx.Size( 412,24 ), 0 )
		sz_UC_Expression.Add( self.txt_UC_Expression, 0, wx.ALL, 5 )
		
		self.txt_UC_ExpressionClear = wx.Button( self, 1002, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_UC_Expression.Add( self.txt_UC_ExpressionClear, 0, wx.ALL, 5 )
		
		
		sz_UnitConverter.Add( sz_UC_Expression, 1, wx.EXPAND, 5 )
		
		sz_UC_ExpressionResult = wx.FlexGridSizer( 0, 2, 0, 0 )
		sz_UC_ExpressionResult.SetFlexibleDirection( wx.BOTH )
		sz_UC_ExpressionResult.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sz_UC_Answer = wx.FlexGridSizer( 0, 2, 0, 0 )
		sz_UC_Answer.SetFlexibleDirection( wx.BOTH )
		sz_UC_Answer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_UC_Answer = wx.StaticText( self, wx.ID_ANY, u"Answer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_UC_Answer.Wrap( -1 )
		sz_UC_Answer.Add( self.txt_UC_Answer, 0, wx.ALL, 5 )
		
		self.txt_UC_ConvertFrom = wx.StaticText( self, wx.ID_ANY, u"Convert From", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_UC_ConvertFrom.Wrap( -1 )
		sz_UC_Answer.Add( self.txt_UC_ConvertFrom, 0, wx.ALL, 5 )
		
		self.answer = "                              "
		self.txt_UC_AnswerDisplay = wx.StaticText( self, 1003, self.answer, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_UC_AnswerDisplay.Wrap( -1 )
		#self.txt_UC_AnswerDisplay.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sz_UC_Answer.Add( self.txt_UC_AnswerDisplay, 0, wx.ALL, 5 )
		
		self.convFromList = []
		self.choice_UC_ConvertFrom = wx.Choice( self, 1004, wx.DefaultPosition, wx.DefaultSize, self.convFromList, 0 )
		self.choice_UC_ConvertFrom.SetSelection( 0 )
		sz_UC_Answer.Add( self.choice_UC_ConvertFrom, 0, wx.ALL, 5 )
		
		self.txt_UC_UnitsConversion = wx.StaticText( self, wx.ID_ANY, u"Units Conversion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_UC_UnitsConversion.Wrap( -1 )
		sz_UC_Answer.Add( self.txt_UC_UnitsConversion, 0, wx.ALL, 5 )
		
		self.txt_UC_ConvertTo = wx.StaticText( self, wx.ID_ANY, u"Convert To", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_UC_ConvertTo.Wrap( -1 )
		sz_UC_Answer.Add( self.txt_UC_ConvertTo, 0, wx.ALL, 5 )
		
		self.answer2 =  "                              "
		self.txt_UC_ConversionDisplay = wx.StaticText( self, 1005, self.answer2, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_UC_ConversionDisplay.Wrap( -1 )
		#self.txt_UC_ConversionDisplay.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		sz_UC_Answer.Add( self.txt_UC_ConversionDisplay, 0, wx.ALL, 5 )
		
		self.convToList = []
		self.choice_UC_ConvertTo = wx.Choice( self, 1006, wx.DefaultPosition, wx.DefaultSize, self.convToList, 0 )
		self.choice_UC_ConvertTo.SetSelection( 0 )
		sz_UC_Answer.Add( self.choice_UC_ConvertTo, 0, wx.ALL, 5 )
		
		
		sz_UC_ExpressionResult.Add( sz_UC_Answer, 1, wx.EXPAND, 5 )
		
		sz_UC_Conversion = wx.FlexGridSizer( 0, 1, 0, 0 )
		sz_UC_Conversion.SetFlexibleDirection( wx.BOTH )
		sz_UC_Conversion.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		sz_UC_Units = wx.FlexGridSizer( 0, 2, 0, 0 )
		sz_UC_Units.SetFlexibleDirection( wx.BOTH )
		sz_UC_Units.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.check_UC_UnitsConversion = wx.CheckBox( self, 1007, u"Units Conversion", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_UC_Units.Add( self.check_UC_UnitsConversion, 0, wx.ALL, 5 )
		
		self.choice_UC_Spacer1 = wx.StaticText( self, wx.ID_ANY, u" ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.choice_UC_Spacer1.Wrap( -1 )
		sz_UC_Units.Add( self.choice_UC_Spacer1, 0, wx.ALL, 5 )
		
		self.choice_UC_TypeOfUnits = wx.StaticText( self, wx.ID_ANY, u"Type of Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.choice_UC_TypeOfUnits.Wrap( -1 )
		sz_UC_Units.Add( self.choice_UC_TypeOfUnits, 0, wx.ALL, 5 )
		
		choice_UC_TypeOfUnitsChoices = ['Acceleration','Angle','Area','Area Mom. of Inertia','Computer Storage','Density','Energy, Work, or Heat','Energy/Mass','Force','Force/Length','Heat Flux','Heat Transfer Coefficent','Length or Distance','Light Intensity','Mass','Mass Flow Rate','Mass Mom. of Inertia','Mass/Area','Mass/Length','Power or Energy/Time','Pressure or Stress','Specific Heat','Specific Volume','Stress Intensity','Temperature','Thermal Conductance','Thermal Conductivity','Time','Torque or Moment','Velocity or Speed','Viscosity, Dynamic','Viscosity, Kinematic','Volume','Volume Flow Rate']
		self.choice_UC_TypeOfUnits = wx.Choice( self, 1008, wx.DefaultPosition, wx.DefaultSize, choice_UC_TypeOfUnitsChoices, 0 )
		self.choice_UC_TypeOfUnits.SetSelection( 0 )
		sz_UC_Units.Add( self.choice_UC_TypeOfUnits, 0, wx.ALL, 5 )
		
		
		sz_UC_Conversion.Add( sz_UC_Units, 1, wx.EXPAND, 5 )
		
		sz_UC_ConvertBtn = wx.FlexGridSizer( 0, 3, 0, 0 )
		sz_UC_ConvertBtn.SetFlexibleDirection( wx.BOTH )
		sz_UC_ConvertBtn.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_UC_Spacer2 = wx.StaticText( self, wx.ID_ANY, u"                                      ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_UC_Spacer2.Wrap( -1 )
		sz_UC_ConvertBtn.Add( self.txt_UC_Spacer2, 0, wx.ALL, 5 )
		
		self.btn_UC_Convert = wx.Button( self, wx.ID_ANY, u"Convert!", wx.DefaultPosition, wx.DefaultSize, 0 )
		sz_UC_ConvertBtn.Add( self.btn_UC_Convert, 0, wx.ALL, 5 )
		
		sz_UC_Conversion.Add( sz_UC_ConvertBtn, 1, wx.EXPAND, 5 )
		
#		self.btn_UC_Back = wx.Button( self, wx.ID_ANY, u"Back to Main", wx.DefaultPosition, wx.DefaultSize, 0 )
#		sz_UC_Conversion.Add( self.btn_UC_Back, 0, wx.ALL, 5 )
		
		sz_UC_ExpressionResult.Add( sz_UC_Conversion, 1, wx.EXPAND, 5 )
		
		
		sz_UnitConverter.Add( sz_UC_ExpressionResult, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( sz_UnitConverter )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txt_UC_Expression.Bind( wx.EVT_TEXT_ENTER, self.onExpression )
		self.txt_UC_ExpressionClear.Bind( wx.EVT_BUTTON, self.onClear )
		self.choice_UC_ConvertFrom.Bind( wx.EVT_CHOICE, self.onConvFrom )
		self.choice_UC_ConvertTo.Bind( wx.EVT_CHOICE, self.onConvTo )
		self.check_UC_UnitsConversion.Bind( wx.EVT_CHECKBOX, self.onConvYes )
		self.choice_UC_TypeOfUnits.Bind( wx.EVT_CHOICE, self.onType )
		self.btn_UC_Convert.Bind( wx.EVT_BUTTON, self.onConvBtn )
#		self.btn_UC_Back.Bind( wx.EVT_BUTTON, self.onBackToMain )
	
	def __del__( self ):
		pass