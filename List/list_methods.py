list1 = ['a','b','c','d']
list2 = ['Six',1,5,"Month"]
list3 = [1,2,3,4,5]

#_____________________LIST METHODS___________________


# Length Of - Gives the total length of the list
len(list1)

# Max Value - Returns item from the list with max value
max(list3)

# Min Value - Returns item from the list with min value
min(list3)


# append(obj) - appends an object to the list
y = list1.append([23,44,'Good'])

# count(obj) - returns count of how many times obj occurs in list
g = list1.count("a")

print(y)
print(g)