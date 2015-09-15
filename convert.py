__author__ = 'Devin Simoneaux'

# CIS-125
# Input Fahrenheit & Get Celsius Temperatures
#
# This program gets a temp in F from the user, and it converts and outputs the temp in C. 

# Declare Magic Numbers and Constants

# LOOPCOUNTER = 2
# name = "bob"

# Write program code here

# Input

F = eval(input("Please enter a temperature in Fahrenheit:"))

# Process

C = (F-32) * 5 / 9

# Output

print("The temperature ", F, " in Fahrenheit is equal to ", C, " Celsius")