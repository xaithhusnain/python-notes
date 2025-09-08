print("hello world")

a = 2
b = 3
sum = a+b
print(sum)

# lines of code

a = 6
b = 9
sum = a+b
print(sum)

# lines of code

a = 12
b = 33
sum = a+b
print(sum)


def calc_sum(a,b):
    return a+b

sum = calc_sum(46,5)
print(sum)


def calc_sum(a,b):
    print(a+b)

calc_sum(6,5)



def print_hello():
    print("hello!")

output = print_hello()
print(output)          # its print NONE that shows it returns nothing




def avg(a,b,c):
    sum = a+b+c
    print(sum/3)

avg(1,2,3)




def avg(a,b,c):
    sum = a+b+c
    return sum/3

average = avg(11,222,34)
print(average)