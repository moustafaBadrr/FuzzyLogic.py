def getValue(points,X):
    #print(points)
    a=(points[1][1]-points[0][1])/(points[1][0]-points[0][0])
    b=points[1][1]-a*points[1][0]
    #print(a," *x+ ",b)
    return a*X+b
def linesEquations(inputs): #mina
    project_funding_sets=[[0,0,10,30],[10,30,40,60],[40,60,70,90],[70,90,100,100]]
    project_funding_states=["very low","low","medium","high"]
    team_experience_level_sets=[[0,15,30], [15,30,45], [30,60,60]]
    team_experience_level_states=["beginner", "intermediate", "expert"]
    #input=[50,40]
    lines4Shape=[0,1,1,0]
    lines3Shape = [0, 1, 0]
    points1 = []
    state1=[]
    for i in range(len(project_funding_sets)):
        state=project_funding_states[i]
        if(min(project_funding_sets[i])<inputs[0] and max(project_funding_sets[i])>inputs[0]):
            #print(project_funding_sets[i])
            state1.append(state)
            for j in range(len(project_funding_sets[i])):
                if project_funding_sets[i][j]>inputs[0]:
                    line=[[project_funding_sets[i][j-1], lines4Shape[j-1]],[project_funding_sets[i][j],lines4Shape[j]]]
                    points1.append(line)
                    break
    res1=[]
    for i in range(len(points1)):
        y=getValue(points1[i],inputs[0])
        res1.append(y)
    #print(points1)
    points2 = []
    state2 = []
    for i in range(len(team_experience_level_sets)):
        state = team_experience_level_states[i]
        if (min(team_experience_level_sets[i]) < inputs[1] and max(team_experience_level_sets[i]) > inputs[1]):
            #print(team_experience_level_sets[i])
            state2.append(state)
            for j in range(len(team_experience_level_sets[i])):
                if team_experience_level_sets[i][j] > inputs[1]:
                    line=[[team_experience_level_sets[i][j-1],lines3Shape[j-1]],[team_experience_level_sets[i][j],lines3Shape[j]]]
                    points2.append(line)
                    break
    res2=[]
    for i in range(len(points2)):
        y=getValue(points2[i],inputs[1])
        res2.append(y)
    states=[state1,state2]
    fuzzyValues=[res1,res2]
    #print(points2)
    #print(fuzzyValues)
    #print(states)

    return fuzzyValues, states
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
