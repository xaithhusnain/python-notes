print("hello world")

# Assigning a default value to parameter, which is used when no argument is passed.


def avg(a,b,c):
    sum = a+b+c
    return sum/3

average = avg(11,222,34)
print(average)


'''
note: all parameters with default values must come after the parameters without defaults.

'''

def avg(a,b=1,c=1):
    sum = a+b+c
    return sum/3

average = avg(2,4,6)
print(average)



def avg(a=1,b=1,c=1):
    sum = a+b+c
    return sum/3

average = avg(2,4,6)
print(average)

