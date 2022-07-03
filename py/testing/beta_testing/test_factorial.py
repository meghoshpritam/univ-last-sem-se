import signal
import resource
from decimal import Underflow
import pytest
from factorial import factorial


def time_exceeded(_, __):
    raise SystemExit(1)


def set_max_runtime(seconds):
    # setting up the resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


def test_check_factorial_of_5():
    input_value = 5
    result = factorial(input_value)
    expected = 120

    assert result == expected


def test_check_factorial_of_0():
    input_value = 0
    result = factorial(input_value)
    expected = 1

    assert result == expected


def test_check_factorial_of_1():
    input_value = 1
    result = factorial(input_value)
    expected = 1

    assert result == expected


def test_throw_underflow_error_for_factorial_of_neg_10():
    input_value = -10

    with pytest.raises(Underflow):
        factorial(input_value)


def test_thales_more_than_5_sec_for_factorial_of_a_large_value():
    input_value = 9878559745

    with pytest.raises(SystemExit):
        set_max_runtime(5)
        factorial(input_value)
