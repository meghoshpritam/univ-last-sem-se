import matplotlib.pyplot as plt


def nordan(k, td, t):
    p = 2 * (pow(td, 2))
    q = pow(t, 2)
    r = pow(2.7182, (-q / p))
    return (k / pow(td, 2)) * t * r


def nordan_relay_graph(k, td, t):
    project_duration = 3 * int(td)
    y = [round(nordan(k, td, time), 5) for time in range(0, project_duration)]

    plt.plot(y, color="blue", linewidth=4, label="Effort respect to time")
    plt.vlines(
        x=td,
        ymin=0,
        ymax=round(nordan(k, td, td), 5),
        color="green",
        linestyle="dashed",
        linewidth=4,
        label=td,
    )
    plt.vlines(
        x=t,
        ymin=0,
        ymax=round(nordan(k, td, t), 5),
        color="red",
        linestyle="dashed",
        linewidth=4,
        label="t",
    )
    plt.legend(loc="upper right")
    plt.xlabel("time")
    plt.ylabel("Effort per unit time")
    plt.title("r_curve")
    plt.show()


if __name__ == "__main__":
    k = float(input("Enter area under the curve(k): "))
    td = float(input("Enter the maximum value of curve(td): "))
    t = float(input("Enter effort time(t) in month: "))

    print("\nRequired effort at time t is, E=",
          round(nordan(k, td, t), 5), "PM\n\n")
    nordan_relay_graph(k, td, t)
