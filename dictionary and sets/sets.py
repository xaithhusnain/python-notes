print("hello world")

a = {1,2,3,4,5,"hello","hello",78.09,True,"1137"}
print(a)
print(type(a))
print(len(a))



# empty set

a = {}  # its wrong syntax bcz it is ued for dectionary
print(type(a))


# correct syntax 

a = set()
print(type(a))


a = ()     # if we did not write set keyword it will be a tuple 
print(type(a))






# set methods

a = {1,2,3,4,5,"hello",78.09,True,"1137"}

a.add("coding")
print(a)
a.remove("coding")
print(a)
# a.clear()
# print(a)
a.pop()
print(a)

'''
Set is the collection of the unordered items. 
Each element in the set must be unique & immutable.
set is mutable but its elements are immutable
'''





# Union & intersection methods in set

set1 = {1,2,3}
set2 = {2,3,4,5}

print(set1.union(set2))
print(set1.intersection(set2))