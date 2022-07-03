from prime_in_range import prime_numbers_in_range


def test_prime_number_in_range_1_10():
    lower = 1
    upper = 10
    result = prime_numbers_in_range(lower, upper)
    expected = [2, 3, 5, 7]

    assert len(result) == len(expected)
    for prime_number in expected:
        assert prime_number in result


def test_return_no_prime_number_if_range_1_1():
    lower = 1
    upper = 1
    result = prime_numbers_in_range(lower, upper)
    expected = []

    assert expected == result


def test_prime_number_in_neg_10_to_10():
    lower = -10
    upper = 10
    result = prime_numbers_in_range(lower, upper)
    expected = [2, 3, 5, 7]

    assert expected == result
