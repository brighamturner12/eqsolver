#https://en.wikipedia.org/wiki/IS%E2%80%93LM_model
#https://github.com/joaqsgonzales/is-lm-macroeconomic-model/blob/main/IS-LM%20Model.ipynb
#https://analystprep.com/cfa-level-1-exam/economics/explain-the-is-lm-curves-and-how-they-combine-to-generate-the-aggregate-demand-curve/

#Y = gdp
#C = consumption
#In = investment
#G = government expenditure
#Yd = disposable income - gdp minus taxes
#T = taxes
#I0 = investments if zero interest rate
#h = sensitivity of investment to interest rate
#r = intenrenst rate
#Ms = money supply
#Md = money demand
#k = sensity money demand in relation to gdp
#mu = sensity money demand in relation to interest rates

#Tr = tax rate
class ISLM:
    IScurve = "Y = C + In + G"
    consumption = "C = a + b*Yd"
    disposableIncome = "Yd = Y - T"
    taxCurve = "T = Tr*Y"
    investmentDemandCurve = "In = I0 - h*r"
    taxesEqualGovernmentExpenditure = "G = T"
    Lmcurve = "Ms = Md"
    moneyDemand = "Md = k*(1-mu*r)*Y" #"Md = k*Y - mu*r" is more standard. I like this form better though. 
