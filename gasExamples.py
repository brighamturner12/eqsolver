
from eqsolver import solver
from eqsolver import gasConsts as consts
from eqsolver import gasEquations

if False:     
    import importlib
    importlib.reload(consts)
    importlib.reload(gasEquations)

gasSolve = solver(gasEquations) #.slv

def energy_to_compress_gas_equals_increase_in_thermal_energy():
    rez = gasSolve.pressureVolumeTemperature_compressionEnergy( #
            outside_p = 0, #consts.baseConditions.seaLevelPascals, #getStartPressure(),
            #y  = consts.gammaIdealGas(),
            v1 = 1,
            p1 = consts.baseConditions.seaLevelPascals,
            T1 = consts.baseConditions.startKelvin,
            v2 = .5
        )

    n = gasSolve.idealGasR(
            V = 1,
            P = consts.baseConditions.seaLevelPascals,
            T = consts.baseConditions.startKelvin,
        )["n"]

    thermalEnergy = n * consts.idealGas.specificHeatPerMole * (rez['T2'] - consts.baseConditions.startKelvin)
    compressionEnergy = rez["energy"]
    print("finding energy required to decrease volume of gas by factor of 2, with zero outside pressure:")
    print("   thermalEnergy:",thermalEnergy)
    print("   compressionEnergy:",compressionEnergy)
energy_to_compress_gas_equals_increase_in_thermal_energy()

print("")
def energy_to_compress_gas_equals_increase_in_thermal_energy_numerical():
    rez = gasSolve.pressureVolumeTemperature_compressionEnergy_numerical( #
            outside_p = 0, #consts.baseConditions.seaLevelPascals, #getStartPressure(),
            #y  = consts.gammaIdealGas(),
            v1 = 1,
            p1 = consts.baseConditions.seaLevelPascals,
            T1 = consts.baseConditions.startKelvin,
            v2 = .5
        )

    n = gasSolve.idealGasR_numerical(
            V = 1,
            P = consts.baseConditions.seaLevelPascals,
            T = consts.baseConditions.startKelvin,
        )["n"]

    thermalEnergy = n * consts.idealGas.specificHeatPerMole * (rez['T2'] - consts.baseConditions.startKelvin)
    compressionEnergy = rez["energy"]
    print("solving for energy numerically:")
    print("   thermalEnergy:",thermalEnergy)
    print("   compressionEnergy:",compressionEnergy)
energy_to_compress_gas_equals_increase_in_thermal_energy_numerical()

print("")
def energy_to_compress_gas_equals_increase_in_thermal_energy_normal_outside_pressure():
    rez = gasSolve.pressureVolumeTemperature_compressionEnergy( #
            outside_p = consts.baseConditions.seaLevelPascals, #getStartPressure(),
            #y  = consts.gammaIdealGas(),
            v1 = 1,
            p1 = consts.baseConditions.seaLevelPascals,
            T1 = consts.baseConditions.startKelvin,
            v2 = .5
        )

    compressionEnergy = rez["energy"]
    print("energy required to decrease volume by 2, with normal outside pressure:")
    print("   compressionEnergy:",compressionEnergy)
energy_to_compress_gas_equals_increase_in_thermal_energy_normal_outside_pressure()

print("")
def energy_to_compress_gas_equals_increase_in_thermal_energy_normal_outside_pressure_algebraic():
    rez = gasSolve.pressureVolumeTemperature_compressionEnergy_algebraic( #
            outside_p = consts.baseConditions.seaLevelPascals, #getStartPressure(),
            #y  = consts.gammaIdealGas(),
            v1 = 1,
            p1 = consts.baseConditions.seaLevelPascals,
            T1 = consts.baseConditions.startKelvin,
            v2 = .5
        )

    compressionEnergy = rez[0]["energy"]
    print("energy required to decrease volume by 2, algebraic solution:")
    print("   ",compressionEnergy)
energy_to_compress_gas_equals_increase_in_thermal_energy_normal_outside_pressure_algebraic()


print("")
def getBoilingPointByPressure():
    print("boiling point by pressure:")
    for i in range(1,21):
        proportion = i/10
        print( "   "+str( round(gasSolve.boilingPoint( 
            P = consts.baseConditions.seaLevelPascals * proportion )['T_celsius'],3)) +
              " C at " + str(int(proportion*100))+"% normal pressure: " )
getBoilingPointByPressure()       

print("")
def getLatentHeatByPressure():
    #https://en.wikipedia.org/wiki/Enthalpy_of_vaporization
    print("latent heat by pressure:")
    print("   notes:")
    print("      note that latent heat really is 2d - it depends on both pressure and temperature")
    print("      here we only follow latent heat found at the boiling point for each pressure")
    print("      notice that latent heat is decreasing, this matches standard teachings")
    print("      likewise, at normal pressure I get L = 41.498 KJ / mole, which is close to")
    print("      40.65 kJ/mol, which is the value reported on the wikipedia for enthalpy of")
    print("      vaporization, we don't know which pressure and temperature combo that")
    print("      number comes from, so the slight discrepency shouldn't be too concerning.")
    print("      unfortunately, this all relies on knowing the boiling point of water which")
    print("      isn't an exact science. here I really on the Antoine equation, which is technically")
    print("      only an equation highly correlated with boiling point. The only other way would be")
    print("      be to download a dataset giving water boiling point for each pressure, or to wait")
    print("      until physicists provide a new equation that is more precise.")
    print("   results:")
    for i in range(1,21):
        proportion = i/10
        print( "      " + str( round(gasSolve.latentHeat( 
            P = consts.baseConditions.seaLevelPascals * proportion )['L']/1000,3)) +
              " KJ / mole at " + str(int(proportion*100))+"% normal pressure: " )
getLatentHeatByPressure()

print("")
def getPressureAndTemperatureAfterCompression():
    rez = gasSolve.pressureVolumeTemperature( #
            #y  = consts.gammaIdealGas(),
            v1 = 1,
            p1 = consts.baseConditions.seaLevelPascals,
            T1 = consts.baseConditions.startKelvin,
            v2 = .5
        )
    print("temperature and pressure increase after decreasing volume by factor of 2:")
    print("   temperature increase:",rez["T2"] - consts.baseConditions.startKelvin,"C")
    print("   pressure increase:",rez["p2"]-consts.baseConditions.seaLevelPascals,"pascals")
getPressureAndTemperatureAfterCompression()

#