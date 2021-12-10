"""Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number."""
def create_phone_number(n):
    f = "".join(map(str, n[0:3]))
    s = "".join(map(str, n[3:6]))
    t = "".join(map(str, n[6:10]))
    return "(" + f + ") " + s + "-" + t
def create_phones_number(n):
    #your code here
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
