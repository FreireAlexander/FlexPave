import math
import scipy.stats as st
from parameters.units import units

class flexiblePavement:

    def __init__(self, 
                 Reliability: float = 0.95, 
                 Standard_Deviation: float = 0.40, 
                 Structural_Number: float = 0, 
                 Delta_PSI: float = 2, 
                 Mr: float= 1500):
        """
        Pavimento Flexible según AASTHOO 93'
        Realiability: Nivel de Confianza del diseño por defecto es 95%
        Standar Deviation o S0: Desviación Estandar, para felxibles entre 0.4 y 0.5
        Structural Number o SN: Número Estructural en centimetros
        Delta_PSI: Diferencia de los indices de serviciabilidad final e inicial del diseño
        Mr: Modulo resiliente de la Subrasante en MPA
        """
        self.Zr = st.norm.ppf(Reliability)
        self.S0 = Standard_Deviation
        self.SN = Structural_Number*25/64
        self.Delta_PSI = Delta_PSI
        self.Mr = units.MPAtoPSI(Mr)

    def getAxes(self):
        return math.pow(10,(self.Zr*self.S0+9.36*math.log10(self.SN+1) \
            -0.20+((math.log10(((self.Delta_PSI)/(4.2-1.5))))/(0.40+(1094/math.pow(self.SN+1,5.19)))) \
            +2.32*math.log10(self.Mr)-8.07))

