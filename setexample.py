# Create a set of colors using curly braces
# This will print {'green', 'blue', 'red'}
colors = {'red', 'green', 'blue'}
print(colors)

# Create a set using the set() function
# This will print {'d', 'o', 'W', 'e', 'r', 'l', 'H'}
# Note that the duplicates got removed
A = set('HelloWorld')
print(A)

# Membership testing. This will print True
print('red' in colors)

# You can iterate over a set
# This will print: green blue red
for e in colors:
    print(e)

# Difference: all elements in A but not in B
# This will print {1, 2}
A = {1, 2, 3}
B = {3, 4, 5}
print(B - A)

# Union: all elements in A and B without the intersection
# This will print {1, 2, 3, 4, 5}
print(A | B)

# Intersection: elements in both A and B
# This will print {3}
print(A & B)

# Elements that are not in common
# This will print {1, 2, 4, 5}
print(A ^ B)

# You can use set comprehensions (similar to list comprehensions).
# Fore more information about list comprehensions you may check
# the references section. Here is an example
# This will print  {1, 2, 4, 5}
C = {e for e in A | B if e not in {3}}
