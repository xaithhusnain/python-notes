a = "hello world"
print(len(a))

# slicing means to access a part of string

# syntax
#  str[ starting_idx : ending_idx ]     #ending idx is not include

print(a[2:5])


# if we did not pass the starting idx it will consider it 0
print(a[:5])
print(a[0:5])


# if we did not pass the ending idx it will consider it equal to the length of str
print(a[2:])
# as the len of a is 11 
print(a[2:11])



# with negative slicing

print(a[-5:8])


# working format of negative positive index

'''

 h   e   l   l   o       w   o   r   l   d
 0   1   2   3   4   5   6   7   8   9   10   ← Positive indexes
-11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1    ← Negative indexes

'''