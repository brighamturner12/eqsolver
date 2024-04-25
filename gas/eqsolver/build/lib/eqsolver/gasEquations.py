
#class equations:

import eqsolver.gasConsts as consts
#import constants

class GROUP_justGas:
    pressureTemperature = "(T2/T1) = (p2/p1)**(1-1/y)"
    volumePressure = "p2/p1 = (v1/v2)**y"
    class pressureVolumeTemperature:
        y = consts.idealGas.y #getStartPressure()
        x = "get:pressureTemperature"
        x2 = "get:volumePressure"
    idealGas = "P*V = n*R*T"
    class idealGasR:
        x = "get:idealGas"
        R = consts.idealGas.constant
    compressionEnergy = "energy = integrate( outside_p - solve(px/p1 - (v1/vx)**y, px)[0],(vx, v1, v2))"
    temperatureEnergy = "energy = m * c * T" #https://www.softschools.com/formulas/physics/specific_heat_formula/61/
    molesToKg = "m = kgPerMole * n"
    
    potentialEnergy = "potentialEnergy = (1/(y-1))*P*V"
class GROUP_boiling_stuff:
    enthalpy = "ln( P1/P2 ) = (-L/R) * ((1/T1) - (1/T2))" #https://sciencing.com/determine-boiling-points-pressure-7678378.html
    class boilingPoint:
        antoineEquation = "log(P_mmHg) / log(10) = A - B /(T_celsius + C)"
        R = consts.idealGas.constant
        antoine_constants = consts.antoine # (3)
        celsiusKelvin2 = "T = T_celsius + 273.15"
        mmHgPascals2 = "P_mmHg = P / 133.322"    
    
    class latentHeat:
        #https://www.chemteam.info/GasLaw/Clasius-Clapeyron-Equation.html
        #https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Physical_Properties_of_Matter/States_of_Matter/Phase_Transitions/Clausius-Clapeyron_Equation
        x = "get:boilingPoint"
        basicClausiusClapeyron = "dP_over_dT = P*L/((T**2)*R)" #https://en.wikipedia.org/wiki/Clausius%E2%80%93Clapeyron_relation
        pressureSlope = "slope_mmHg = diff(solve( (log(P_mmHg) / log(10)) - ( A - B /(T_celsius + C)) , P_mmHg)[0],T_celsius)"
        pressureSlopeConversion = "slope_mmHg = dP_over_dT / 133.322"
        celsiusKelvin2 = "T = T_celsius + 273.15"
        mmHgPascals2 = "P_mmHg = P / 133.322"      
    
    class expansion:
        x = "get:latentHeat"
        y = consts.water 
        #dP = -1
        gettingEnergyLost = "energyChange = waterVolume * waterKgPerM3 * waterHeatCapacity * (1/dP_over_dT) * dP"
        molesLost = "molesWaterLost = -energyChange * (1/L)"
        volumeWaterLost = "volumeWaterLost = molesWaterLost * (1/molesPerKg) * (1/waterKgPerM3)"
        steamVolumeIncrease = "P*steamVolumeGained = molesWaterLost*R*T"
        volumeIncrease = "volumeIncrease = steamVolumeGained - volumeWaterLost"
    class expansionPlus:
        x = "get:expansion"
        changeTemperature = "dT = (1/dP_over_dT) * dP"
        
        idealGas = "P*finalOutsideV = outsideMoles*R*outsideT"
        outsideVolChange = "outsideVolChange = finalOutsideV - startOutsideV"
        ultimateVolIncrease = "ultimateVolIncrease = outsideVolChange + volumeIncrease"
        #dP_over_dTV = "dP_over_dTV = dP / volumeIncrease"
        #f
class GROUP_showing_off_sympy_powers: # has to start with "GROUP_"
    diffExperiment = "diff( log(x), x) + y = 5"
    integralExperiment = "integrate( log(x), x) + y = 5"
    limitedIntegralExperiment = "integrate(1/x, (x, a, b)) = 5" #goes from a to b
    solveExperiment = "solve(x - 4 + a, x)[0] + b = 3"
