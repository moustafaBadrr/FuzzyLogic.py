def get_value(points, x):
    # print(points)
    a = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
    b = points[1][1] - a * points[1][0]
    # print(a," *x+ ",b)
    return a * x + b


def lines_equations(inputs):  # mina
    project_funding_sets = [[0, 0, 10, 30], [10, 30, 40, 60], [40, 60, 70, 90], [70, 90, 100, 100]]
    project_funding_states = ["very low", "low", "medium", "high"]
    team_experience_level_sets = [[0, 15, 30], [15, 30, 45], [30, 60, 60]]
    team_experience_level_states = ["beginner", "intermediate", "expert"]
    # input=[50,40]
    lines4_shape = [0, 1, 1, 0]
    lines3_shape = [0, 1, 0]
    points1 = []
    state1 = []
    for i in range(len(project_funding_sets)):
        state = project_funding_states[i]
        if (min(project_funding_sets[i]) < inputs[0]) and max(project_funding_sets[i]) > inputs[0]:
            # print(project_funding_sets[i])
            state1.append(state)
            for j in range(len(project_funding_sets[i])):
                if project_funding_sets[i][j] > inputs[0]:
                    line = [[project_funding_sets[i][j - 1], lines4_shape[j - 1]],
                            [project_funding_sets[i][j], lines4_shape[j]]]
                    points1.append(line)
                    break
    res1 = []
    for i in range(len(points1)):
        y = get_value(points1[i], inputs[0])
        res1.append(y)
    # print(points1)
    points2 = []
    state2 = []
    for i in range(len(team_experience_level_sets)):
        state = team_experience_level_states[i]
        if (min(team_experience_level_sets[i]) < inputs[1]) and max(team_experience_level_sets[i]) > inputs[1]:
            # print(team_experience_level_sets[i])
            state2.append(state)
            for j in range(len(team_experience_level_sets[i])):
                if team_experience_level_sets[i][j] > inputs[1]:
                    line = [[team_experience_level_sets[i][j - 1], lines3_shape[j - 1]],
                            [team_experience_level_sets[i][j], lines3_shape[j]]]
                    points2.append(line)
                    break
    res2 = []
    for i in range(len(points2)):
        y = get_value(points2[i], inputs[1])
        res2.append(y)
    states = [state1, state2]
    fuzzy_values = [res1, res2]
    # print(points2)
    # print(fuzzyValues)
    # print(states)

    return fuzzy_values, states


def get_index_of_value(value, arr_of_value):  # Mustafa
    for i in range(0, len(arr_of_value)):
        if arr_of_value[i] == value:
            return i
    return -1


def rules(fuzzy_values, states):  # mustafa
    rule1_value, rule2_value, rule3_value, rule4_value = 0, 0, 0, 0
    # First Rule . If project_funding is high or team_experience_level is expert then risk is low
    state1_risk = "low"
    if "high" in states[0] and "expert" in states[1]:
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


def calc_the_result(rules_values_res, rules_states_res):  # peter

    risk_sets = [[0, 25, 50], [25, 50, 75], [50, 100, 100]]
    centroid_high = sum(risk_sets[0]) / len(risk_sets[0])
    centroid_normal = sum(risk_sets[1]) / len(risk_sets[1])
    centroid_low = sum(risk_sets[2]) / len(risk_sets[2])
    numerator = []
    for i in range(len(rules_values_res)):
        if rules_states_res[i] == 'low':
            numerator.append(rules_values_res[i] * centroid_low)
        elif rules_states_res[i] == 'normal':
            numerator.append(rules_values_res[i] * centroid_normal)
        else:
            numerator.append(rules_values_res[i] * centroid_high)
    risk = sum(numerator) / sum(rules_values_res)
    possible_states = []
    points = []
    lines3_shape = [0, 1, 0]
    for i in range(len(risk_sets)):
        if min(risk_sets[i]) < risk < max(risk_sets[i]):
            if i == 0:
                possible_states.append("high")
            elif i == 1:
                possible_states.append("normal")
            else:
                possible_states.append("low")
            for j in range(len(risk_sets[i])):
                if risk_sets[i][j] > risk:
                    line = [[risk_sets[i][j - 1], lines3_shape[j - 1]],
                            [risk_sets[i][j], lines3_shape[j]]]
                    points.append(line)
                    break

    result = []
    for i in range(len(points)):
        y = get_value(points[i], risk)
        result.append(y)
    max_intersect = max(result)
    index = get_index_of_value(max_intersect, result)
    result_state = possible_states[index]
    return risk, result_state


def fuzzy(inputs):
    fuzzy_values, states = lines_equations(inputs)
    rules_values_res, rules_states_res = rules(fuzzy_values, states)
    risk, state = calc_the_result(rules_values_res, rules_states_res)
    return risk, state


def main():
    variables_num = int(input("Variables :"))
    inputs = []
    for i in range(variables_num):
        if i == 0:
            x = int(input("Project Fund :"))
            inputs.append(x)
        elif i == 1:
            x = int(input("Experience Level :"))
            inputs.append(x)
    risk, state = fuzzy(inputs)
    print("risk =", risk)
    print("risk will be ", state)


main()
