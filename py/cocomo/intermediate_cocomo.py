import matplotlib.pyplot as plt

kloc = int(input("Enter total number of lines of code: \n"))
constants = []

colors = {
    0: 'red',
    1: 'orange',
    2: 'green'
}
effort = 0

required_software_reliability = [0.75, 0.88, 1.00, 1.15, 1.40]
size_of_application_database = [0, 0.94, 1.00, 1.08, 1.16]
complexity_of_the_product = [0.70, 0.85, 1.00, 1.15, 1.30]
runtime_performance_constraints = [0, 0, 1.00,	1.11,	1.30]
memory_constraints = [0, 0, 1.00, 1.06, 1.21]
volatility_of_the_virtual_machine_environment = [0, 0.87, 1.00, 1.15, 1.30]
required_turnabout_time = [0, 0.94, 1.00, 1.07, 1.15]
analyst_capability = [1.46, 1.19, 1.00, 0.86, 0.71]
applications_experience = [1.29, 1.13, 1.00, 0.91, 0.82]
software_engineer_capability = [1.42,	1.17,	1.00,	0.86,	0.70]
virtual_machine_experience = [1.21,	1.10,	1.00,	0.90, 0]
programming_language_experience = [1.14,	1.07,	1.00,	0.95, 0]
application_of_software_engineering_methods = [1.24, 1.10, 1.00, 0.91, 0.82]
use_of_software_tools = [1.24, 1.10, 1.00, 0.91, 0.83]
required_development_schedule = [1.23,	1.08,	1.00,	1.04,	1.10]

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


def relay_graph_effort(a, b, kloc, color, EAF):
    effort = cocomo(a, b, kloc, 0, EAF)
    effortArr = []
    klocArr = []
    for i in range(1, kloc + 1):
        effortArr.append(cocomo(a, b, i, 1, EAF))
        klocArr.append(i)

    plt.plot(klocArr, effortArr,
             color=colors[color], linewidth=4, label=f"E: {effort}")
    draw_curve(1)
    return effortArr


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


def cocomo(a, b, kloc, flag, EAF):
    effort = round((a * pow(kloc, b)), 4) * EAF
    if flag == 1:
        return effort
    print("Effort: " + str(effort) + " PM")
    return effort


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
        effortArr.append(relay_graph_effort(3.2, 1.05, kloc, 0, EAF))
    elif(i == 1):
        print("In Semi Detached Mode")
        effortArr.append(relay_graph_effort(3.0, 1.12, kloc, 1, EAF))
    elif(i == 2):
        print("In Embedded Mode")
        effortArr.append(relay_graph_effort(2.8, 1.20, kloc, 2, EAF))
for i in range(1, kloc + 1):
    klocArr.append(i)

for i in range(0, 3):
    plt.plot(klocArr, effortArr[i], color=colors[i], linewidth=4)
draw_curve(1)
