print("hello world")

#  Loops are used for sequential traversal. For traversing list, string, tuples etc.

nums = [1,2,3,4,5,6]
for i in nums:
    print(i)

fruits = ["mango","apple","banana","peach"]
for i in fruits:
    print(i)


nums = (1,2,3,4,5,6)
for i in nums:
    print(i)


a = "abcdefghij"
for i in a:
    print(i)


nums = (1,2,3,4,5,6)
for i in nums:
    if i == 5:
        print("5 found")
        break
    print(i)
else:
    print("ended")

# else run in those cases in which loop runs compeletely but in other
# like in break cases else will no executed



