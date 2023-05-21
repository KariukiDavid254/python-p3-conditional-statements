# control_flow.py

def admin_login(username, password):
    if username == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature <= 32:
        return "It's freezing out there!"
    elif temperature >= 90:
        return "It's too dang hot out there!"
    elif temperature >= 70:
        return "It's perfect out there!"
    elif temperature >= 50:
        return "It's a little chilly out there!"
    else:
        return "It's brisk out there"

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation!"
