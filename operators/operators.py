a = 40
b = 20

# Arithmetic Operators
a + b # Addition
a - b # Substraction
a / b # Division
a * b # Multiplication
a % b # Modulus
a ** b # Exponent
a // b # Floor Division

# Comparison Operators
a == b # Equal to
a != b # Not equal
a <= b # Less than or equal to
a >= b # Greater than or equal to
a > b # Greater than
a < b # Less than


# Assignment Operators
a = b # a = b
a += b # a = a + b
a -= b # a = a - b
a *= b # a = a * b
a %= b # a = a % b
a **= b # a = a**b
a //= b # a = a // b

# Logical Operators (used primarily in the expression evaluation to make a decision)
(a > b) and (b > a)
(a > b) or (b > a)
z = not(a > b)
print(z)

# Bitwise Operators (performs bit by bit operation)
a & b # Binary AND
a | b # Binary OR
a ^ b # Binary XOR
~(a) # Negation
a << b # Left Shift
a >> b # Right Shift


# Membership Operators (used to check the membership of value inside a data structure)
data = ['a','b','c','d','e']
'a' in data # True
'a' not in data # False


# Identity Operators
a is b # False
a is not b # True