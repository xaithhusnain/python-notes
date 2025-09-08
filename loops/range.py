print("hello world")


'''
Range functions returns a sequence of numbers, starting from 0 by default, and increments by
1 (by default), and stops before a specified number.(sq( start?, stop, step?) 

'''

print(range(5))

sq = range(5)
print(sq[0])
print(sq[1])
print(sq[2])
print(sq[3])

for i in sq:
    print(i)

for i in range(5):
    print(i)

for i in range(0,5):
    print(i)

for i in range(1,5):
    print(i)


for i in range(2,10,2):
    print(i)