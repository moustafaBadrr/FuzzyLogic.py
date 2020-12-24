def linesEquations(inputs): #mina
    project_funding_sets=[[0,0,10,30],[10,30,40,60],[40,60,70,90],[70,90,100,100]]
    project_funding_states=["very low","low","medium","high"]
    team_experience_level_sets=[[0,15,30], [15,30,45], [30,60,60]]
    team_experience_level_states=["beginner", "intermediate", "expert"]
    #input=[50,40]
    #......
    #return [[res1,res2],[res1,res2]],[["state1","state2"],["state1","state2"]]
    pass
def rules(fuzzyValues, states): # mustafa
    #fuzzyValues=[[res1,res2],[res1,res2]]
    #states[["state1","state2"],["state1","state2"]]
    features=["project_funding","team_experience_level"]
    #rules.............
    #return [v1,v2,v3,v4],["state1","state2","state3","state4"]
    pass
def calcTheResult(rulesValuesRes,rulesStatesRes): #peter
    # rulesValuesRes=[v1, v2, v3, v4]
    # rulesStatesRes=["state1", "state2", "state3", "state4"]

    riskSets=[[0,25,50],[25,50,75],[50,100,100]]
    riskStates=["high","normal","low"]

    # return risk=66.6 state="normal"
    pass

def fuzzy(inputs):
    fuzzyValues,states=linesEquations(inputs)
    rulesValuesRes,rulesStatesRes=rules(fuzzyValues, states)
    risk,state=calcTheResult(rulesValuesRes, rulesStatesRes)
    return risk,state
def main():
    variablesNum = int(input("Variables :"))
    inputs=[]
    for i in range(variablesNum):
        if i == 0:
            x = int(input("Project Fund :"))
            inputs.append(x)
        elif i == 1:
            x = int(input("Experience Level :"))
            inputs.append(x)
    risk, state=fuzzy(inputs)
    print("risk =",risk)
    print("risk will be ", state)