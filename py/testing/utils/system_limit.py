# importing libraries
import signal
import resource

# checking time limit exceed


def time_exceeded(signo, frame):
    print("Time's up !")
    raise SystemExit(1)


def set_max_runtime(seconds):
    # setting up the resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


# max run time of 15 millisecond
if __name__ == '__main__':
    set_max_runtime(15)
    while True:
        pass
