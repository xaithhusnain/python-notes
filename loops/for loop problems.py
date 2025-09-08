print("hello world")

a = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,36)

for i in a:
    print(i)


for i in a:
    if i == 36:
        print(i)


x = 36
idx = 0

for i in a:
    if i == x:
        print("found at index,", idx)  # its called linear search as we searching in a line one by one
        break
    idx += 1