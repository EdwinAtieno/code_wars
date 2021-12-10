"""Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string."""
#code
def add_binary(a,b):
    #your code here
    c=bin(a+b).replace("0b", "")
    bin_c = str(c)
    return bin_c










