'''
Nested for loop: Having a for loop in a for loop
'''

# initialization
i = 1
j = 1

for i in range(1,6):
    print()
    for j in range(1,i+1):
        print("*",end="")