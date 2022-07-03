import matplotlib.pyplot as plt


def jensen(c, t, k):
    L = c * t * pow(k, 1 / 3)
    return L


def jensen_relay_graph(c, t, k):
    project_duration = 3 * int(t)
    y = [round(jensen(c, time, k), 5) for time in range(0, project_duration)]

    plt.plot(y, color="blue", linewidth=4,
             label="Project size respect to time")
    plt.legend(loc="upper left")
    plt.xlabel("time")
    plt.ylabel("product size")
    plt.title("Jensen replay graph")
    plt.show()


if __name__ == "__main__":
    c = float(input("Enter the effective technology  constant: "))
    t = float(input("Enter the development time: "))
    k = float(input("Enter the effort needed to develop: "))
    print("\nThe product size(L) is = ", round(jensen(c, t, k), 5), "KLOC")
    jensen_relay_graph(c, t, k)
