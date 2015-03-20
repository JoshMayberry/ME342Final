import wx
from ..views import Frm_ThermoSetup #Needed to communicate with the frame
from .logicThermoInput import LogicThermoInput #Needed to go to the next frame
import numpy as np #Needed for np.nan

class LogicThermoSetup(Frm_ThermoSetup):
	def __init__(self, parent):

		print ("Building ", self.__class__)
		self.parent = parent
		#Initialize Variables
		self.medium,self.system,self.container = 'IdealGas','Closed','Rigid'
		self.etc1,self.etc2,self.etc3,self.etc4,self.etc5,self.valve = ('N/A',)*6
		self.W,self.Wdot,self.V2,self.V1,self.v2,self.v1,self.roe,self.Q,self.Qdot,self.m2dot,self.m1dot,self.midot,self.medot,self.pe,self.pi,self.p2,self.p1,self.ke,self.ki,self.k2,self.k1,self.m2,self.m1,self.u2,self.u1,self.s2,self.s1,self.se,self.si,self.T,self.k,self.Cp,self.Cv,self.Cavg = (np.nan,)*34
		self.inputList = [[],[],[]]
		#Build GUI
		Frm_ThermoSetup.__init__(self, parent)
		
	def onBtnClick_Medium_IdealGas( self, event ):
		self.medium = 'IdealGas'
		event.Skip()

	def onBtnClick_Medium_Water( self, event ):
		self.medium = 'Water'
		event.Skip()
	
	def onBtnClick_Medium_R132( self, event ):
		self.medium = 'R132'
		event.Skip()
	
	def onBtnClick_System_Closed( self, event ):
		self.system = 'Closed'
		event.Skip()
	
	def onBtnClick_System_Steady( self, event ):
		self.system = 'Steady'
		event.Skip()
	
	def onBtnClick_System_Unsteady( self, event ):
		self.system = 'Unsteady'
		event.Skip()
	
	def onBtnClick_Container_Rigid( self, event ):
		self.container = 'Rigid'
		event.Skip()
	
	def onBtnClick_Container_Piston( self, event ):
		self.container = 'Piston'
		event.Skip()
	
	def onBtnClick_Container_Membrane( self, event ):
		self.container = 'Membrane'
		event.Skip()
	
	def onBtnClick_Container_Nozzle( self, event ):
		self.container = 'Nozzle'
		event.Skip()
	
	def onBtnClick_Container_Turbine( self, event ):
		self.container = 'Turbine'
		event.Skip()
	
	def onBtnClick_Container_HeatExch( self, event ):
		self.container = 'HeatExch'
		event.Skip()
	
	def onBtnClick_Container_Mixing( self, event ):
		self.container = 'Mixing'
		event.Skip()
	
	def onBtnClick_Etc_Adiabadic( self, event ):
		if self.btn_TS_Adiabadic.GetValue() == True:
			self.etc1 = 'Adiabadic'
		else: self.etc1 = 'N/A'
		event.Skip()
	
	def onBtnClick_Etc_Isothermal( self, event ):
		if self.btn_TS_Isothermal.GetValue() == True:
			self.etc2 = 'Isothermal'
		else: self.etc2 = 'N/A'
		event.Skip()
	
	def onBtnClick_Etc_Reversable( self, event ):
		if self.btn_TS_Reversable.GetValue() == True:
			self.etc3 = 'Reversable'
		else: self.etc3 = 'N/A'
		event.Skip()
	
	def onBtnClick_Etc_Polytropic( self, event ):
		if self.btn_TS_Polytropic.GetValue() == True:
			self.etc4 = 'Polytropic'
		else: self.etc4 = 'N/A'
		event.Skip()

	def onBtnClick_Etc_Valve( self, event ):
		if self.btn_TS_Valve.GetValue() == True:
			self.valve = 'Valve'
		else: self.valve = 'N/A'
		event.Skip()
	
	def onBtnClick_ContinueToInput( self, event ):
		"""
			Depending on what was chosen, the next frame will be configured differently.
			This difference in configration is controlled by a multi-dimensional list.
		"""
		#To check variables: #print('medium',self.medium,'system',self.system,'container',self.container,'etc1',self.etc1,'etc2',self.etc2,'etc3',self.etc3,'etc4',self.etc4,'etc5',self.etc5,'valve',self.valve)

    #    if medium == 'R132a':
            #Use the R132a tables for calculations
    #    if medium == 'IdealGas':
            #Give them a scrollable dropdown list of gases to choose from

		if self.system == 'Closed':
			self.me,self.mi,self.hi,self.he,self.si,self.se = (0,)*6
			self.inputList[0].extend(['P1','u1','s1','m1','x1'])
			self.inputList[1].extend(['P2','u2','s2','m2','x2'])
			self.inputList[2].extend(['roe'])
		if self.system == 'Steady':
			self.m2,self.m1,self.u2,self.u1,self.s2,self.s1 = (0,)*6
			self.inputList[0].extend(['P1','ui','si','mi','x1'])
			self.inputList[1].extend(['P2','ue','se','me','x2'])
			self.inputList[2].extend(['roe'])
		if self.system == 'Unsteady':
			self.inputList[0].extend(['P1','u1','s1','m1','ui','si','mi','x1'])
			self.inputList[1].extend(['P2','u2','s2','m2','ue','se','me','x2'])
			self.inputList[2].extend(['roe'])

		if self.container == 'Rigid':
			self.V2,self.V1,self.v2,self.v1,self.m2dot,self.m1dot,self.midot,self.medot,self.pe,self.pi,self.p2,self.p1,self.ke,self.ki,self.k2,self.k1 = (0,)*16
			self.inputList[2].extend(['W','Wdot'])
		if self.container == 'Piston':
			self.pe,self.pi,self.p2,self.p1,self.ke,self.ki,self.k2,self.k1 = (0,)*8
			self.inputList[0].extend(['V1','v1','m1dot','midot'])
			self.inputList[1].extend(['V2','v2','m2dot','medot'])
			self.inputList[2].extend(['W','Wdot'])
		if self.container == 'Membrane':
			self.pe,self.pi,self.p2,self.p1,self.ke,self.ki,self.k2,self.k1 = (0,)*8
			self.inputList[0].extend(['V1','v1'])
			self.inputList[1].extend(['V2','v2'])
			self.inputList[2].extend(['W','Wdot'])
		if self.container == 'Nozzle':
			self.W,self.Wdot,self.pe,self.pi,self.p2,self.p1 = (0,)*6
			self.inputList[0].extend(['ki','k1','V1','v1'])
			self.inputList[1].extend(['ke','k2','V2','v2'])
		if self.container == 'Turbine':
			self.pe,self.pi,self.p2,self.p1 = (0,)*4
			self.inputList[0].extend(['ki','k1','V1','v1'])
			self.inputList[1].extend(['ke','k2','V2','v2'])
			self.inputList[2].extend(['W','Wdot'])
		if self.container == 'Mixing':
			self.W,self.Wdot,self.pe,self.pi,self.p2,self.p1,self.ke,self.ki,self.k2,self.k1 = (0,)*10
			self.inputList[0].extend(['V1','v1'])
			self.inputList[1].extend(['V2','v2'])
		if self.container == 'HeatExch':
			self.m2dot,self.m1dot,self.midot,self.medot,self.pe,self.pi,self.p2,self.p1,self.ke,self.ki,self.k2,self.k1 = (0,)*12
		
		if self.valve == 'Valve': #make it smart with the containers. Some modifications may have to be done to the .kv file. Example: Heat Exchangers don't have valves.
			self.W,self.Wdot,self.pe,self.pi,self.p2,self.p1,self.ke,self.ki,self.k2,self.k1 = (0,)*10
			self.inputList[0].extend(['V1','v1'])
			self.inputList[1].extend(['V2','v2'])

		if self.etc1 == 'Adiabadic':
			self.Q,self.Qdot = (0,)*2 #Make it smart with the adiabatic. Maybe it confirms if they don't choose it for a Turbine, or if they do for a Heat Exchanger.
		else:
			self.inputList[2].extend(['Q','Qdot'])
		
		if self.etc2 == 'Isothermal':
			self.inputList[0].extend(['T'])
		else:
			self.inputList[0].extend(['T1'])
			self.inputList[1].extend(['T2'])

		#if self.etc3 == 'Reversable':

		if self.etc4 == 'Polytropic':
			self.inputList[2].extend(['k','Cp','Cv','Cavg'])
		else:
			self.k,self.Cp,self.Cv,self.Cavg = (0,)*4

		args = self.inputList
		LogicThermoInput(self.parent,*args).Show()
		self.Destroy()
		event.Skip()

if __name__ == '__main__':
	app = wx.App()
	frame = LogicThermoSetup(None)
	frame.Show()
	app.MainLoop()