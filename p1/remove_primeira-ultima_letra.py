# Remove First and Last Character

def remove_char(s):

    return '' if len(s) <= 2 else s[1:-1]


string = 'country'
print(remove_char(string))
