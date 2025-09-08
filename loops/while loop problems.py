n = 5
i = 1
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i += 1

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")



sqaure = []
i = 1
while i <= 10:
    sqaure.append(i**2)
    i += 1
print(sqaure)


a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

for i in a:
    if 36 in a:
        print("yes")
        break
else:
    print("no")

a = None
while a == True:
    if 36 in a:
        print("yes")
        break
else:
    print("no")



idx = 0
while idx < len(a):
    print(idx)
    idx += 1



idx = 0
while idx < len(a):
    print(a[idx])
    idx += 1




x = 366
idx = 0

while idx < len(a):
    if a[idx] == x:
        print("found at idx,", idx)
        break
    idx += 1
else:
    print("not found")