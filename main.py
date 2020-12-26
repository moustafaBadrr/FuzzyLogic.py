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


def get_index_of_value(value, arr_of_value):  # Mustafa
    for i in range (0, len(arr_of_value)):
        if arr_of_value[i] == value:
            return i
    return -1


def rules (fuzzy_values, states):  # mustafa

    # First Rule . If project_funding is high or team_experience_level is expert then risk is low
    state1_risk = "low"
    if "high" in states[0] and "expert" in states [1]:
        value_of_high = fuzzy_values[0][get_index_of_value("high", states[0])]
        value_of_expert = fuzzy_values[1][get_index_of_value("expert", states[1])]
        rule1_value = max(value_of_high, value_of_expert)
        print("First Rule existing two of them", rule1_value)
    else:
        if "high" in states[0]:
            rule1_value = fuzzy_values[0][get_index_of_value("high", states[0])]
        elif "expert" in states[1]:
            rule1_value = fuzzy_values[1][get_index_of_value("expert", states[1])]
        else:
            rule1_value = 0
    # Second Rule If project_funding is medium and team_experience_level is intermediate
    # or team_experience_level is beginner then risk is normal.
    state2_risk = "normal"
    if "medium" in states[0] and ("intermediate" in states[1] or "beginner" in states[1]):
        value_of_medium = fuzzy_values[0][get_index_of_value("medium", states[0])]
        if "intermediate" in states[1]:
            value_of_intermediate = fuzzy_values[1][get_index_of_value("intermediate", states[1])]
            rule2_value = min(value_of_medium, value_of_intermediate)
        elif "beginner" in states[1]:
            value_of_beginner = fuzzy_values[1][get_index_of_value("beginner", states[1])]
            rule2_value = min(value_of_medium, value_of_beginner)
    else:
        rule2_value = 0  # because it is AND so we select the minimum and
        # if any missing value so the minimum is equal to 0
    # Third Rule If project_funding is very low then risk is high
    state3_risk = "high"
    if "very low" in states[0]:
        rule3_value = fuzzy_values[0][get_index_of_value("very low", states[0])]
    else:
        rule3_value = 0
    # Fourth Rule If project_funding is low and team_experience_level is beginner then risk is high
    state4_risk = "high"
    if "low" in states[0] and "beginner" in states[1]:
        value_of_low = fuzzy_values[0][get_index_of_value("low", states[0])]
        value_of_beginner2 = fuzzy_values[1][get_index_of_value("beginner", states[1])]
        rule4_value = min(value_of_low, value_of_beginner2)
    else:
        rule4_value = 0
    return [rule1_value, rule2_value, rule3_value, rule4_value], [state1_risk, state2_risk, state3_risk, state4_risk]



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
    
main()
