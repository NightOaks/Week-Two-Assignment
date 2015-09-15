__author__ = 'Devin Simoneaux'

# CIS-125
# Loop Conversion
#
# Converts Fahrenheit to Celsius on multiples of 10 from 0-100.s

# Declare Magic Numbers and Constants

# LOOPCOUNTER = 2
# name = "bob"

# Write program code here

# Input

# Process

for F in range(0,101,10):
    D = F
    C = (F-32) * 5 / 9
    print(D, " Fahrenheit is equal to ", C, " Celsius.")

# Output