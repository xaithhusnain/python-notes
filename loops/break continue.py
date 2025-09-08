'''
Break : used to terminate the loop when encountered.
Continue : terminates execution in the current iteration & continues execution of the loop
with the next iteration.

'''


i = 0
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

print("loop ended")



i = 0 
while i <= 10:
    if i == 7:
        i += 1
        continue
    print(i)
    i += 1

print("loop ended")


i = 0 
while i <= 10:
    if i%2 == 0:
        i += 1
        continue
    print(i)
    i += 1





 