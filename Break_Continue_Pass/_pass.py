i = 1

for i in range(1,11):
    print("position %d"%i)
    if i == 3:
        pass # It is a null operation
        print("Inside the pass block")
    
    if i == 4:
        print("Outside the pass block")