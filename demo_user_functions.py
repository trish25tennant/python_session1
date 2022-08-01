#! /bin/python
# Name: demo_lotto.py
# Author: Trish Saha
# Version: 1.0
# Description: This program will demo how to define, call and pass parameters into a user function

"""
    Lottery Generator
"""
import sys

message = "hello" + " " + "world"
print(message)

def say_hello():
    message = "hello" + " " + "world"
    print(message)
    return None

say_hello()

def say_hello1(greeting, recipient):
    message = f"{greeting} {recipient}"
    print(message)
    return None

say_hello1("ciao", "amici") #Positional parameter passing
say_hello1(greeting="hola", recipient= "amigos")# Named parameter passing
say_hello1(recipient = "mes amies", greeting= "bonjour") #Named parameter passing (in different order)
say_hello1("namaste", recipient= "dosto") # Mixed parameter passing

# Example of a user function definition with parameter
# passing and default values
def say_hello2(greeting = "ni ha", recipient = "peng yu"):
    """
        Display a greeting
    """
    message = f"{greeting} {recipient}"
    print(message)
    return None

def main():
    """ The main function"""
    say_hello2()

if __name__== "__main__":
    # Execute if ran directly as a program
    # Ignore this is if imported as a module
    main()
    sys.exit(0)
