
class baseConditions:
    def kelvinFromFahrenheit(fahrenheit):
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        return kelvin
    def kelvinFromCelsius(celsius):
        kelvin = celsius + 273.15
        return kelvin
    def fahrenheitFromKelvin(kelvin):
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        return fahrenheit
    def celsiusFromKelvin(kelvin):
        celsius = kelvin - 273.15
        return celsius
    
    seaLevelHectoPascals = 1013 #https://en.wikipedia.org/wiki/Pascal_(unit)
    seaLevelPascals = 100 * seaLevelHectoPascals #1PA = J/(m^3) #https://www.google.com/search?q=hectopascal+to+pascal
    sealLevelMmhg = seaLevelPascals / 133.322 # https://www.google.com/search?q=how+to+convert+pascal+to+mmhg
    sealLevelBars = seaLevelPascals / 100000 #https://www.google.com/search?q=pascals+to+bars

    startKelvin = kelvinFromFahrenheit( 60 )
class idealGas:
    constant = 8.31446261815324 # J⋅K−1⋅mol−1 # https://en.wikipedia.org/wiki/Gas_constant
    y = 5/3 # also known as gamma # http://astronomy.nmsu.edu/jasonj/565/docs/10_01.pdf
    specificHeatPerMole = constant * (3/2)
class air:
    y = 1.4 # https://www.grc.nasa.gov/www/k-12/BGP/specheat.html
    heatPerMol = 20.85 #https://en.wikipedia.org/wiki/Table_of_specific_heat_capacities
    kgPerMole = 0.0289 #http://www.faculty.luther.edu/~bernatzr/Courses/Sci123/Chapter08/IdealGasLaw/frameIGL.html
    airHeatPerKg = 1007 #https://www.researchgate.net/figure/Air-density-and-air-specific-heat-capacity-under-different-temperature-Source-25_tbl3_340027386
class antoine:
    # see here:
    # http://ddbonline.ddbst.com/AntoineCalculation/AntoineCalculationCGI.exe?component=Water
    # also, see chatgpt here:
    # C:\Users\brigh\notMusic\records\other\immigration_analysis_christianity\depression_based_on_enthalpy.py
    # P in mmHg, T in °C, also base 10 logs used
    A = 8.07131
    B = 1730.63
    C = 233.426
class water:
    waterHeatHeatPerKg = 4184 #https://en.wikipedia.org/wiki/Specific_heat_capacity
    waterKgPerM3 = 1000 #https://en.wikipedia.org/wiki/Kilogram_per_cubic_metre
    molesPerKg = 55.55 #https://www.omnicalculator.com/chemistry/molarity, https://www.quora.com/What-is-the-number-of-moles-in-1-kg-of-water
    steamHeatPerMole = 35.8 #https://www.google.com/search?q=specific+heat+steam+per+mole
