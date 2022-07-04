import matplotlib.pyplot as plt
kloc = int(input("Enter total number of lines of code(KLOC): "))

colors = {
    0: 'red',
    1: 'orange',
    2: 'green'
}
effort = 0


def relay_graph_effort(a, b, c, d, kloc, color):  # calculate effort and time
    effort, time = cocomo(a, b, c, d, kloc, 0)
    effortArr = []
    klocArr = []
    # klocnew = kloc + 10
    for i in range(1, kloc + 1):
        effortArr.append(cocomo(a, b, c, d, i, 1))
        klocArr.append(i)

    plt.plot(klocArr, effortArr,
             color=colors[color], linewidth=4, label=f"E: {effort} | T: {time}")
    draw_curve(1)
    return effortArr


def relay_graph_time(a, b, c, d, kloc, color):
    effort, time = cocomo(a, b, c, d, kloc, 3)
    timeArr = []
    klocArr = []
    # klocnew = kloc + 10
    for i in range(1, kloc + 1):
        timeArr.append(cocomo(a, b, c, d, i, 2))
        klocArr.append(i)

    plt.plot(klocArr, timeArr, color=colors[color],
             linewidth=4, label=f"E: {effort} | T: {time}")
    draw_curve(0)
    return timeArr


def draw_curve(flag):  # Draw graph
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


def cocomo(a, b, c, d, kloc, flag):

    effort = round((a * pow(kloc, b)), 4)
    time = round((c * pow(effort, d)), 4)
    personRequired = round((effort / time), 4)
    productivity = round((kloc / effort), 4)
    if flag == 1:
        return effort
    if flag == 2:
        return time
    if flag == 3:
        return effort, time
    print("Effort: " + str(effort) + " PM")
    print("Time: " + str(time) + " months")
    print("Average person required: " + str(personRequired) + " persons")
    print("Productivity: " + str(productivity) + " KLOC/PM")
    return effort, time


effortArr = []
klocArr = []
timeArr = []
for i in range(0, 3):
    if(i == 0):
        print("In Organic Mode")
        effortArr.append(relay_graph_effort(2.4, 1.05, 2.5, 0.38, kloc, 0))
        timeArr.append(relay_graph_time(2.4, 1.05, 2.5, 0.38, kloc, 0))
    elif(i == 1):
        print("In Semi Detached Mode")
        effortArr.append(relay_graph_effort(3.0, 1.12, 2.5, 0.35, kloc, 1))
        timeArr.append(relay_graph_time(3.0, 1.12, 2.5, 0.35, kloc, 1))
    elif(i == 2):
        print("In Embedded Mode")
        effortArr.append(relay_graph_effort(3.6, 1.20,  2.5,  0.32, kloc, 2))
        timeArr.append(relay_graph_time(3.6, 1.20,  2.5,  0.32, kloc, 2))
for i in range(1, kloc + 1):
    klocArr.append(i)

for i in range(0, 3):
    plt.plot(klocArr, effortArr[i], color=colors[i], linewidth=4)
    i += 1
draw_curve(1)

for i in range(0, 3):
    plt.plot(klocArr, timeArr[i], color=colors[i], linewidth=4)
    i += 1
draw_curve(0)
