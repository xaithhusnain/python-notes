print("hello world")

# When a function calls itself repeatedly.

def show(n):
    print(n)

show(5)

def show(n):
    if n==0:      # base case
        return     # when return nothing it known as control return
    print(n)
    show(n-1)    # recursive case
    print("end")

show(5)




def fact(n):
    if (n == 0 or n == 1):
        return 1
    return n * fact(n-1)

print(fact(7))