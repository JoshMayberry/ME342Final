from ..views import Frm_UnitConverter
#from .logicSubject import LogicSubject
from math import *

class LogicUnitConverter(Frm_UnitConverter):
	def __init__(self, parent):
		Frm_UnitConverter.__init__(self,parent)
		self.Type = 'Acceleration'
		self.ConvYes = False
		self.rounding = 13

	def onExpression( self, event ):
		#1001
		self.expression = self.FindWindowById(1001).GetLineText(0)
		self.answer = eval(self.expression)
		self.FindWindowById(1003).SetLabel(str(round(self.answer,self.rounding)))
		event.Skip()
	
	def onClear( self, event ):
		#1002
		self.expression = ' '
		self.answer = ' '
		self.FindWindowById(1001).SetLabel(self.expression)
		self.FindWindowById(1003).SetLabel(str(self.answer))
		self.FindWindowById(1005).SetLabel(str(self.answer2))
		event.Skip()
	
	def onConvFrom( self, event ):
		#1004
		n = self.FindWindowById(1004).GetSelection()
		self.convFrom = self.FindWindowById(1004).GetString(n)
		event.Skip()
	
	def onConvTo( self, event ):
		#1006
		n = self.FindWindowById(1006).GetSelection()
		self.convTo = self.FindWindowById(1006).GetString(n)
		event.Skip()
	
	def onType( self, event ):
		#1008
		n = self.FindWindowById(1008).GetSelection()
		self.Type = self.FindWindowById(1008).GetString(n)
		if self.convYes == True: self.updateLists()
		event.Skip()

	def onConvYes( self, event ):
		#1007
		if self.FindWindowById(1007).GetValue() == True:
			self.convYes = True
			self.updateLists()	
		else: self.ConvYes = False
		event.Skip()

	def onConvBtn( self, event ):
		if self.FindWindowById(1007).GetValue() == True:
			self.answer2 = self.convert(self.answer,self.convFrom,self.convTo,self.Type)
			self.FindWindowById(1005).SetLabel(str(round(self.answer2,self.rounding)))	
		event.Skip()

	def onBackToMain( self, event ):
		LogicSubject(self.parent).Show()
		#self.Destroy()
		event.Skip()

	def updateLists(self):
		#Updates the conversion lists.
		if self.Type == 'Acceleration': self.convFromList = ['cm/s^2','ft/s^2','g (standard gravity)','in/s^2','m/s^2','mm/s^2']
		elif self.Type == 'Angle': self.convFromList = ['degree','microRadian','minute','radian','second']
		elif self.Type == 'Area': self.convFromList = ['acre (US Survey ft)','barn','circular mil','cm^2','ft^2','in^2','km^2','m^2','mi^2','mm^2','yd^2']
		elif self.Type == 'Area Mom. of Inertia': self.convFromList = ['cm^4','ft^4','in^4','m^4','mm^4']
		elif self.Type == 'Computer Storage': self.convFromList = ['bit','byte','GB (gigabyte)','gigabit','KB (kilobyte)','kilobit','MB (megabyte)','megabit','TB (terabyte)','terabit']
		elif self.Type == 'Density': self.convFromList = ['grain/gallon (US)','g/cm^3','g/liter','g/mm^3','kg/cm^3','kg/liter','kg/m^3','kg/mm^3','lbm/ft^3','lbm/gal (UK)','lbm/gal (US)','lbm/in^3','lbm/yd^3','mg/cm^3','mg/liter','mg/mm^3','oz/ft^3','oz/gal (UK)','oz/gal (US)','oz/in^3','oz/yd^3','slug/ft^3','slug/gal (UK)','slug/gal (US)','slug/in^3','slug/yd^3','ton(2000 lbm)/ft^3','ton(2000 lbm)/gal (UK)','ton(2000 lbm)/gal (US)','ton(2000 lbm)/in^3','ton(2000 lbm)/yd^3']
		elif self.Type == 'Energy, Work or Heat': self.convFromList = ['BTU (international)','BTU (thermal)','cal (international)','cal (thermal)','ergs','eV','ft-lbf','hp-h','J','kcal (international)','kcal (thermal)','kJ','kW-h','kPa-m^3','m^2/s^2','MMBTU','mJ','MJ','psia-ft^3','quad (10^15 BTU IT.)','therm (Europe)','therm (US)','ton of TNT (equivalent)','W-h','N-m']
		elif self.Type == 'Energy/Mass': self.convFromList = ['BTU/lbm','cal/g','cal/kg','J/g','J/kg','kJ/kg','kJ/kmol']
		elif self.Type == 'Force': self.convFromList = ['dyne','kip (1000 lbf)','kgf (kilogram force)','kN (10^3 N)','lbf (Pound force)','N (Newtons)','kg-m/s^2','lbm-ft/s^2']
		elif self.Type == 'Force/Length': self.convFromList = ['dyne/cm','dyne/mm','kip/in','kip/ft','kN/cm','kN/m','kN/mm','lbf/in','lbf/ft','N/m','N/cm','N/mm','oz/in','oz/ft']
		elif self.Type == 'Heat Flux': self.convFromList = ['W/cm^2','W/m^2','BTU/h-ft^2']
		elif self.Type == 'Heat Transfer Coefficent': self.convFromList = ['W/m^2-C','W/m^2-K','BTU/h-ft^2-F','BTU/h-ft^2-R']
		elif self.Type == 'Length or Distance': self.convFromList = ['angstrom','astronomical unit','caliber','chain','chain, US survey','cm','cubit','fathom','fermi','ft','ft, US survey','furlong','in','km','leagues','light year','m','mi (mile)','mi, US survey','microinch','micron','mil (0.001 in)','mm','nm (nanometer)','nm (nautical mile)','parsec','rod','rod, US survey','yd (yard)']
		elif self.Type == 'Light Intensity': self.convFromList = ['footcandle','lumens/ft^2','lumens/in^2','lumens/cm^2','lux (lumens/m^2)','phots']
		elif self.Type == 'Mass': self.convFromList = ['carat, metric','grain (troy)','g','hundredweight, short','kg','lbf-s^2/in','lbm (pound)','mg','oz','pennyweight','slug (lbf-s^2/ft)','ton, long (2240 lbm)','ton, metric (tonne)','ton, short (2000 lbm)']
		elif self.Type == 'Mass Flow Rate': self.convFromList = ['/h','g/min','g/s','kg/h','kg/min','kg/s','lbm/h','lbm/min','lbm/s','oz/h','oz/min','oz/s','slug/h','slug/min','slug/s','ton(2000 lbm)/h','ton(2000 lbm)/min','ton(2000 lbm)/s']
		elif self.Type == 'Mass Mom. of Inertia': self.convFromList = ['kg-m^2','lbm-in^2','lbm-ft^2','slug-ft^2']
		elif self.Type == 'Mass/Area': self.convFromList = ['g/cm^2','g/m^2','g/mm^2','kg/cm^2','kg/m^2','kg/mm^2','lbm/ft^2','lbm/in^2','lbm/yd^2','oz/ft^2','oz/in^2','oz/yd^2','slug/ft^2','slug/in^2','slug/yd^2','ton(2000 lbm)/ft^2','ton(2000 lbm)/in^2','ton(2000 lbm)/yd^2']
		elif self.Type == 'Mass/Length': self.convFromList = ['denier','g/cm','g/m','g/mm','kg/cm','kg/m','kg/mm','lbm/ft','lbm/in','lbm/yd','oz/ft','oz/in','oz/yd','slug/ft','slug/in','slug/yd','tex','ton(2000 lbm)/ft','ton(2000 lbm)/in','ton(2000 lbm)/yd']
		elif self.Type == 'Power or Energy/Time': self.convFromList = ['BTU/h','BTU/min','BTU/s','cal/h','cal/min','cal/s','erg/h','erg/min','erg/s','ft-lbf/h','ft-lbf/min','ft-lbf/s','hp (horsepower)','hp (boiler hp)','J/h','J/min','J/s','kcal/h','kcal/min','kcal/s','kW (kiloWatt)','tons of refrig.','W (Watt)']
		elif self.Type == 'Pressure or Stress': self.convFromList = ['atmosphere','bar','cm Hg (0 C)','cm water (4 C)','dyne/cm^2','ft Hg (32 F)','ft Hg (60 F)','ft water (39.2 F)','ft water (60 F)','GPa','inch Hg (32 F)','inch Hg (60 F)','inch water (39.2 F)','inch water (60 F)','kgf/cm^2','kgf/m^2','kgf/mm^2','kPa','ksi (1000 psi)','lbf/ft^2','mbar (millibar)','mm Hg (0 C)','mm water (4 C)','MPa','Pa (Pascal)','psi (lbf/in^2)','psia','torr']
		elif self.Type == 'Specific Heat': self.convFromList = ['BTU/(lbm-F)','cal/(g-C)','cal/(kg-C)','kcal/(g-C)','kcal/(kg-C)','kJ/(kg-K)','kJ/(kg-K)','kJ/(kmol-C)','kJ/(kmol-K)','J/(kg-K)','J/(g-C)','J/(g-K)']
		elif self.Type == 'Specific Volume': self.convFromList = ['cm^3/g','ft^3/lbm','liter/kg','m^3/kg']
		elif self.Type == 'Stress Intensity': self.convFromList = ['kPa-m^(0.5)','ksi-in^(0.5)','MPa-m^(0.5)','psi-in^(0.5)','Pa-m^(0.5)']
		elif self.Type == 'Temperature': self.convFromList = ['Centigrade (C)','Fahrenheit (F)','Kelvin (K)','Rankine (R)','Delise (De)','Newton (N)','Reaumur (Re)','Romer (Ro)']
		elif self.Type == 'Thermal Conductance': self.convFromList = ['BTU/(ft^2-h-F)','BTU/(ft^2-s-F)','cal/(cm^2-h-C)','cal/(cm^2-s-C)','W/(m^2-K)']
		elif self.Type == 'Thermal Conductivity': self.convFromList = ['BTU/(ft-h-F)','BTU/(ft-h-R)','BTU/(ft-s-F)','cal/(cm-h-C)','cal/(cm-s-C)','W/(m-K)']
		elif self.Type == 'Time': self.convFromList = ['d (day)','day (sidereal)','h (hour)','hour (sidereal)','microsecond','min (minutes)','minutes (sidereal)','ms (milisecond)','ns (nanosecond)','s (seconds)','seconds (sidereal)','week','year (365 days)','year (sidereal)']
		elif self.Type == 'Torque or Moment': self.convFromList = ['dyne-mm','dyne-cm','kip-ft','kip-in','lbf-ft','lbf-in','ozf-ft','ozf-in','N-cm','N-m','N-mm']
		elif self.Type == 'Velocity or Speed': self.convFromList = ['cm/h','cm/min','cm/s','ft/h','ft/min','ft/s','in/h','in/min','in/s','km/h','km/min','km/s','knots (naut. mi/h)','m/h','m/min','m/s','miles/h','miles/min','miles/s','mm/h','mm/min','mm/s']
		elif self.Type == 'Viscosity, Dynamic': self.convFromList = ['centipoise','lbf-h/in^2','lbf-s/ft^2','lbf-s/in^2','lbm/(ft-s)','lbm/(ft-h)','Pa-S (Pascal-second)','poise','slug/(ft-s)']
		elif self.Type == 'Viscosity, Kinematic': self.convFromList = ['centistokes','ft^2/s','in^2/s','m^2/s','stokes']
		elif self.Type == 'Volume': self.convFromList = ['acre-ft (US Survey ft)','acre-in (US Survey ft)','barrel (42 US gal)','bushel (US dry)','cc (cm^3)','cord (128 ft^3)','cup (US liquid)','fl oz (US fluid oz)','ft^3','gallon (US dry)','gallon (US liquid)','gallon (UK & Can.)','in^3','liter','m^3','mi^3','ml (mililiter)','mm^3 (cubic mm)','peck (US dry)','pint (US liquid)','pint (US dry)','quart (US liquid)','quart (US dry)','tablespoon','teaspoon','yd^3']
		elif self.Type == 'Volume Flow Rate': self.convFromList = ['acre-ft/h (US Survey fit)','acre-ft/min (US Survey)','barrel/h (42 gal)','barrel/min (42 gal)','cm^3/h','cm^3/min','cm^3/s','ft^3/h','ft^3/min','ft^3/s','gallon/h (US liquid)','gallon/min (US liquid)','gallon/s (US liquid)','in^3/h','in^3/min','in^3/s','liter/h','liter/min','liter/s','m^3/h','m^3/min','m^3/s','mm^3/h','mm^3/min','mm^3/s','quart/h (US liquid)','quart/min (US liquid)','quart/s (US liquid)','yd^3/h','yd^3/min','yd^3/s']
		else: self.convFromList = []
		self.convToList = self.convFromList[:]
		self.FindWindowById(1004).SetItems(self.convToList)
		self.FindWindowById(1004).SetSelection(0)
		n = self.FindWindowById(1004).GetSelection()
		self.convTo = self.FindWindowById(1004).GetString(n)

		self.FindWindowById(1006).SetItems(self.convToList)
		self.FindWindowById(1006).SetSelection(0)
		n = self.FindWindowById(1006).GetSelection()
		self.convFrom = self.FindWindowById(1006).GetString(n)

	def convert(self,x,unitForm,unitTo,unitType):
		"""
			'x' is what must be converted
			'unitForm' is the unit which self.answer is in.
			'unitTo' is the unit which self.answer2 is in.
			'unitType' is the type of units
			'y' is the SI form of x

			First, the unitFrom is converted to SI units, and then to the unitTo.

			Note: Make a sub program that can figure out the units that involuve kmol. It needs to find the molecular weights.
		"""
		#x = eval(x)
		print('Converting...')

		#print('x',x)
		#print('unitForm',unitForm)
		#print('unitTo',unitTo)
		#print('unitType',unitType)

		if unitType != 'Temperature':
			for i in range(2):
				if unitType == 'Acceleration': #m/s^2
					if unitForm == 'cm/s^2': y = x*0.01
					elif unitForm == 'ft/s^2': y = x*0.3048
					elif unitForm == 'g (standard gravity)': y = x*9.80665
					elif unitForm == 'in/s^2': y = x*0.0254
					elif unitForm == 'km/s^2': y = x*1000
					elif unitForm == 'm/s^2': y = x*1
					elif unitForm == 'mm/s^2': y = x*0.001
					else: print('Error in',unitType)

				elif unitType == 'Angle': #radian
					if unitForm == 'degree': y = x*0.0174532925199433
					elif unitForm == 'microRadian': y = x*0.1*10**-5
					elif unitForm == 'minute': y = x*0.000290888208665722
					elif unitForm == 'radian': y = x*0.48481368110954*10**-5
					else: print('Error in',unitType)

				elif unitType == 'Area': #m^2
					if unitForm == 'acre (US Survey ft)': y = x*4046.8726098743
					elif unitForm == 'barn': y = x*0.1*10**-27
					elif unitForm == 'circular mil': y = x*0.50670747909750*10**-9
					elif unitForm == 'cm^2': y = x*0.0001
					elif unitForm == 'ft^2': y = x*0.09290304
					elif unitForm == 'in^2': y = x*0.00064516
					elif unitForm == 'km^2': y = x*1000000
					elif unitForm == 'm^2': y = x*1
					elif unitForm == 'mi^2': y = x*2589988.110336
					elif unitForm == 'mm^2': y = x*0.1*10**-5
					elif unitForm == 'yd^2': y = x*0.83612736
					else: print('Error in',unitType)

				elif unitType == 'Area Mom. of Inertia': #m^4
					if unitForm == 'cm^4': y = x*0.1*10**-7
					elif unitForm == 'ft^4': y = x*0.0086309748412416
					elif unitForm == 'in^4': y = x*0.41623142560000*10**-6
					elif unitForm == 'm^4': y = x*1
					elif unitForm == 'mm^4': y = x*0.1*10**-11
					else: print('Error in',unitType)

				elif unitType == 'Computer Storage': #KB
					if unitForm == 'bit': y = x*0.0001220703125
					elif unitForm == 'byte': y = x*0.0009765625
					elif unitForm == 'GB (gigabyte)': y = x*1048576
					elif unitForm == 'gigabit': y = x*131072
					elif unitForm == 'KB (kilobyte)': y = x*1
					elif unitForm == 'kilobit': y = x*0.125
					elif unitForm == 'MB (megabyte)': y = x*1024
					elif unitForm == 'megabit': y = x*128
					elif unitForm == 'TB (terabyte)': y = x*1073741824
					elif unitForm == 'terabit': y = x*134217728
					else: print('Error in',unitType)

				elif unitType  == 'Density': #kg/m^3
					if unitForm == 'grain/gallon (US)': y = x*0.017118061045271
					elif unitForm == 'g/cm^3': y = x*1000
					elif unitForm == 'g/liter': y = x*1
					elif unitForm == 'g/mm^3': y = x*1000000
					elif unitForm == 'kg/cm^3': y = x*1000000
					elif unitForm == 'kg/liter': y = x*1000
					elif unitForm == 'kg/m^3': y = x*1
					elif unitForm == 'kg/mm^3': y = x*1000000000
					elif unitForm == 'lbm/ft^3': y = x*16.01846337396
					elif unitForm == 'lbm/gal (UK)': y = x*99.776372663102
					elif unitForm == 'lbm/gal (US)': y = x*119.8264273169
					elif unitForm == 'lbm/in^3': y = x*27679.904710203
					elif unitForm == 'lbm/yd^3': y = x*0.593276421257783
					elif unitForm == 'mg/cm^3': y = x*1
					elif unitForm == 'mg/liter': y = x*0.000999999997475243
					elif unitForm == 'mg/mm^3': y = x*1000
					elif unitForm == 'oz/ft^3': y = x*1.0011539608725
					elif unitForm == 'oz/gal (UK)': y = x*6.2360232914439
					elif unitForm == 'oz/gal (US)': y = x*7.489151707306
					elif unitForm == 'oz/in^3': y = x*1729.9940443877
					elif unitForm == 'oz/yd^3': y = x*0.0370797763286114
					elif unitForm == 'slug/ft^3': y = x*515.3788183932
					elif unitForm == 'slug/gal (UK)': y = x*3210.2098588471
					elif unitForm == 'slug/gal (US)': y = x*3855.3012908374
					elif unitForm == 'slug/in^3': y = x*890574.59818344
					elif unitForm == 'slug/yd^3': y = x*19.088104384933
					elif unitForm == 'ton(2000 lbm)/ft^3': y = x*32036.92674792
					elif unitForm == 'ton(2000 lbm)/gal (UK)': y = x*199552.7453262
					elif unitForm == 'ton(2000 lbm)/gal (US)': y = x*239652.85463379
					elif unitForm == 'ton(2000 lbm)/in^3': y = x*55359809.420406
					elif unitForm == 'ton(2000 lbm)/yd^3': y = x*1186.5528425156
					else: print('Error in',unitType)

				elif unitType == 'Energy, Work or Heat': #J
					if unitForm == 'BTU (international)': y = x*1055.05585262
					elif unitForm == 'BTU (thermal)': y = x*1054.3502644889
					elif unitForm == 'cal (international)': y = x*4.1868
					elif unitForm == 'cal (thermal)': y = x*4.184
					elif unitForm == 'ergs': y = x*0.1*10**-6
					elif unitForm == 'eV': y = x*0.16021770000000*10**-18
					elif unitForm == 'ft-lbf': y = x*1.3558179483314
					elif unitForm == 'hp-h': y = x*2684519.5376962
					elif unitForm == 'J (Joule)': y = x*1
					elif unitForm == 'kcal (international)': y = x*4186.8
					elif unitForm == 'kcal (thermal)': y = x*4184
					elif unitForm == 'kJ': y = x*1000
					elif unitForm == 'kW-h': y = x*3600000
					elif unitForm == 'kPa-m^3': y = x*1
					#elif unitForm == 'm^2/s^2': y = x* #Specific Energy. Make a sub section for this.
					elif unitForm == 'MMBTU': y = x*1055055852.62
					elif unitForm == 'mJ': y = x*0.001
					elif unitForm == 'MJ': y = x*1000000
					elif unitForm == 'psia-ft^3': y = x*195.23792781206
					elif unitForm == 'quad (10^15 BTU IT.)': y = x*0.10550558526200*10**19
					elif unitForm == 'therm (Europe)': y = x*105506000
					elif unitForm == 'therm (US)': y = x*105480400
					elif unitForm == 'ton of TNT (equivalent)': y = x*4184000000
					elif unitForm == 'W-h': y = x*3600
					elif unitForm == 'N-m': y = x*1
					else: print('Error in',unitType)

				elif unitType == 'Energy/Mass': #J/kg
					if unitForm == 'BTU/lbm': y = x*2326
					elif unitForm == 'cal/g': y = x*4184
					elif unitForm == 'cal/kg': y = x*4184000
					elif unitForm == 'J/g': y = x*1000
					elif unitForm == 'J/kg': y = x*1
					elif unitForm == 'kJ/kg': y = x*1000
					#elif unitForm == 'kJ/kmol': y = x*
					else: print('Error in',unitType)

				elif unitType == 'Force': #N
					if unitForm == 'dyne': y = x*0.1*10**-4
					elif unitForm == 'kip (1000 lbf)': y = x*4448.2216152605
					elif unitForm == 'kgf (kilogram force)': y = x*9.80665
					elif unitForm == 'kN': y = x*1000
					elif unitForm == 'lbf (Pound force)': y = x*4.4482216152605
					elif unitForm == 'N (Newtons)': y = x*1
					elif unitForm == 'kg-m/s^2': y = x*1
					elif unitForm == 'lbm-ft/s^2': y = x*4.44822
					else: print('Error in',unitType)

				elif unitType == 'Force/Length': #N/m
					if unitForm == 'dyne/cm': y = x*0.001
					elif unitForm == 'dyne/mm': y = x*0.01
					elif unitForm == 'kip/in': y = x*175126.83524648
					elif unitForm == 'kip/ft': y = x*14593.902937206
					elif unitForm == 'kN/cm': y = x*100000
					elif unitForm == 'kN/m': y = x*1000
					elif unitForm == 'kN/mm': y = x*1000000
					elif unitForm == 'lbf/in': y = x*175.12683524648
					elif unitForm == 'lbf/ft': y = x*14.593902937206
					elif unitForm == 'N/m': y = x*1
					elif unitForm == 'N/cm': y = x*100
					elif unitForm == 'N/mm': y = x*1000
					elif unitForm == 'oz/in': y = x*10.945427202905
					elif unitForm == 'oz/ft': y = x*0.912118933575398
					else: print('Error in',unitType)

				elif unitType == 'Heat Flux': #W/m^2
					if unitForm == 'W/cm^2': y = x*10**4
					elif unitForm == 'W/m^2': y = x*1
					elif unitForm == 'BTU/h-ft^2': y = x*0.3171

				elif unitType == 'Heat Generation Rate': #W/m^3
					if unitForm == 'W/cm^3': y = x*10**6
					elif unitForm == 'W/m^3': y = x*1
					elif unitForm == 'BTU/h-ft^3': y = x*0.09665

				elif unitType == 'Heat Transfer Coefficent': #W/m^2-K
					if unitForm == 'W/m^2-C': y = x*1
					elif unitForm == 'W/m^2-K': y = x*1
					elif unitForm == 'BTU/h-ft^2-F': y = x*0.17612
					elif unitForm == 'BTU/h-ft^2-R': y = x*0.17612 #is this right?

				elif unitType == 'Length or Distance': #m
					if unitForm == 'angstrom': y = x*0.1*10**-9
					elif unitForm == 'astronomical unit': y = x*149597900000
					elif unitForm == 'caliber': y = x*0.000254
					elif unitForm == 'chain': y = x*20.1168
					elif unitForm == 'chain, US survey': y = x*20.11684023368
					elif unitForm == 'cm': y = x*0.01
					elif unitForm == 'fathom': y = x*1.8288
					elif unitForm == 'fermi': y = x*0.1*10**-14
					elif unitForm == 'ft': y = x*0.3048
					elif unitForm == 'ft, US survey': y = x*0.304800609601219
					elif unitForm == 'furlong': y = x*201.168
					elif unitForm == 'in': y = x*0.0254
					elif unitForm == 'km': y = x*1000
					elif unitForm == 'leagues': y = x*5556
					elif unitForm == 'light year': y = x*0.946073*10**16
					elif unitForm == 'm': y = x*1
					elif unitForm == 'mi (mile)': y = x*1609.344
					elif unitForm == 'mi, US survey': y = x*1609.3472186944
					elif unitForm == 'microinch': y = x*0.254*10**-7
					elif unitForm == 'micron': y = x*0.1*10**-5
					elif unitForm == 'mil (0.001 in)': y = x*0.254*10**-7
					elif unitForm == 'mm': y = x*0.001
					elif unitForm == 'nm (nanometer)': y = x*0.000001
					elif unitForm == 'nm (nautical mile)': y = x*1852
					elif unitForm == 'parsec': y = x*0.3085678*10**17
					elif unitForm == 'rod': y = x*5.0292
					elif unitForm == 'rod, US survey': y = x*5.0292100584201
					elif unitForm == 'yd (yard)': y = x*0.9144
					else: print('Error in',unitType)

				elif unitType == 'Light Intensity': #lumens/m^2
					if unitForm == 'footcandle': y = x*10.76391041671
					elif unitForm == 'lumens/ft^2': y = x*10.76391041671
					elif unitForm == 'lumens/in^2': y = x*0.0747493778938175
					elif unitForm == 'lumens/cm^2': y = x*10000
					elif unitForm == 'lux (lumens/m^2)': y = x*1
					elif unitForm == 'phots': y = x*10000
					else: print('Error in',unitType)

				elif unitType == 'Mass': #kg 
					if unitForm == 'carat, metric': y = x*0.0002
					elif unitForm == 'grain (troy)': y = x*0.6479891*10**-4
					elif unitForm == 'g': y = x*0.001
					elif unitForm == 'hundredweight, short': y = x*45.359237
					elif unitForm == 'kg': y = x*1
					elif unitForm == 'lbf-s^2/in': y = x*175.12683524648
					elif unitForm == 'lbm (pound)': y = x*0.45359237
					elif unitForm == 'mg': y = x*0.1*10**-5
					elif unitForm == 'oz': y = x*0.028349523125
					elif unitForm == 'pennyweight': y = x*0.00155517384
					elif unitForm == 'slug (lbf-s^2/ft)': y = x*14.593902937206
					elif unitForm == 'ton, long, (2240 lbm)': y = x*1016.0469088
					elif unitForm == 'ton, metric (tonne)': y = x*1000
					elif unitForm == 'ton, short (2000 lbm)': y = x*907.18474
					else: print('Error in',unitType)
				
				elif unitType == 'Mass Flow Rate': #kg/s
					if unitForm == 'g/h': y = x*0.27777777777778*10**-6
					elif unitForm == 'g/min': y = x*0.16666666666667*10**-4
					elif unitForm == 'g/s': y = x*0.001
					elif unitForm == 'kg/h': y = x*0.000277777777777778
					elif unitForm == 'kg/min': y = x*0.0166666666666667
					elif unitForm == 'kg/s': y = x*1
					elif unitForm == 'lbm/h': y = x*0.000125997880555556
					elif unitForm == 'lbm/min': y = x*0.00755987283333333
					elif unitForm == 'lbm/s': y = x*0.45359237
					elif unitForm == 'oz/h': y = x*0.78748675347222*10**-5
					elif unitForm == 'oz/min': y = x*0.000472492052083333
					elif unitForm == 'oz/s': y = x*0.028349523125
					elif unitForm == 'slug/h': y = x*0.00405386192700177
					elif unitForm == 'slug/min': y = x*0.243231715620106
					elif unitForm == 'slug/s': y = x*14.593902937206
					elif unitForm == 'ton(2000 lbm)/h': y = x*0.251995761111111
					elif unitForm == 'ton(2000 lbm)/min': y = x*15.119745666667
					elif unitForm == 'ton(2000 lbm)/s': y = x*907.18474
					else: print('Error in',unitType)

				elif unitType == 'Mass Mom. of Inertia': #kg-m^2
					if unitForm == 'kg-m^2': y = x*1
					elif unitForm == 'lbm-in^2': y = x*0.0002926396534292
					elif unitForm == 'lbm-ft^2': y = x*0.0421401100938048
					elif unitForm == 'slug-ft^2': y = x*1.3558179483314
					else: print('Error in',unitType)

				elif unitType == 'Mass/Area': #kg/m^2
					if unitForm == 'g/cm^2': y = x*10
					elif unitForm == 'g/m^2': y = x*0.001
					elif unitForm == 'g/mm^2': y = x*1000
					elif unitForm == 'kg/cm^2': y = x*10000
					elif unitForm == 'kg/m^2': y = x*1
					elif unitForm == 'kg/mm^2': y = x*1000000
					elif unitForm == 'lbm/ft^2': y = x*4.8824276363831
					elif unitForm == 'lbm/in^2': y = x*703.06957963916
					elif unitForm == 'lbm/yd^2': y = x*0.542491959598117
					elif unitForm == 'oz/ft^2': y = x*0.305151727273941
					elif unitForm == 'oz/in^2': y = x*43.941848727447
					elif unitForm == 'oz/yd^2': y = x*0.0339057474748823
					elif unitForm == 'slug/ft^2': y = x*157.08746384625
					elif unitForm == 'slug/in^2': y = x*22620.594793859
					elif unitForm == 'slug/yd^2': y = x*17.454162649583
					elif unitForm == 'ton(2000 lbm)/ft^2': y = x*9764.8552727661
					elif unitForm == 'ton(2000 lbm)/in^2': y = x*1406139.1592783
					elif unitForm == 'ton(2000 lbm)/yd^2': y = x*1084.9839191962
					else: print('Error in',unitType)

				elif unitType == 'Mass/Length': #'kg/m'
					if unitForm == 'denier': y = x*0.11111111111111*10**-6
					elif unitForm == 'g/cm': y = x*0.1
					elif unitForm == 'g/m': y = x*0.001
					elif unitForm == 'g/mm': y = x*1
					elif unitForm == 'kg/cm': y = x*100
					elif unitForm == 'kg/m': y = x*1
					elif unitForm == 'kg/mm': y = x*1000
					elif unitForm == 'lbm/ft': y = x*1.4881639435696
					elif unitForm == 'lbm/in': y = x*17.857967322835
					elif unitForm == 'lbm/yd': y = x*0.496054647856518
					elif unitForm == 'oz/ft': y = x*0.0930102464730971
					elif unitForm == 'oz/in': y = x*1.1161229576772
					elif unitForm == 'oz/yd': y = x*0.0310034154910324
					elif unitForm == 'slug/ft': y = x*47.880258980336
					elif unitForm == 'slug/in': y = x*574.56310776403
					elif unitForm == 'slug/yd': y = x*15.960086326779
					elif unitForm == 'tex': y = x*0.99999999747524*10**-6
					elif unitForm == 'ton(2000 lbm)/ft': y = x*2976.3278871391
					elif unitForm == 'ton(2000 lbm)/in': y = x*35715.934645669
					elif unitForm == 'ton(2000 lbm)/yd': y = x*992.10929571304
					else: print('Error in',unitType)

				elif unitType == 'Power or Energy/Time': #W
					if unitForm == 'BTU/h': y = x*0.293071070172222
					elif unitForm == 'BTU/min': y = x*17.584264210333
					elif unitForm == 'BTU/s': y = x*1055.05585262
					elif unitForm == 'cal/h': y = x*0.00116222222222222
					elif unitForm == 'cal/min': y = x*0.0697333333333333
					elif unitForm == 'cal/s': y = x*4.184
					elif unitForm == 'erg/h': y = x*0.27777777777778*10**-1
					elif unitForm == 'erg/min': y = x*0.16666666666667*10**-8
					elif unitForm == 'erg/s': y = x*0.1*10**-6
					elif unitForm == 'ft-lbf/h': y = x*0.000376616096758722
					elif unitForm == 'ft-lbf/min': y = x*0.0225969658055233
					elif unitForm == 'ft-lbf/s': y = x*1.3558179483314
					elif unitForm == 'hp (horsepower)': y = x*745.69987158227
					elif unitForm == 'hp (boiler hp)': y = x*9809.5
					elif unitForm == 'J/h': y = x*0.000277777777777778
					elif unitForm == 'J/min': y = x*0.0166666666666667
					elif unitForm == 'J/s': y = x*1
					elif unitForm == 'kcal/h': y = x*1.1622222222222
					elif unitForm == 'kcal/min': y = x*69.733333333333
					elif unitForm == 'kcal/s': y = x*4184
					elif unitForm == 'kW (kiloWatt)': y = x*1000		
					elif unitForm == 'tons of refrig.': y = x*3516.8528420667
					elif unitForm == 'W (Watt)': y = x*1
					else: print('Error in',unitType)

				elif unitType == 'Pressure or Stress': #kPa
					if unitForm == 'atmosphere': y = x*101.325
					elif unitForm == 'bar': y = x*100
					elif unitForm == 'cm Hg (0 C)': y = x*1.333224
					elif unitForm == 'cm water (4 C)': y = x*0.0980665
					elif unitForm == 'dyne/cm^2': y = x*0.0001
					elif unitForm == 'ft Hg (32 F)': y = x*40.636668
					elif unitForm == 'ft Hg (60 F)': y = x*40.5222
					elif unitForm == 'ft water (39.2 F)': y = x*2.988984
					elif unitForm == 'ft water (60 F)': y = x*2.98608
					elif unitForm == 'GPa': y = x*1000000
					elif unitForm == 'inch Hg (32 F)': y = x*3.386389
					elif unitForm == 'inch Hg (60 F)': y = x*3.37685
					elif unitForm == 'inch water (39.2 F)': y = x*0.249082
					elif unitForm == 'inch water (60 F)': y = x*0.24884
					elif unitForm == 'kgf/cm^2': y = x*98.0665
					elif unitForm == 'kgf/m^2': y = x*0.00980665
					elif unitForm == 'kgf/mm^2': y = x*9806.65
					elif unitForm == 'kPa': y = x*1
					elif unitForm == 'ksi (1000 psi)': y = x*6894.7572931684
					elif unitForm == 'lbf/ft^2': y = x*0.0478802589803358
					elif unitForm == 'mbar (millibar)': y = x*0.1
					elif unitForm == 'mm Hg (0 C)': y = x*0.1333224
					elif unitForm == 'mm water (4 C)': y = x*0.00980665
					elif unitForm == 'MPa': y = x*1000
					elif unitForm == 'Pa (Pascal)': y = x*0.001
					elif unitForm == 'psi (lbf/in^2)': y = x*6.8947572931684
					elif unitForm == 'psia': y = x*6.8947572931684
					elif unitForm == 'torr': y = x*0.1333224
					else: print('Error in',unitType)

				elif unitType == 'Specific Heat': #J/(Kg-K)
					if unitForm == 'BTU/(lbm-F)': y = x*4186.8
					elif unitForm == 'BTU/(lbm-R)': y = x*4186.8
					#elif unitForm == 'BTU/(lbmol-F)': y = x*
					#elif unitForm == 'BTU/(lbmol-R)': y = x*
					elif unitForm == 'cal/(g-C)': y = x*4184
					elif unitForm == 'cal/(kg-C)': y = x*4.184
					elif unitForm == 'kcal/(g-C)': y = x*4184000
					elif unitForm == 'kcal/(kg-C)': y = x*4184
					elif unitForm == 'kJ/(kg-C)': y = x*1000
					elif unitForm == 'kJ/(kg-K)': y = x*1000
					#elif unitForm == 'kJ/(kmol-C)': y = x*
					#elif unitForm == 'kJ/(kmol-K)': y = x*
					elif unitForm == 'J/(kg-K)': y = x*1
					elif unitForm == 'J/(g-C)': y = x*1000
					elif unitForm == 'J/(g-K)': y = x*1000
					else: print('Error in',unitType)

				elif unitType == 'Specific Volume': #m^3/kg
					if unitForm == 'm^3/kg': y = x*1
					elif unitForm == 'liter/kgl': y = x*1000
					elif unitForm == 'cm^3/g': y = x*1000
					elif unitForm == 'ft^3/lbm': y = x*0.062428

				elif unitType == 'Stress Intensity': #kPa-m^(0.5)
					if unitForm == 'kPa-m^(0.5)': y = x*1
					elif unitForm == 'ksi-in^(0.5)': y = x*1098.8434941088
					elif unitForm == 'MPa-m^(0.5)': y = x*1000
					elif unitForm == 'psi-in^(0.5)': y = x*1.0988434941088
					elif unitForm == 'Pa-m^(0.5)': y = x*0.001
					else: print('Error in',unitType)

				elif unitType == 'Thermal Conductance': #W/(m^2-K)
					if unitForm == 'BTU/(ft^2-h-F)': y = x*5.6782633411135
					elif unitForm == 'BTU/(ft^2-s-F)': y = x*20441.748028009
					elif unitForm == 'cal/(cm^2-h-C)': y = x*11.622222222222
					elif unitForm == 'cal/(cm^2-s-C)': y = x*41840
					elif unitForm == 'W/(m^2-K)': y = x*1
					else: print('Error in',unitType)

				elif unitType == 'Thermal Conductivity': #W/(m-K)
					if unitForm == 'BTU-in/(ft^2-h-F)': y = x*0.144227888864283
					elif unitForm == 'BTU-in/(ft^2-s-F)': y = x*519.22039991142
					elif unitForm == 'BTU/(ft-h-F)': y = x*1.7307346663714
					elif unitForm == 'BTU/(ft-s-F)': y = x*6230.644798937
					elif unitForm == 'cal/(cm-h-C)': y = x*0.116222222222222
					elif unitForm == 'cal/(cm-s-C)': y = x*418.4		
					elif unitForm == 'W/(m-K)': y = x*1
					else: print('Error in',unitType)

				elif unitType == 'Time': #s
					if unitForm == 'd (day)': y = x*86400
					elif unitForm == 'day (sidereal)': y = x*86339.359018964
					elif unitForm == 'h (hour)': y = x*3600
					elif unitForm == 'hour (sidereal)': y = x*3597.4732924568
					elif unitForm == 'microsecond': y = x*0.1*10**-5
					elif unitForm == 'min (minutes)': y = x*60
					elif unitForm == 'minutes (sidereal)': y = x*59.957888207614
					elif unitForm == 'ms (milisecond)': y = x*0.001
					elif unitForm == 'nanosecond': y = x*0.1*10**-8
					elif unitForm == 's (Seconds)': y = x*1
					elif unitForm == 'seconds (sidereal)': y = x*0.999298136793566
					elif unitForm == 'week': y = x*604800
					elif unitForm == 'year (365 days)': y = x*31536000
					elif unitForm == 'year (sidereal)': y = x*31558149.504
					else: print('Error in',unitType)

				elif unitType == 'Torque or Moment': #N-m
					if unitForm == 'dyne-mm': y = x*0.1*10**-7
					elif unitForm == 'dyne-cm': y = x*0.1*10**-6
					elif unitForm == 'kip-ft': y = x*1355.8179483314
					elif unitForm == 'kip-in': y = x*112.98482902762
					elif unitForm == 'lbf-ft': y = x*1.3558179483314
					elif unitForm == 'lbf-in': y = x*0.112984829027617
					elif unitForm == 'ozf-ft': y = x*0.0847386217707125
					elif unitForm == 'ozf-in': y = x*0.00706155181422604
					elif unitForm == 'N-cm': y = x*0.01
					elif unitForm == 'N-m': y = x*1
					elif unitForm == 'N-mm': y = x*0.001
					else: print('Error in',unitType)

				elif unitType == 'Velocity or Speed': #m/s
					if unitForm == 'cm/h': y = x*0.27777777777778*10**-5
					elif unitForm == 'cm/min': y = x*0.000166666666666667		
					elif unitForm == 'cm/s': y = x*0.01
					elif unitForm == 'ft/h': y = x*0.84666666666667*10**-4
					elif unitForm == 'ft/min': y = x*0.00508
					elif unitForm == 'ft/s': y = x*0.3048
					elif unitForm == 'in/h': y = x*0.70555555555556*10**-5
					elif unitForm == 'in/min': y = x*0.000423333333333333
					elif unitForm == 'in/s': y = x*0.0254
					elif unitForm == 'km/h': y = x*0.277777777777778
					elif unitForm == 'km/min': y = x*16.666666666667
					elif unitForm == 'km/s': y = x*1000
					elif unitForm == 'knots (naut. mi/h)': y = x*0.514444444444444
					elif unitForm == 'm/h': y = x*0.000277777777777778
					elif unitForm == 'm/min': y = x*0.0166666666666667
					elif unitForm == 'm/s': y = x*1
					elif unitForm == 'miles/h': y = x*0.44704
					elif unitForm == 'miles/min': y = x*26.8224
					elif unitForm == 'miles/s': y = x*1609.344
					elif unitForm == 'mm/h': y = x*0.27777777777778*10**-6
					elif unitForm == 'mm/min': y = x*0.16666666666667*10**-4
					elif unitForm == 'mm/s': y = x*0.001
					else: print('Error in',unitType)

				elif unitType == 'Viscosity, Dynamic': #Pa-s
					if unitForm == 'centipoise': y = x*0.001
					elif unitForm == 'lbf-h/in^2': y = x*24821126.255406
					elif unitForm == 'lbf-s/ft^2': y = x*47.880258980336
					elif unitForm == 'lbf-s/in^2': y = x*6894.7572931684
					elif unitForm == 'lbm/(ft-s)': y = x*1.4881639435696
					elif unitForm == 'lbm/(ft-h)': y = x*0.000413378873213765
					elif unitForm == 'Pa-s (Pascal-second)': y = x*1
					elif unitForm == 'poise': y = x*0.1	
					elif unitForm == 'slug/(ft-s)': y = x*47.880258980336
					else: print('Error in',unitType)

				elif unitType == 'Viscosity, Kinematic': #m^2/s
					if unitForm == 'centistokes': y = x*0.1*10*-6
					elif unitForm == 'ft^2/s': y = x*0.09290304
					elif unitForm == 'in^2/s': y = x*0.00064516
					elif unitForm == 'm^2/s': y = x*1
					elif unitForm == 'stokes': y = x*0.0001
					else: print('Error in',unitType)

				elif unitType == 'Volume': #m^3
					if unitForm == 'acre-ft (US Survey ft)': y = x*1233.4892384681
					elif unitForm == 'acre-in (US Survey ft)': y = x*102.79076987235
					elif unitForm == 'barrel (42 US gal)': y = x*0.158987294928
					elif unitForm == 'bushel (US dry)': y = x*0.03523907016688
					elif unitForm == 'cc (cm^3)': y = x*0.1*10**-5
					elif unitForm == 'cord (128 ft^3)': y = x*3.624556363776
					elif unitForm == 'cup (US liquid)': y = x*0.0002365882365
					elif unitForm == 'fl oz (US fluid oz)': y = x*0.295735295625*10**-4
					elif unitForm == 'ft^3 (cubic feet)': y = x*0.028316846592
					elif unitForm == 'gallon (US dry)': y = x*0.00440488377086
					elif unitForm == 'gallon (US liquid)': y = x*0.003785411784
					elif unitForm == 'gallon (UK & Can.)': y = x*0.00454609
					elif unitForm == 'in^3': y = x*0.16387064
					elif unitForm == 'liter': y = x*0.001
					elif unitForm == 'm^3': y = x*1
					elif unitForm == 'mi^3 (cubic mile)': y = x*4168181825.4406
					elif unitForm == 'ml (milliliter)': y = x*0.1*10**-5
					elif unitForm == 'mm^3': y = x*0.1*10**-8
					elif unitForm == 'peck (US dry)': y = x*0.00880976754172
					elif unitForm == 'pint (US liquid)': y = x*0.000473176473
					elif unitForm == 'pint (US dry)': y = x*0.0005506104713575
					elif unitForm == 'quart (US liquid)': y = x*0.000946352946		
					elif unitForm == 'quart (US dry)': y = x*0.001101220942715
					elif unitForm == 'tablespoon': y = x*0.1478676478125*10**-4
					elif unitForm == 'teaspoon': y = x*0.492892159375*10**-5
					elif unitForm == 'yd^3': y = x*0.764554857984
					else: print('Error in',unitType)

				elif unitType == 'Volume Flow Rate': #m^3/s
					if unitForm == 'acre-ft/h (US Survey ft)': y = x*0.342635899574486
					elif unitForm == 'acre-ft/min (US Survey)': y = x*20.558153974469
					elif unitForm == 'barrel/h (42 gal)': y = x*0.4416313748*10**-4
					elif unitForm == 'barrel/min (42 gal)': y = x*0.0026497882488
					elif unitForm == 'cm^3/h': y = x*0.27777777777778*10**-9
					elif unitForm == 'cm^3/min': y = x*0.16666666666667*10**-7
					elif unitForm == 'cm^3/s': y = x*0.1*10**-5
					elif unitForm == 'ft^3/h': y = x*0.786579072*10**-5
					elif unitForm == 'ft^3/min': y = x*0.0004719474432
					elif unitForm == 'ft^3/s': y = x*0.028316846592
					elif unitForm == 'gallon/h (US liq.)': y = x*0.10515032733333*10**-5
					elif unitForm == 'gallon/min (US liq.)': y = x*0.630901964*10**-4
					elif unitForm == 'gallon/s (US liq.)': y = x*0.003785411784
					elif unitForm == 'in^3/h': y = x*0.45519622222222*10**-8
					elif unitForm == 'in^3/min': y = x*0.27311773333333*10**-6
					elif unitForm == 'in^3/s': y = x*0.16387064*10**-4
					elif unitForm == 'liter/h': y = x*0.27777777777778*10**-6
					elif unitForm == 'liter/min': y = x*0.16666666666667*10**-4
					elif unitForm == 'liter/s': y = x*0.001
					elif unitForm == 'm^3/h': y = x*0.000277777777777778
					elif unitForm == 'm^3/min': y = x*0.0166666666666667
					elif unitForm == 'm^3/s': y = x*1
					elif unitForm == 'mm^3/h': y = x*0.27777777777778*10**-12
					elif unitForm == 'mm^3/min': y = x*0.16666666666667*10**-1
					elif unitForm == 'mm^3/s': y = x*0.1*10**-8
					elif unitForm == 'quart/h (US liq.)': y = x*0.26287581833333*10**-6
					elif unitForm == 'quart/min (US liq.)': y = x*0.157725491*10**-4
					elif unitForm == 'quart/s (US liq.)': y = x*0.000946352946
					elif unitForm == 'yd^3/h': y = x*0.00021237634944
					elif unitForm == 'yd^3/min': y = x*0.0127425809664
					elif unitForm == 'yd^3/s': y = x*0.764554857984
					else: print('Error in',unitType)
				else: y = 1 #Unitless
				
				x = 1/y
				unitForm = unitTo

		else: #K
			if unitForm == 'Centigrade (C)': y = x +273.15
			elif unitForm == 'Fahrenheit (F)': y = (x+459.67)*5/9
			elif unitForm == 'Kelvin (K)': y = x*1
			elif unitForm == 'Rankine (R)': y = x*5/9
			elif unitForm == 'Delise (De)': y = 373.15-x*2/3
			elif unitForm == 'Newton (N)': y = x*100/33+237.15
			elif unitForm == 'Reaumur (Re)': y = x*5/4+237.15
			elif unitForm == 'Romer (Ro)': (y-7.5)*40/21+273.15
			else: print('Error in',unitType)

			if unitTo == 'Centigrade (C)': x = y - 273.15
			elif unitTo == 'Fahrenheit (F)': x = y*9/5 - 459.67
			elif unitTo == 'Kelvin (K)': x = y*1
			elif unitTo == 'Rankine (R)': x = y*9/5
			elif unitTo == 'Delise (De)': x = (373.15-y)*3/2
			elif unitTo == 'Newton (N)': x = (y-273.15)*33/100
			elif unitTo == 'Reaumur (Re)': x = (y-273.15)*4/5
			elif unitTo == 'Romer (Ro)': x = (y-273.15)*21/40+7.5
			else: print('Error in',unitType)
		print('Conversion Sucessful\n')
		return x