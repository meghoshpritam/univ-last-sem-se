import matplotlib.pyplot as plt

kloc = int(input("Enter total number of lines of code: \n"))
constants = []

colors = {
    0: 'red',
    1: 'orange',
    2: 'green',
    3: 'blue',
    4: 'yellow'
}
effort = 0

required_software_reliability = [0.75, 0.88, 1.00, 1.15, 1.40]
size_of_application_database = [0, 0.94, 1.00, 1.08, 1.16]
complexity_of_the_product = [0.70, 0.85, 1.00, 1.15, 1.30]
runtime_performance_constraints = [0, 0, 1.00,  1.11, 1.30]
memory_constraints = [0, 0, 1.00, 1.06, 1.21]
volatility_of_the_virtual_machine_environment = [0, 0.87, 1.00, 1.15, 1.30]
required_turnabout_time = [0, 0.94, 1.00, 1.07, 1.15]
analyst_capability = [1.46, 1.19, 1.00, 0.86, 0.71]
applications_experience = [1.29, 1.13, 1.00, 0.91, 0.82]
software_engineer_capability = [1.42,  1.17, 1.00, 0.86, 0.70]
virtual_machine_experience = [1.21,  1.10, 1.00, 0.90, 0]
programming_language_experience = [1.14,  1.07, 1.00, 0.95, 0]
application_of_software_engineering_methods = [1.24,  1.10, 1.00, 0.91, 0.82]
use_of_software_tools = [1.24,  1.10, 1.00, 0.91, 0.83]
required_development_schedule = [1.23,  1.08, 1.00, 1.04, 1.10]

organic_small_up = [0.06, 0.16, 0.26, 0.42, 0.96]
organic_mid_up = [0.06, 0.16, 0.24, 0.38, 0.22]
s_det_mid_up = [0.07, 0.17, 0.25, 0.33, 0.25]
s_det_large_up = [0.07, 0.17, 0.24, 0.31, 0.28]
embaded_large_up = [0.08, 0.18, 0.25, 0.26, 0.31]
embaded_xlarge_up = [0.08, 0.18, 0.24, 0.24, 0.34]

organic_small_tp = [0.10, 0.19, 0.24, 0.39, 0.18]
organic_mid_tp = [0.12, 0.19, 0.21, 0.34, 0.26]
s_det_mid_tp = [0.20, 0.26, 0.21, 0.27, 0.26]
s_det_large_tp = [0.22, 0.27, 0.19, 0.25, 0.29]
embaded_large_tp = [0.36, 0.36, 0.18, 0.18, 0.28]
embaded_xlarge_tp = [0.40, 0.38, 0.16, 0.16, 0.30]

sofConst = ["Plan & Requirement: ",
            "Design: ",
            "Detail Design: ",
            "Code & Test: ",
            "Integration & Test: "
            ]

informations = ["Select Required Software Reliability: ",
                "Select Size of Application Database(Select between Low to Very High): ",
                "Select Complexity of The Product: ",
                "Select Runtime Performance Constraints(Select between Nominal to Very High): ",
                "Select Memory Constraints(Select between Nominal to Very High): ",
                "Select Volatility of the virtual machine environment(Select between Low to Very High): ",
                "Select Required turnabout time(Select between Low to Very High): ",
                "Select Analyst capability: ",
                "Select Applications experience: ",
                "Select Software engineer capability: ",
                "Select Virtual machine experience(Select between Very Low to High): ",
                "Select Programming language experience(Select between Very Low to High): ",
                "Select Application of software engineering methods: ",
                "Select Use of software tools: ",
                "Select Required development schedule: "
                ]


def selectConstants(option, value):
    if option == 0:
        constants.append(required_software_reliability[value])
    elif option == 1:
        constants.append(size_of_application_database[value])
    elif option == 2:
        constants.append(complexity_of_the_product[value])
    elif option == 3:
        constants.append(runtime_performance_constraints[value])
    elif option == 4:
        constants.append(memory_constraints[value])
    elif option == 5:
        constants.append(volatility_of_the_virtual_machine_environment[value])
    elif option == 6:
        constants.append(required_turnabout_time[value])
    elif option == 7:
        constants.append(analyst_capability[value])
    elif option == 8:
        constants.append(applications_experience[value])
    elif option == 9:
        constants.append(software_engineer_capability[value])
    elif option == 10:
        constants.append(virtual_machine_experience[value])
    elif option == 11:
        constants.append(programming_language_experience[value])
    elif option == 12:
        constants.append(application_of_software_engineering_methods[value])
    elif option == 13:
        constants.append(use_of_software_tools[value])
    elif option == 14:
        constants.append(required_development_schedule[value])


def detailedCocomo(E, T):
    cons = []
    cons3 = []
    if(E < 32000):
        for j in organic_small_up:
            flag = round((j * E), 4)
            cons.append(flag)
        for k in organic_small_tp:
            flag = round((k * T), 4)
            cons3.append(flag)
        return cons, cons3
    elif(E >= 32000 and E < 128000):
        for j in organic_mid_up:
            flag = round((j * E), 4)
            cons.append(flag)
        for k in organic_mid_tp:
            flag = round((k * T), 4)
            cons3.append(flag)
        return cons, cons3
    elif(E >= 128000 and E < 320000):
        for j in s_det_large_up:
            flag = round((j * E), 4)
            cons.append(flag)
        for k in s_det_large_tp:
            flag = round((k * T), 4)
            cons3.append(flag)
        return cons, cons3
    elif(E >= 320000):
        for j in embaded_xlarge_up:
            flag = round((j * E), 4)
            cons.append(flag)
        for k in embaded_xlarge_tp:
            flag = round((k * T), 4)
            cons3.append(flag)
        return cons, cons3


def relay_graph(a, b, c, d, kloc, color, EAF):
    cons = []
    cons2 = []
    effort, time = cocomo(a, b, c, d, kloc, 0, EAF)
    print(f"Effort required {effort} PM")
    print(f"Time required {time} months")
    cons, cons2 = detailedCocomo(effort, time)

    print("\n")
    print("Effort required in different phases")
    print("************************************************************\n")
    for i in range(0, 5):
        print(sofConst[i] + str(cons[i]) + " PM")
    effortArr = []
    timePoints = []
    effortPoints = []
    klocArr = []
    transEff = []
    transTi = []
    for i in range(1, kloc + 1):
        l1 = []
        l2 = []
        pointEffort = cocomo(a, b, c, d, i, 1, EAF)
        pointTime = cocomo(a, b, c, d, i, 2, EAF)
        l1, l2 = detailedCocomo(pointEffort, pointTime)
        effortPoints.append(l1)
        timePoints.append(l2)
        klocArr.append(i)

        transEff = transpose(effortPoints, transEff)
        transTi = transpose(timePoints, transTi)
    for i in range(0, 5):
        plt.plot(klocArr, transEff[i], color=colors[i],
                 linewidth=4, label=f"{sofConst[i]}: {cons[i]}")
        i += 1
    draw_curve(1)
    for i in range(0, 5):
        plt.plot(klocArr, transTi[i], color=colors[i],
                 linewidth=4, label=f"{sofConst[i]}: {cons2[i]}")
    print("\n")
    print("Development time in different phases")
    print("************************************************************\n")
    for i in range(0, 5):
        print(sofConst[i] + str(cons2[i]) + " Months")
    draw_curve(0)


def transpose(l1, l2):
    l2 = list(map(list, zip(*l1)))
    return l2


def draw_curve(flag):
    plt.legend(loc="upper right")
    plt.xlabel("KLOC")
    if flag == 1:
        plt.ylabel("Estimated Effort")
        plt.title("Effort versus product size")
    else:
        plt.ylabel("Estimated Time")
        plt.title("Time versus product size")
    plt.show()
    print("\n")


def cocomo(a, b, c, d, kloc, flag, EAF):
    effort = round((a * pow(kloc, b)), 4) * EAF
    time = round((c * pow(effort, d)), 4)
    if flag == 1:
        return effort
    if flag == 2:
        return time
    return effort, time


EAF = 1
for i in range(0, 15):
    print("\n")
    print("Very Low- Press 0\nLow - Press 1\nNominal - Press 2\nHigh - Press 3\nVery High - Press 4")
    flag = int(input(informations[i]))
    selectConstants(i, flag)

print("----------------------------------------------------------------------\n")
for i in constants:
    EAF = EAF * i

print("Effort Adjustment Factor: " + str(EAF) + "\n")
effortArr = []
klocArr = []
timeArr = []
for i in range(0, 3):
    if(i == 0):
        print("In Organic Mode")
        print("--------------------\n")
        effortArr.append(relay_graph(2.4, 1.05, 2.5, 0.38, kloc, 0, EAF))
        print("\n")
    elif(i == 1):
        print("In Semi Detached Mode")
        print("--------------------\n")
        effortArr.append(relay_graph(3.0, 1.12, 2.5, 0.35, kloc, 1, EAF))
        print("\n")
    elif(i == 2):
        print("In Embedded Mode")
        print("--------------------\n")
        effortArr.append(relay_graph(3.6, 1.20, 2.5, 0.32, kloc, 2, EAF))
        print("\n")
for i in range(1, kloc + 1):
    klocArr.append(i)
