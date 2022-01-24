import re

regex = "\d"
number = "ab12345cd"
print(re.match(regex, number))

print(re.match("[A-Z][a-z]", "Abcdefg"))