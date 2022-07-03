def prime_numbers_in_range(lower, upper):
    prime_numbers = []
    for number in range(lower, upper + 1):
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                prime_numbers.append(number)

    return prime_numbers


if __name__ == "__main__":
    lower_value = int(input("Please, Enter the Lowest Range Value: "))
    upper_value = int(input("Please, Enter the Upper Range Value: "))

    prime_numbers = prime_numbers_in_range(lower_value, upper_value)

    print(f"Prime numbers in between {lower_value} to {upper_value} are:")
    for number in prime_numbers:
        print(number)
