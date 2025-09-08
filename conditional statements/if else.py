print("hello world")

# if elif else structure
'''
if(condition) :
    Statement1
elif(condition):
    Statement2
else:
    StatementN

'''


age = 18
if (age >= 18):
    print("Eligible for driving license.")
else:
    print("Not eligible for driving license.")


light = "green"

if light == "red":
    print("stop")
elif light == "yellow":
    print("Ready to go.")
elif light == "green":
    print("go now.")



# in case of if all if statements works.

a= 5
if a>2:
    print("greater than 2")
if a>3:
    print("greater than 3")


#in case of if elif only 1 statment works if 1 becames true then all other will neglect

if a>2:
    print("greater than 2")
elif a>3:
    print("greater than 3")



marks = 89

if marks>=90 and marks<100:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade B")
elif marks>=70 and marks<80:
    print("Grade C")
elif marks>=60 and marks<70:
    print("Grade D")
else:
    print("Fail")





# nested if else

age = 21
# nationality = "Pakistan".lower()
# if age >= 21:
#     if nationality == "pakistan".lower():
#         print("eligible for passport.")
#     else:
#         print("not eligible")


# a = 12
# if a%2==0:
#     print("even")
# else:
#     print("odd")



a = 12
b = 37
c = 55

if a>b:
    greater = a
else:
    greater = b

# if greater > c:
#     print("greater number is:", greater)
# else:
#     print("greater number is:", c)



# print(max(a,b,c))


# if a>b and a>c:
#     print("greater number is:", a)
# elif b>a and b>c:
#     print("greater number is:", b)
# else:
#     print("greater number is:", c)



a = 148
if a%7==0:
    print("yes its a multiple of 7")
else:
    print("not the multiple of 7")