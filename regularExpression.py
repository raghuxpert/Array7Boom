import re

txt = "The rain in The Spain"
x = re.findall("^The", txt)
print(type(x))
print(x)

