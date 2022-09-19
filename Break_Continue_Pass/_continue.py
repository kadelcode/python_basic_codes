i = 0

for i in range(0,10):
    i += 1
    print("%d"%(i))
    if i == 6: 
        continue # This statement skips the remaining lines of code of the loop, and starts with the next iteration.
    print("A number!")