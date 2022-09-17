'''
Multiplication table for a particular number
'''

# initialization
i = 1
x = int(input('Enter a number for the Multiplication table:'))

while (i < 13):
    print("%d X %d = %d"%(x,i,x*i))
    i = i + 1

# An else block can be used with the while loop
# It is executed if the condition of the while loop becomes false
else:
    print("Program Execution Stopped!")