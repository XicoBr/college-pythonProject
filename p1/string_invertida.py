"""string_1 = 'world'
string_invertida = string_1[::-1]
print(string_invertida)"""

string = 'world'
string_invertida = ''
for char in string:
    string_invertida = char + string_invertida

print(string_invertida)
