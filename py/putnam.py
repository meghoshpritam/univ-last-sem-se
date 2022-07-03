import matplotlib.pyplot as plt

tcs = [2, 8, 11]
colors = {
    2: 'red',
    8: 'orange',
    11: 'green'
}


def putnam(tc, effort, time):
    return tc * pow(effort, 1/3) * pow(time, 4/3)


def putnam_relay_graph(tc, effort, time):
    project_duration = 3 * int(time)
    y = [round(putnam(tc, effort, _time), 5)
         for _time in range(0, project_duration)]

    plt.plot(y, color=colors[tc], linewidth=4,
             label=f"tc: {tc} | product size: {putnam(tc, effort, time)}")
    plt.legend(loc="upper left")
    plt.xlabel("time")
    plt.ylabel("product size")
    plt.title(f"tc: {tc} | effort: {effort} | time: {time}")
    plt.show()


def putnam_relay_graph_all(effort, time):
    project_duration = 3 * int(time)
    for tc in tcs:
        y = [round(putnam(tc, effort, _time), 5)
             for _time in range(0, project_duration)]

        plt.plot(y, color=colors[tc], linewidth=4,
                 label=f"tc: {tc} | product size: {putnam(tc, effort, time)}")
    plt.legend(loc="upper left")
    plt.xlabel("time")
    plt.ylabel("product size")
    plt.title(f"Putnam relay graph")
    plt.show()


if __name__ == "__main__":
    effort = int(
        input("Enter effort(developers) need to develop the software: "))
    time = int(input("Enter estimated time for develop a software(in months): "))

    for record in tcs:
        product_size = putnam(record, effort, time)
        print(f"For tc: {record}, the Product size id {product_size}")
        putnam_relay_graph(record, effort, time)
    putnam_relay_graph_all(effort, time)
