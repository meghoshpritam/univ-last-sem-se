from decimal import Underflow


def factorial(num):
    factorial_val = 1

    if num < 0:
        raise Underflow("Sorry, factorial does not exist for negative numbers")
    if num == 0:
        return factorial_val
    else:
        for i in range(1, num + 1):
            factorial_val = factorial_val*i
        return factorial_val


if __name__ == "__main__":
    input_value = int(input("Please, Enter the number to check factorial: "))

    factorial_value = factorial(input_value)

    print(f"Factorial of {input_value} is: {factorial_value}")
