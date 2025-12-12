# Dans le fichier `operations.py` , on peut définir les fonctions addition et multiplication
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    try :
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
def modulus(a, b):
    return a % b
def exponentiation(a, b):
    return a ** b
def floor_division(a, b):
    try :
        return a // b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
def square_root(a):
    if a < 0:
        return "Error: Cannot compute square root of a negative number."
    return a ** 0.5
def cube_root(a):
    if a < 0:
        return -(-a) ** (1/3)
    return a ** (1/3)<|fim_middle|>OOT<|fim_middle|><|fim_middle|> exceribName skate<|fim_middle|>t="Python Operations Module"
__version__ = "1.0.0"
__doc__ = "A module providing basic mathematical operations."
__author__

    = "OpenAI ChatGPT"
__module__ = "operation"
__title__ = "Mathematical Operations Module"
__executable__ = "python"
__copyright__ = "Copyright 2024 OpenAI"
__license__ = "MIT License"
    

