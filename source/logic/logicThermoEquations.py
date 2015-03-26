	
class LogicThermoEquations:
	"""
		This regulates all the Thermo Equations.
	"""
	def __init__(self,parent):
		#This is a list of all the equations that will be solved
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

	def eqnDatabase(self):
		#A dictionary containing what each equation involves.
		#This will be used to plan an equation corse.
		return {
		'roeVA': ['mdot','roe','Velo','A'], 'roeVdot': ['mdot','roe','Vdot'],
		'vRoe': ['v','roe'], 'hupv': ['h','u','P','v'], 'pvrt': ['P','v','R','T'],
		'pvmrt': ['P','V','m','R','T'], 'kcpcv': ['k','Cp','Cv'],
		'cpcvr': ['Cp','Cv','R'], 'deltaU': ['u2','u1','Cv','T2','T1'],
		'deltaH': ['h2','h1','Cp','T2','T1'], 'deltaHIncom': ['h2','h1','Cp','v','T2','T1','P2','P1'],
		'wbIntEqn': ['Wb','P','V2','V1'], 'wbDeltaVEqn': ['Wb','P','V2','V1'],
		'wbn': ['Wb','P2','P1','V2','V1','n'], 'wbnmr': ['Wb','T2','T1','m','R','n'],
		'wbnm': ['Wb','P2','P1','v2','v1','m','R','n'], 'wbn1v': ['Wb','P1','V2','V1'],
		'wbn1p': ['Wb','P2','P1','V1'], 'wbn1mrv': ['Wb','V2','V1','m','R','T'],
		'wbn1mrp': ['Wb','P2','P1','m','R','T'],
		'EnergyBalance': ['Q','W','mi','me','hi','he','ki_v','ke_v','pi_h','pe_h','m2','m1','u2','u1','k2_v','k1_v','p2_h','p1_h'],
		'effThWQh': ['effTh','W','Qh'], 'effThQhQl': ['effTh','Qh','Ql'],
		'effThWQhQl': ['W','Qh','Ql'], 'copHpWQh': ['copHp','Qh','W'],
		'copRefWQh': ['copRef','Ql','W'], 'copRefQhQl': ['copRef','Qh','Ql'],
		'copRefWQhQl': ['W','Qh','Ql'], 'copHpRef': ['copHp','copRef']
		}
		pass

	def roeVAEqn(x):
		"""mdot=roe*Velo*A; x is [mdot,roe,Velo,A]"""
		mdot,roe,Velo,A = x[0],x[1],x[2],x[3]
		return roe*Velo*A-mdot

	def roeVdotEqn(x):
		"""mdot=roe*Vdot; x is [mdot,roe,Vdot]"""
		mdot,roe,Vdot = [x0],x[1],x[2]
		return roe*Vdot-mdot

	def vRoeEqn(x):
		"""roe = 1/v; x is [v,roe]"""
		v, roe = x[0],x[1]
		return 1/v - roe

	def hupvEqn(x):
		"""h=u+P*v; x is [h,u,P,v]"""
		h,u,P,v = x[0],x[1],x[2],x[3]
		return u+P*v-h

	##Ideal Gas Equations
	def pvrtEqn(x):
		"""Pv=RT; x is [P,v,R,T]"""
		P,v,R,T = x[0],x[1],x[2],x[3]
		return P*v-R*T

	def pvmrtEqn(x):
		"""PV=mRT; x is [P,V,m,R,T]"""
		P,V,m,R,T = x[0],x[1],x[2],x[3],x[4]
		return P*V-m*R*T

	def kcpcvEqn(x):
		"""k=Cp/Cv; x is [k,Cp,Cv]"""
		k,Cp,Cv = x[0],x[1],x[2]
		return k-Cp/Cv

	def cpcvrEqn(x):
		"""Cp=Cv+R; x is [Cp,Cv,R]"""
		Cp,Cv,R = x[0],x[1],x[2]
		return Cv+R-Cp

	def deltaUEqn(x):
		"""u2-u1=Cv*(T2-T1) if Cv is constant; x is [u2,u1,Cv,T2,T1]"""
		u2,u1,Cv,T2,T1 = x[0],x[1],x[2],x[3],x[4]
		return Cv*(T2-T1)-(u2-u1)

	def deltaHEqn(x):
		"""h2-h1=Cp*(T2-T1) if Cp is constant; x is [h2,h1,Cp,T2,T1]"""
		h2,h1,Cp,T2,T1 = x[0],x[1],x[2],x[3],x[4]
		return Cp*(T2-T1)-(h2-h1)

	##Incompressible Equations
	def deltaHIncomEqn(x):
		"""h2-h1=C*(T2-T1)+v*(P2-P1); x is [h2,h1,Cp,T2,T1,v,P2,P1]"""
		h2,h1,Cp,T2,T1,v,P2,P1 = x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]
		return Cp*(T2-T1)+v*(P2-P1)-(h2-h1)

	##Boundary Work Equations
	def wbIntEqn(x):
		"""Wb=Integral(P*dV,V1,V2); x is [Wb,P,V2,V1]"""
		Wb,P,V2,V1 = x[0],x[1],x[2],x[3]
		ans,err = integral.quad(P,V1,V2)
		return ans-Wb

	def wbDeltaVEqn(x):
		"""Wb=P*(V2-V1); x is [Wb,P,V2,V1]"""
		Wb,P,V2,V1 = x[0],x[1],x[2],x[3]
		return P*(V2-V1)-Wb

	###Ideal Gas Boundary Work Equations
	def wbnEqn(x):
		"""Wb=(P2*V2-P1*V1)/(1-n); x is [Wb,P2,P1,V2,V1,n]"""
		Wb,P2,P1,V2,V1,n = x[0],x[1],x[2],x[3],x[4],x[5]
		return (P2*V2-P1*V1)/(1-n)-Wb

	def wbnmrEqn(x):
		"""Wb=m*R*(T2-T1)/(1-n); x is [Wb,T2,T1,m,R,n]"""
		Wb,T2,T1,m,R,n = x[0],x[1],x[2],x[3],x[4],x[5]
		return m*R*(T2-T1)/(1-n)-Wb

	def wbnmEqn(x):
		"""Wb = m*(P2*v2-P1*v1)/(1-n); x is [Wb,P2,P1,v2,v1,m,R,n]"""
		Wb,P2,P1,v2,v1,m,R,n = x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]
		return m*(P2*v2-P1*v1)/(1-n)-Wb

	def wbn1vEqn(x):
		"""Wb=P1*V1*ln(V2/V1); x is [Wb,P1,V2,V1]"""
		Wb,P1,V2,V1 = x[0],x[1],x[2],x[3]
		return P1*V1*math.log(V2/V1)-Wb

	def wbn1pEqgn(x):
		"""Wb=P1*V1*ln(P1/P2); x is [Wb,P2,P1,V1]"""
		Wb,P2,P1,V1 = x[0],x[1],x[2],x[3]
		return P1*V1*math.log(P1/P2)-Wb

	def wbn1mrvEqn(x):
		"""Wb = m*R*T*ln(V2/V1); x is [Wb,V2,V1,m,R,T]"""
		Wb,V2,V1,m,R,T = x[0],x[1],x[2],x[3],x[4],x[5]
		return m*R*T*log(V2/V1)-Wb

	def wbn1mrp(x):
		"""Wb = m*R*T*ln(P1/P2); x is [Wb,P2,P1,m,R,T]"""
		Wb,P2,P1,m,R,T = x[0],x[1],x[2],x[3],x[4],x[5]
		return m*R*T*log(P1/P2)-Wb

	##Energy Balance
	def EnergyBalance(x):
		"""Q-W+mi*(h+ke+pe)i-me*(h+ke+pe)e=m2*(u+ke+pe)2-m1*(u+ke+pe)1; x is [Q,W,mi,me,hi,he,ki,ke,pi,pe,m2,m1,u2,u1,k2,k1,p2,p1]"""
		Q,W,mi,me,hi,he,ki,ke,pi,pe,m2,m1,u2,u1,k2,k1,p2,p1 = x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16]
		return Q-W+mi*(hi+ki+pi)-me*(he+ke+pe)-(m2*(u2+k2+p2)-m1*(u1+k1+p1))

	##Efficency
	def effThWQh(x):
		"""effTh = W/Qh; x is [effTh,W,Qh]"""
		effTh,W,Qh = x[0],x[1],x[2]
		return W/Qh-effTh

	def effThQhQl(x):
		"""effTh = (Qh-Ql)/Qh; x is [effTh,Qh,Ql]"""
		effTh,Qh,Ql = x[0],x[1],x[2]
		return (Qh-Ql)/Qh-effTh

	def effThWQhQl(x):
		"""(Qh-Ql)/Qh = W/Qh; x is [W,Qh,Ql]"""
		W,Qh,Ql = x[0],x[1],x[2]
		return (Qh-Ql)/Qh-W/Qh

	def copHpWQh(x):
		"""copHp = Qh/W; x is [copHp,Qh,W]"""
		copHp,Qh,W = x[0],x[1],x[2]
		return Qh/W-copHp

	def copHpQhQl(x):
		"""copHp = 1-Ql/Qh; x is [copHp,Qh,Ql]"""
		copHp,Qh,Ql = x[0],x[1],x[2]
		return 1-Ql/Qh-copHp

	def copHpWQhQl(x):
		"""Qh/W=1-Ql/Qh; x is [W,Qh,Ql]"""
		W,Qh,Ql = x[0],x[1],x[2]
		return 1-Ql/Qh-Qh/W

	def copRefWQh(x):
		"""copRef = Qh/W; x is [copRef,Ql,W]"""
		copRef,Ql,W = x[0],x[1],x[2]
		return Ql/W-copRef

	def copRefQhQl(x):
		"""copRef = 1-Ql/Qh; x is [copRef,Qh,Ql]"""
		copRef,Qh,Ql = x[0],x[1],x[2]
		return 1/(Qh/Ql-1)-copRef

	def copRefWQhQl(x):
		"""Qh/W=1-Ql/Qh; x is [W,Qh,Ql]"""
		W,Qh,Ql = x[0],x[1],x[2]
		return 1-Ql/Qh-Qh/W

	def copHpRef(x):
		"""copHp=copRef+1; x is [copHp,copRef]"""
		copHp,copRef = x[0],x[1]
		return copRef+1-copHp