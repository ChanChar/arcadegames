__author__ = 'Charles C. Lee'

import math
# Multiple Choice

answers = "fdbcdbadedb"

for number, answer in enumerate(list(answers)):
    print("{}. {}".format(number+1, answer.upper()))

# Lab I

# Part A: Fahrenheit to Celsius

def ftoc():
    temperature_in_f = float(input("Enter temperature in Fahrenheit: "))
    temperature_in_c = (temperature_in_f - 32) * (5/9)
    print("The temperature in Celsius: {}".format(temperature_in_c))

# Part B: Area of a Trapezoid

def area_of_trapezoid():
    print("Area of a trapezoid")
    height = int(input("Enter the height of the trapezoid: "))
    bottom_length = int(input("Enter the length of the bottom base: "))
    top_length = int(input("Enter the length of the top base: "))

    area = 1/2 * (bottom_length + top_length) * height

    print("The area is: {}".format(area))

# Part C: Volume of a Sphere

def sphere_volume(radius=input("Enter the radius: ")):

    volume = (4 * math.pi * int(radius) ** 3) / 3
    print("The volume of the sphere is: {}".format(volume))
