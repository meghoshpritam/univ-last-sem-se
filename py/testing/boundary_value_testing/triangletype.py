# https://www.geeksforgeeks.org/performing-bva-testing-using-pytest/
# import math

class Error(BaseException):
    pass


class OutOfRangeError(Error):
    def __init__(self, message):
        self.message = message


class TriangleError(Error):
    def __init__(self, message):
        self.message = message


def checkRange(a, b, c):
    if a < 10 or a > 50:
        raise OutOfRangeError('A is out of the given range')
    if b < 10 or b > 50:
        raise OutOfRangeError('B is out of the given range')
    if c < 10 or c > 50:
        raise OutOfRangeError('C is out of the given range')


def checkTriangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        raise TriangleError('Triangle cannot be formed with these sides')


def triangleType(a, b, c):
    checkRange(a, b, c)
    checkTriangle(a, b, c)
    # s = (a + b+c)/2
    # ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
    # inradius = ar / s
    if(a == b and b == c):
        return "Equilateral Triangle"
    elif(a == b or a == c or b == c):
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"


def main():
    try:
        print("Enter the sides of the triangle in range [10-50]")

        a = int(input('Enter Side A:'))
        b = int(input('Enter Side B:'))
        c = int(input('Enter Side C:'))
    except ValueError as v:
        print(v + " Raised :Input is not an integer.")
        exit(0)
    try:
        checkRange(a, b, c)
    except OutOfRangeError as e:
        print("OutOfRangeError:" + e.message)

    try:
        checkTriangle(a, b, c)
    except TriangleError as e:
        print('TriangleError:' + e.message)

    typeOfTriangle = triangleType(a, b, c)

    print("The triangle is: " + typeOfTriangle)


if __name__ == "__main__":
    main()
