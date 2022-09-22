# Python Strings - A sequence of characters enclosed in single or double quotes

text = "Python is a programming language"

text1 = 'I love python'

# Accessing values in strings
print(text[0]) # P
print(text[4]) # o
print(text[0:6]) # Python

# ___________________String operators___________________

# concatenation
w1 = 'Python '
w2 = 'Language'

print(w1 + w2) # Python Language

# repetition
print(w1*3) # Python Python Python

# slice
print(w1[2]) # t

# range slice
print(w1[0:3]) # Pyt

# membership
print('P' in w1) # True
print('P' in w2) # False