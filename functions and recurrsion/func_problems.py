print("hello world")

cities = ["islamabad","lahore","Quetta","karachi","Peshawar","Multan"]
heroes = ["Quaid-e-Azam","Allama Iqbal","Abdul Sattar Eidhi","Doctor Abdul Qadeer khan"]


def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)


def print_elements(list):
    for i in list:
        print(i,end=" ")
    print()

print_elements(cities)
print("\n")
print_elements(heroes)




def factorial(n):
    f = 1
    i = 1
    while i <= n:
        f = f*i
        i +=1
    print(f)


def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f*i
    print(f)

factorial(6)






def USD_to_INR(usd):
    inr = usd*87
    print(f"{usd} USD = {inr} INR")

USD_to_INR(20)



def odd_even(num):
    if num%2 == 0:
        print("EVEN")
    else:
        print("ODD")

odd_even(8)
