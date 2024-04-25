
from eqsolver import solver
from eqsolver import ISLM

if False:     
    import importlib
    importlib.reload(ISLM)

ISLMSolve = solver(ISLM) #.slv

def basiceISLMExample():
    #the solution employs a quadratic where the answer is at the point of zero slope.
    #thus, the equations technically give two answers though they are the same
    print("Working through a basic problem in the ISLM model:")
    class inputs:
        a = 35
        b = .5
        Tr = .1
        I0 = 30
        h = 200
        k = 1.25
        mu = 2
        Ms = 100
    print("   here is a basic solution to a problem involving the ISLM model.") 
    print("   here I set a (the amount consumed if disposable income were zero), to 35")
    print("   b - them marginal propensity to consume - is .5")
    print("   Tax rate is .1")
    print("   I0 - the investments if interest rate was zero - is 30")
    print("   h - the decrease in investment demand for increase in interest rate - is 200")
    print("   k - the sensity to money demand in relation to gdp - is 1.25.")
    print("   mu - the decrease (fractional) of money demand in relation to interest rate - is 2")
    print("   MS - the money supply - is 100")
    print("   this is a very over simplified model obviously. A few issues with it include:")
    print("   1) it doesn't take into account the supply side")
    print("   2) investment demand should itself be a function of gdp")
    print("   3) it doesnt' take into account labor - people should be willing to work more if less is taxed")
    print("   4) it doesn't take into account supply side of investments - people should be put more income")
    print("      into investments if interest rate is higher")
    print("   Thus we see that the ISLM model is fairly simple.")
    print("   In my view, the most important true principal of the model is that interest rate is not")
    print("   arbitrary and is (or usually is), determined by the market reaching equilibrium")
    print("   To better understand the model, I reccomend looking at the equations in ISLM.py")
    sol0 = ISLMSolve.ISLM(
        inputs,
        solutionIndex = 0
    )

    # sol1 = ISLMSolve.ISLM(
    #     inputs,
    #     solutionIndex = 1
    # )
    assert len(set( sol0.keys() ) - set(['Md', 'r', 'In', 'G',   'T', 'Y', 'C', 'Yd'])) == 0
    print("")
    print("Solution:")
    print("   money demand is:", round(sol0['Md'],2))
    print("   interest rate is:", round(sol0["r"],2))
    #print("Taxes are:", sol0["T"])
    print("   GDP is:", round(sol0["Y"],2))
    
    print("   Government spending is:", round(sol0["G"],2))
    print("   disposable income is:", round(sol0["Yd"],2))
    print("   Consumption is:", round(sol0["C"],2))
    print("   Investments are:", round(sol0["In"],2))
basiceISLMExample()

print("")
def effectOfIncreasingTaxesOnGDP(): 
    class inputs:
            a = 35
            b = .5
            I0 = 30
            h = 200
            k = 1.25
            mu = 2
            Ms = 100

    print("Effect of tax rate on gdp:")
    for i in range(5):    
        TR = i / 5
        sol = ISLMSolve.ISLM(
            inputs,
            solutionIndex = 0,
            Tr = TR
        )
        print( "   tax rate: "+str(round(TR*100,0))+"% GDP: " + str(round(sol['Y'],2) ))
    print("   GDP increases with increased taxes, because government spending is counted")
    print("   as part of GDP. Discounting government spending, investment and consumption")
    print("   decline with increased Gov't spending. It's important that this is just a")
    print("   an overly simplified model.")
effectOfIncreasingTaxesOnGDP()

print("")
def effectOfIncreasingTaxesOnConsumption():
    class inputs:
            a = 35
            b = .5
            I0 = 30
            h = 200
            k = 1.25
            mu = 2
            Ms = 100
    print("Effect of tax rate on Consumption:")
    for i in range(5):    
        TR = i / 5
        sol = ISLMSolve.ISLM(
            inputs,
            solutionIndex = 0,
            Tr = TR
        )
        print( "   tax rate: "+str(round(TR*100,0))+"% Consumption: " + str(round(sol['C'],2) ))
    print("   as we see, with higher taxes, consumption decreases.")
effectOfIncreasingTaxesOnConsumption()

print("")
def algebraicSolution():
    class inputs:
        a = 35
        b = .5
        Tr = .1
        I0 = 30
        h = 200
        k = 1.25
        mu = 2
        Ms = 100
    
    print("Algebraic solution to the model:")
    sol0 = ISLMSolve.ISLM_algebraic(
        inputs,
        solutionIndex = 0
    )
    print( "   it turns out that solving this algebraicly would be very difficult")
    print( "   here is the algebraic solution for GDP:")
    print( "   ",sol0[0]["Y"])
    print( "   and here is the algebraic solution for consumption:")
    print( "   ",sol0[0]["C"])
algebraicSolution()

