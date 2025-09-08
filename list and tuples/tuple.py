print("hello world")

tup = (87, 64, 33, 95, 76)

# as its imutable so changes are not allowed

# tup[0] = 43 #NOT allowed in python



# tuple indexing

print(tup[0])
print(tup[3])
print(tup[1:3])
print(tup[5])    # out of range




# empty tuple

a = ()
print(a)
print(type(a))



# single element tuple

# b = (1)
# print(b)
# print(type(b))

# in case of single element case we have to put a comma a after it other its not a tuple

a = (1,)
print(a)
print(type(a))





tup = (2,5,3,1,4,1)
print(tup.index(3))  #returns index of first occurrence
print(tup.count(1))  #counts total occurrences 
print(tup.index(1))





