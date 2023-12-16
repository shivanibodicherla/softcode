# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 20:09:01 2023

@author: shiva
"""

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Error: division by zero",
}

def calculate(num1, num2, operation):
    result = operations[operation](num1, num2)
    return result

while True:
    try:
        num1 = float(input(" Please Enter your first number: "))
        num2 = float(input(" Please Enter your second number: "))
        operation = input("Please Enter operation that you want to perform (addition(+), subtraction(-), multiplication(*), division(/)): ")
        result = operations[operation](num1, num2)
        print("Result for the given numbers is :", result)
        break
    except ValueError:
        print("Error: invalid input. Please enter a number.")