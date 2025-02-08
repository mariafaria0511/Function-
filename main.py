#area of a circle: Pi * r^2
# Values: 10, 6, 24, 2, 1

def solveMyValue(number):
    import math
    answer = math.pi * (number * number)
    rounded_number = round(answer, 2)
    return rounded_number

myNumber = solveMyValue(10)
print("When I call the function it returned", myNumber)


#Money
def solveMyValue(money, tax):
    answer = money + (money * (tax/100))
    rounded_number = round(answer, 2)
    return rounded_number

myNumber = solveMyValue(20, 6)
print("When I call the function it returned", myNumber)


#Temperature
def solveMyValue(fahrenheit):
    answer = (fahrenheit - 32) * (5/9)
    rounded_number = round(answer, 4)
    return rounded_number
