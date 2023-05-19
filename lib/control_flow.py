#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == 'admin' and password == 'admin':
        return True
    else:
        return False

    

def hows_the_weather(temperature):
    # your code here
    if temperature < 10:
    # if temperature is less than 10
        return "it's cold"
    elif temperature < 20:
    # if temperature is between 10 and 20
        return "it's mild"
    elif temperature < 30:
    # if temperature is between 20 and 30
        return "it's warm"
    elif temperature < 40:
    # if temperature is between 30 and 40
        return "it's hot"
    elif temperature < 50:
    # if temperature is between 40 and 50
        return "it's very hot"
    elif temperature < 60:
    # if temperature is between 50 and 60
        return "it's very hot"
    

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)
    


def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return "invalid operation"
    
