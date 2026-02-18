# Write code below 💖
import math


def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area


print(calculate_circle_area(3))
"""
Now that you can tell the difference between pure and impure functions, let’s try it out.

Create a pure function to calculate the area of a circle given its radius.

Define a calculate_circle_area() function that takes the radius of the circle as input.
Compute the area of the circle using the formula: area=π∗r^2  .
Return the result
"""


""""
 A pure function is a function whose output derives solely from its input values, without side effects. They always return the same result, making them reliable and testable.

Global variables are defined outside of a function, making them easy to find and change values. Pure functions do not use or refrence global variables. You can always count on pure functions to act the same.

Here is an example of an impure function vs. a pure function:

def impure_squared(number):
  result = number ** 2
  print('The square of', number, 'is', result)
  return result

def pure_squared(number):
  return number ** 2

Pay attention to the syntax:

The pure function only returns the squared value of number.
The impure function prints something to the terminal (the side effect).
"""
