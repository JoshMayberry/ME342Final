	
class LogicThermoEquations:
	""" This regulates all the Thermo Equations."""
	
	def constants():
		#All units must be previously changed to SI metric
		Ru = 8.31447                #kJ/kmol*K  Universal Gas Constant
		g = 9.81                    #m/s2       Standard Acceleration of Gravity
		Patm = 101.325              #kPa        Standard Atmospheric Pressure
		sigmaSB = 5.6704*10**-8     #W/m2*K4    Stefan-Boltzmann Constant
		kSB = 1.380650*10**-23      #J/K        Boltzmann's Constant
		c0 = 2.9979*10**8           #m/s        Speed of Light in a Vacuume 
		c = 331.36                  #m/s        Speed of Sound in Dry Air
		hIF = 333.7                 #kJ/kg      Heat of Fusion of Water
		hFG = 2256.5                #kJ/kg      Enthalpy of Vaporization of Water
		return ({'Ru':Ru,'g':g,'Patm':Patm,'sigmaSB':sigmaSB,'kSB':kSB,'c0':c0,'c':c,'hIF':hIF,'hFG':hFG})

	def eqnDatabase(self):
		#A dictionary containing what each equation involves.
		#This will be used to plan an equation corse.
		return {
			'roeVA1': ['mdot1','roe','Velo1','A1'], 'roeVdot1': ['mdot1','roe','Vdot1'],
			'vRoe1': ['v1','roe'], 'hupv1': ['hi','u1','P1','v1'], 'pvrt1': ['P1','v1','R','T1'],
			'pvmrt1': ['P1','V1','m1','R','T1'],         
			'roeVA2': ['mdot2','roe','Velo2','A2'], 'roeVdot2': ['mdot2','roe','Vdot2'],
			'vRoe2': ['v2','roe'], 'hupv2': ['he','u2','P2','v2'], 'pvrt2': ['P2','v2','R','T2'],
			'pvmrt2': ['P2','V2','m2','R','T2'],
			'Tconst': ['T1','T2'], 'Pconst': ['P1','P2'], 'hconst': ['hi','he'], 'uconst':['u1','u2'], 'vconst':['v1','v2'],
			'Vconst': ['V1','V2'], 'mconst': ['m1','m2'], 'kcpcv': ['n','Cp','Cv'],
			'cpcvr': ['Cp','Cv','R'], 'deltaU': ['u2','u1','Cv','T2','T1'],
			'deltaH': ['he','hi','Cp','T2','T1'], 'deltaHIncom1': ['he','hi','Cp','v1','T2','T1','P2','P1'],
			'wbIntEqn': ['Wb','P1','V2','V1'], 'wbDeltaVEqn': ['Wb','P1','V2','V1'],
			'wbn': ['Wb','P2','P1','V2','V1','n'], 'wbnmr': ['Wb','T2','T1','m1','R','n'],
			'wbnm': ['Wb','P2','P1','v2','v1','m1','R','n'], 'wbn1v': ['Wb','P1','V2','V1'],
			'wbn1p': ['Wb','P2','P1','V1'], 'wbn1mrv': ['Wb','V2','V1','m1','R','T1'],
			'wbn1mrp': ['Wb','P2','P1','m1','R','T1'],
			'wbTotal': ['W','Wb','We','Ws'],
			'we': [], 'ws': [],
			'EnergyBalance': ['Q','W','mi','me','hi','he','ki_v','ke_v','pi_h','pe_h','m2','m1','u2','u1','k2_v','k1_v','p2_h','p1_h'],
			'effThWQh': ['effTh','W','Qh'], 'effThQhQl': ['effTh','Qh','Ql'],
			'effThWQhQl': ['W','Qh','Ql'], 'copHpWQh': ['copHp','Qh','W'],
			'copRefWQh': ['copRef','Ql','W'], 'copRefQhQl': ['copRef','Qh','Ql'],
			'copRefWQhQl': ['W','Qh','Ql'], 'copHpRef': ['copHp','copRef']
			}

	def roeVA1Eqn(self):
		"""mdot=roe*Velo*A"""
		return self.roe1*self.Velo1*self.A1-self.mdot1

	def roeVdot1Eqn(self):
		"""mdot=roe*Vdot"""
		return self.roe1*self.Vdot1-self.mdot1

	def vRoe1Eqn(self):
		"""roe = 1/v"""
		return 1/self.v1-self.roe1

	def hupv1Eqn(self):
		"""h=u+P*v"""
		return self.u1+self.P1*self.v1-self.h1

	##Ideal Gas Equations
	def pvrt1Eqn(self):
		"""Pv=RT"""
		return self.P1*self.v1-self.R1*self.T1

	def pvmrt1Eqn(self):
		"""PV=mRT"""
		return self.P1*self.V1-self.m1*self.R1*self.T1

	def roeVA2Eqn(self):
		"""mdot=roe*Velo*A"""
		return self.roe2*self.Velo2*self.A2-self.mdot2

	def roeVdot2Eqn(self):
		"""mdot=roe*Vdot"""
		return self.roe2*self.Vdot2-self.mdot2

	def vRoe2Eqn(self):
		"""roe = 1/v"""
		return 1/self.v2-self.roe2

	def hupv2Eqn(self):
		"""h=u+P*v"""
		return self.u2+self.P2*self.v2-self.h2

	##Ideal Gas Equations
	def pvrt2Eqn(self):
		"""Pv=RT"""
		return self.P2*self.v2-self.R2*self.T2

	def pvmrt2Eqn(self):
		"""PV=mRT"""
		return self.P2*self.V2-self.m2*self.R2*self.T2

	def TconstEqn(self):
		"""T1=T2"""
		return self.T1-self.T2

	def PconstEqn(self):
		"""P1=P2"""
		return self.P1-self.P2

	def hconstEqn(self):
		"""he=hi"""
		return self.he-self.hi

	def uconstEqn(self):
		"""u1=u2"""
		return self.u1-self.u2

	def vconstEqn(self):
		"""v1=v2"""
		return self.v1-self.v2

	def VconstEqn(self):
		"""V1=V2"""
		return self.V1-self.V2

	def mconstEqn(self):
		"""m1=m2"""
		return self.m1-self.m2

	def kcpcvEqn(self):
		"""k=Cp/Cv"""
		return self.k-self.Cp/self.Cv

	def cpcvrEqn(self):
		"""Cp=Cv+R"""
		return self.Cv+self.R-self.Cp

	def deltaUEqn(self):
		"""u2-u1=Cv*(T2-T1) if Cv is constant"""
		return self.Cv*(self.T2-self.T1)-(self.u2-self.u1)

	def deltaHEqn(self):
		"""h2-h1=Cp*(T2-T1) if Cp is constant"""
		return self.Cp*(self.T2-self.T1)-(self.h2-self.h1)

	##Incompressible Equations
	def deltaHIncomEqn(self):
		"""h2-h1=C*(T2-T1)+v*(P2-P1)"""
		return self.Cp*(self.T2-self.T1)+self.v1*(self.P2-self.P1)-(self.h2-self.h1)

	##Boundary Work Equations
	def wbIntEqn(self):
		"""Wb=Integral(P*dV,V1,V2)"""
		ans,err = integral.quad(self.P1,self.V1,self.V2)
		return ans-self.Wb

	def wbDeltaVEqn(self):
		"""Wb=P*(V2-V1)"""
		return self.P1*(self.V2-self.V1)-self.Wb

	###Ideal Gas Boundary Work Equations
	def wbnEqn(self):
		"""Wb=(P2*V2-P1*V1)/(1-n)"""
		return (self.P2*self.V2-self.P1*self.V1)/(1-self.n)-self.Wb

	def wbnmrEqn(self):
		"""Wb=m*R*(T2-T1)/(1-n)"""
		return self.m1*self.R*(self.T2-self.T1)/(1-self.n)-self.Wb

	def wbnmEqn(self):
		"""Wb = m*(P2*v2-P1*v1)/(1-n)"""
		return self.m1*(self.P2*self.v2-self.P1*self.v1)/(1-self.n)-self.Wb

	def wbn1vEqn(self):
		"""Wb=P1*V1*ln(V2/V1)"""
		return self.P1*self.V1*math.log(self.V2/self.V1)-self.Wb

	def wbn1pEqn(self):
		"""Wb=P1*V1*ln(P1/P2)"""
		return self.P1*self.V1*math.log(self.P1/self.P2)-self.Wb

	def wbn1mrvEqn(self):
		"""Wb = m*R*T*ln(V2/V1)"""
		return self.m1*self.R*self.T1*log(self.V2/self.V1)-self.Wb

	def wbn1mrpEqn(self):
		"""Wb = m*R*T*ln(P1/P2)"""
		return self.m1*R*T1*log(P1/P2)-Wb

	def wTotalEqn(self):
		"""W = Wb+Ws+We"""
		return self.Wb+self.Ws+self.We-self.W

	def weEqn(self):
		"""Not in Yet"""
		pass

	def wsEqn(self):
		"""Not in Yet"""
		pass

	##Energy Balance
	def EnergyBalanceEqn(self):
		"""Q-W+mi*(h+ke+pe)i-me*(h+ke+pe)e=m2*(u+ke+pe)2-m1*(u+ke+pe)1"""
		return self.Q-self.W+self.mi*(self.hi+self.ki+self.pi)-self.me*(self.he+self.ke+self.pe)-(self.m2*(self.u2+self.k2+self.p2)-self.m1*(self.u1+self.k1+self.p1))

	##Efficency
	def effThWQhEqn(self):
		"""effTh = W/Qh"""
		return self.W/self.Qh-self.effTh

	def effThQhQlEqn(self):
		"""effTh = (Qh-Ql)/Qh"""
		return (self.Qh-self.Ql)/self.Qh-self.effTh

	def effThWQhQlEqn(self):
		"""(Qh-Ql)/Qh = W/Qh"""
		return (self.Qh-self.Ql)/self.Qh-self.W/self.Qh

	def copHpWQhEqn(self):
		"""copHp = Qh/W"""
		return self.Qh/self.W-self.copHp

	def copHpQhQlEqn(self):
		"""copHp = 1-Ql/Qh"""
		return 1-self.Ql/self.Qh-self.copHp

	def copHpWQhQlEqn(self):
		"""Qh/W=1-Ql/Qh"""
		return 1-self.Ql/self.Qh-self.Qh/self.W

	def copRefWQhEqn(self):
		"""copRef = Qh/W"""
		return self.Ql/self.W-self.copRef

	def copRefQhQlEqn(self):
		"""copRef = 1-Ql/Qh"""
		return 1/(self.Qh/self.Ql-1)-self.copRef

	def copRefWQhQlEqn(self):
		"""Qh/W=1-Ql/Qh;"""
		return 1-self.Ql/self.Qh-self.Qh/self.W

	def copHpRefEqn(self):
		"""copHp=copRef+1"""
		return self.copRef+1-self.copHp