# initialization
i = 1

for i in range(1,10):
    print(i)
    i += 1


'''program to print the table of a given number'''
#initialization
j = 1
num = int(input("Enter a number for its multiplication table: "))
for j in range(1,13):
    print("%d x %d = %d"%(num, j, num*j))
    