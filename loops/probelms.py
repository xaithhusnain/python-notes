print("hello world")



n = 1
i = 0
sum = 0
while i <= n:
    sum = sum+i
    i +=1
print(sum)


n = 10
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)




n = 5
f = 1
for i in range(1,n+1):
    f *= i
print(f)

if n == 0:
    print(f)
else:
    for i in range(1,n+1):
        f = f*i
    print(f)




i = 1
while i <= n:
    f = f*i
    i +=1
print(f"the factorial of {n} is {f}")