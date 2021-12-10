"""Simple, remove the spaces from the string, then return the resultant string."""
def no_space(s):
    return s.replace(' ', '')

def removeSpaces(string):
    list = []
    # Traverse the given string. If current character
    # is not space, then place it at index 'count++'
    for i in range(len(string)):
        if string[i] != ' ':
            list.append(string[i])

    return ''.join(list)
