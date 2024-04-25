
import sympy as sp
class solver:
    # important argumetns to function calls:
    # setVal, 
    #       redefine, solutionIndex,
    #
    # keywords to put in function name:
    #     algebraic, f
    # what to do if the input class already has all the values:
        # the function name can have variable names in it too, and it will be forced to calculate them rather than use them
        # set redefine = True, otherwise it gets an error, assuming setVal is true, if you want to redefine your class
    # 
    def __getattr__(self, attr):
        # here it deciphers the method name to use the correct equations.         
        def basicFuncToReturn(*args, **kwargs ):
            def processEquationsAndParsedVariables(allEquations , varsHereToFind, allInputs, reallyBasicInputs, isAlgebraic, isNumerical):
                
                ####### deal with keywords #######
                setVal = False
                if "setVal" in kwargs.keys():
                    setVal = kwargs["setVal"]
                
                redefine = False
                if "redefine" in kwargs.keys():
                    redefine = kwargs["redefine"] # , setVal, redefine
                
                if "solutionIndex" in kwargs.keys():
                    solutionIndex = kwargs["solutionIndex"]
                    #assert solutionIndex < 2
                else:
                    solutionIndex = -1
                
                # deal with this part
                if isNumerical:
                    assert not isAlgebraic
                    changedEquations = []
                    for eq in allEquations:
                        changedEquations.append( sp.simplify(eq).subs(allInputs) )
                    # startValsAre1 = {}
                    # for ell in varsHereToFind:
                    #     startValsAre1[ell] = 1.0
                    # print(changedEquations )
                    # print(varsHereToFind )
                    # print(startValsAre1)
                    varNames = list(varsHereToFind)
                    solutionn_unprcd = sp.nsolve( changedEquations ,  varNames , [1.0]*len(varsHereToFind) )
                    solutionn = {}
                    for i,varnm in enumerate(varNames):
                        solutionn[varnm ] = solutionn_unprcd[i]
                    
                    if setVal:
                        for keyy in solutionn:
                            assert redefine  or  (not hasattr(args[0], keyy )) , (hasattr(args[0], keyy ), keyy, solutionn[ keyy ])
                            setattr(args[0], keyy , solutionn[keyy] )
                    return solutionn
                
                funcPerhapsHere = "_fasfdjksa_" + "_".join(list(sorted(allEquations))) + \
                                    "_fasfdjksa_" + "_".join(list(sorted(varsHereToFind))) + \
                                    "si" + str(solutionIndex)
                
                if funcPerhapsHere in self.myFuncs.keys():
                    return self.myFuncs[ funcPerhapsHere ]( allInputs, reallyBasicInputs , isAlgebraic, setVal, redefine, *args) #, **kwargs)
                
                def getInstructions(knowns, equations):
                    equationToSymbols = {}
                    knownSet = set( knowns.keys() )
                    potentialToKnown = []
                    for equation in equations:
                        inner_symbols = sp.sympify(equation).free_symbols
                        inner_variable_names = [str(symbol) for symbol in inner_symbols]

                        equationToSymbols[equation] = set(inner_variable_names)
                        potentialToKnown.extend(inner_variable_names)
                    potentialToKnown = set( potentialToKnown )
                    thingsToFind = potentialToKnown - knownSet
                    
                    didSomething = True
                    equationsToFind = set(equations)
                    instructionsz = []
                    while didSomething:
                        didSomething = False
                        for equation in equationsToFind:
                            varsToFind = list(equationToSymbols[equation] - knownSet)
                            if len(varsToFind) == 1:
                                
                                knownSet.add(varsToFind[0])
                                didSomething = True
                                
                                equationsToFind = equationsToFind - set([equation])
                                
                                solutionn = sp.solve( equation , varsToFind[0])[0]
                                
                                instructionsz.append({
                                    "name":varsToFind[0],
                                    "solution":sp.simplify(solutionn),
                                })
                    finalThingsToFind = potentialToKnown - knownSet
                    if len(finalThingsToFind) > 0:
                        solutionList = sp.solve(  list( equationsToFind ) , finalThingsToFind  )
                        
                        if isinstance(solutionList,list):
                            if solutionIndex == -1:
                                
                                assert len(solutionList) == 1,(len(solutionList), solutionList)
                            else:
                                solutionList = solutionList[ solutionIndex ]
                        for thingg in finalThingsToFind:
                            instructionsz.append({
                                        "name":thingg,
                                        "solution": sp.simplify(solutionList[ sp.simplify(thingg) ]),
                                    })
                        
                    return instructionsz 
                instructionsz = getInstructions(
                    knowns = allInputs, 
                    equations = allEquations )
                
                #solutionList = sp.solve( allEquations , varsHereToFind )                
                def innerFunc( allInputs, reallyBasicInputs , isAlgebraic, setVal, redefine, *args): #,  **kwargs):
                    
                    resultsz = {}
                    if isAlgebraic:
                        oldInputs = allInputs.copy()
                        allInputs = reallyBasicInputs #{}
                    for instruction in instructionsz:  
                        if isAlgebraic:
                            allInputs[ instruction["name"] ] = sp.simplify(instruction["solution"].subs(allInputs))
                        else:
                            
                            allInputs[ instruction["name"] ] = float(instruction["solution"].subs(allInputs))
                        resultsz[ instruction["name"] ] = allInputs[ instruction["name"] ]
                        
                        if setVal:
                            
                            assert redefine  or  (not hasattr(args[0], instruction["name"] )) , (hasattr(args[0], instruction["name"] ), instruction["name"], allInputs[ instruction["name"] ])
                            setattr(args[0], instruction["name"], allInputs[ instruction["name"] ] )       
                    
                    if isAlgebraic:
                        return resultsz, oldInputs
                    else:
                        return resultsz
                
                self.myFuncs[ funcPerhapsHere ] = innerFunc
                
                return self.myFuncs[ funcPerhapsHere ]( allInputs, reallyBasicInputs , isAlgebraic, setVal, redefine, *args) #, **kwargs)
            assert len(args) <= 1, "there can only be one non keyword argument - the class containing variable names"
            
            ####### step 1 - getting equation names and variables referenced #######
            eqNames = attr.split("_")
            allVariables = []
            allEquations = []
            mustFind = []
            maybeKnownStuff = {}
            isAlgebraic = False
            isNumerical = False
            def dealWithEquation( thisEquation ):
                if thisEquation[0:len("known:")] == "known:":
                    splitEquation = thisEquation.split(":")
                    maybeKnownStuff[splitEquation[1]] = float(splitEquation[2])
                else:
                    allEquations.append( thisEquation )
                    inner_symbols = sp.sympify(thisEquation).free_symbols
                    inner_variable_names = [str(symbol) for symbol in inner_symbols]
                    allVariables.extend( inner_variable_names )
            for eqName in eqNames:
                if eqName == "algebraic":
                    isAlgebraic = True
                elif eqName == "numerical":
                    isNumerical = True
                elif eqName in self.knowledgeDict.keys():
                    if isinstance(self.knowledgeDict[eqName],dict):
                        relevantDict = self.knowledgeDict[eqName] #attr]
                        for keyy in relevantDict.keys():
                            thisEquation = relevantDict[keyy]
                                                        
                            dealWithEquation( thisEquation )
                    else:
                        thisEquation  = self.knowledgeDict[eqName]
                        
                        dealWithEquation( thisEquation )
                else:
                    mustFind.append(eqName)
            allPosibleVars = set(allVariables) - set(mustFind) #possible to know
            
            ####### step 2 - process equations that are actually constant definitions #######
            potentialVariables = set()
            allInputs = {}
            reallyBasicInputs = {}
            for key, value in maybeKnownStuff.items():
                if key in allPosibleVars:
                    potentialVariables.add( key )
                    allInputs[key] = value
                    reallyBasicInputs[key] = value
            
            ####### step 3 - process keyword arguments #######
            for key, value in kwargs.items():
                if key in allPosibleVars:
                    potentialVariables.add( key )
                    allInputs[key] = value
            
            varsHereToFind = set(list(allPosibleVars - potentialVariables) + mustFind )
            ####### if enough variables are known that it is possible to solve, proceed to solve the equations #######
            if len(varsHereToFind) <= len(allEquations):
                return processEquationsAndParsedVariables(allEquations , varsHereToFind, allInputs, reallyBasicInputs, isAlgebraic, isNumerical)
            
            #######################################################
            ####### step 4 - process input class if necessary #######
            
            
            assert len(args) == 1, ( "you didn't have enough equations for the number of unknown variables, and you didn't provide a class containing more equation names", 
                                    "num unknown variables to find:"+str(len(varsHereToFind)),
                                    "num equations provided:"+str(len(allEquations)),
                                    "the variables still left unknown:" + str(varsHereToFind),
                                    "all equations provided:" + str(allEquations))
            arg = args[0]
            for key in allPosibleVars:
                if hasattr(arg, key):
                    potentialVariables.add( key )
                    allInputs[key] = getattr(arg, key)
            
            # allPosibleVars = set(allVariables) - set(mustFind) #possible to be known
            # potentialVariables - known from args
            # allInputs - the same
            varsHereToFind = set(list(allPosibleVars - potentialVariables) + mustFind )
           
            ####### assert that enough equations exist to solve the unknown variables #######             
            assert len(varsHereToFind) <= len(allEquations), ( "you didn't have enough equations for the number of unknown variables", 
                                    "num unknown variables to find:"+str(len(varsHereToFind)),
                                    "num equations provided:"+str(len(allEquations)),
                                    "the variables still left unknown:" + str(varsHereToFind),
                                    "all equations provided:" + str(allEquations))
            return processEquationsAndParsedVariables(allEquations , varsHereToFind, allInputs, reallyBasicInputs, isAlgebraic, isNumerical)
        
        return basicFuncToReturn
    def __init__(self, theWorldsKnowledge ):
        def get_custom_attributes(cls):
            custom_attrs = {}
            for attr_name, attr_value in cls.__dict__.items():
                # Exclude attributes inherited from the base classes
                if not attr_name.startswith('__'):
                    custom_attrs[attr_name] = attr_value
            return custom_attrs
        def completelyTurnToDictionary( stuff ):
            startt = get_custom_attributes( stuff )
            newDict = {}
            for key in startt.keys():
                if not ( isinstance(startt[key],str) or
                            isinstance(startt[key],int) or
                            isinstance(startt[key],float) ):
                    newDict[key] = completelyTurnToDictionary( startt[key] )
                    if key[0:len("GROUP_")] == "GROUP_":
                        for keyy in newDict[key].keys():
                            newDict[keyy] = newDict[key][keyy]
                else:
                    newDict[key] = startt[key]
                        
            return newDict #startt
        totalDict = completelyTurnToDictionary( theWorldsKnowledge )
        
        def findEndOfTrail(name, stringg, outerDict):
            
            if isinstance(stringg,dict):
                rezs = []
                for key in stringg.keys():
                    rezs.extend( findEndOfTrail(key,stringg[key],outerDict) )
                return rezs
            elif isinstance(stringg,int) or isinstance(stringg,float):
                return [[name, "known:"+name + ":"+str(stringg)]]
            elif stringg[0:len("get:")] == "get:":
                theRest = stringg[ len("get:"): ].split(".")
                whereAmI = outerDict
                for keyy in theRest:
                    whereAmI = whereAmI[keyy]
                if isinstance( whereAmI, str ):
                    return findEndOfTrail( theRest[-1], whereAmI, outerDict)
                else:
                    rezs = []
                    for key in whereAmI.keys():
                        rezs.extend( findEndOfTrail(key,whereAmI[key],outerDict))
                    return rezs
            else:
                splitString = stringg.split("=")
                assert len(splitString)==2
                return [[name, "(" + splitString[0]+") - ("+splitString[1]+")"]]
        def removeEquals(dictt ,outerDict):
            rezs = {}
            for key in dictt.keys():
                allTheStuffToAdd = findEndOfTrail(
                        name = key,
                        stringg = dictt[key],
                        outerDict = outerDict)
                if not ( isinstance(dictt[key],str) or
                            isinstance(dictt[key],int) or
                            isinstance(dictt[key],float) ):
                    #rezs[key] = removeEquals(dictt[key] ,outerDict)
                    thingToAdd = {}
                    for name,equation in allTheStuffToAdd:
                        thingToAdd[name] = equation
                    rezs[key] = thingToAdd
                else:                    
                    for name,equation in allTheStuffToAdd:
                        rezs[name] = equation
            return rezs
        self.knowledgeDict = removeEquals(totalDict,totalDict)
        
        self.myFuncs = {}
