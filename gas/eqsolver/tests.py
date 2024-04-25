

#from .gas_laws import constants

import eqsolver.gasConsts as gasConsts 

if False:     
    import importlib
    importlib.reload( gasConsts )    

base = gasConsts.baseConditions

def reallyClose(num1,num2):
    return abs((num1-num2)/num1) < .000001

assert reallyClose( 50 , base.fahrenheitFromKelvin(base.kelvinFromFahrenheit(50)) )
assert reallyClose( 50 , base.celsiusFromKelvin(base.kelvinFromCelsius(50)) )

