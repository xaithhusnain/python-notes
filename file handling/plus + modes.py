print("hello world")

f = open("demo.txt","r+")
data = f.read()
print(data)
f.close()

f = open("demo.txt","r+")
f.write("abcd")
f.close()



# in "r+" we can do both read and write 
# but here we have to use it wisely bcz 
# it when both function work a same time cursor got shift with these commands


f = open("demo.txt","r+")
f.write("abcd")
data = f.read()
print(data)
f.close()


# the above given code will first write\overwrite the first 4 leters 
# but in this case cursor will shift to the 5th position
# and if we read it after it then it will read it from 5th position








f = open("demo.txt","w+")
f.write("i am coder learning ML.")
data = f.read()
print(data)
f.close()


# when we are in "w+" mode and we first read it then it will wiped or truncate the whole data 







f = open("demo.txt","a+")
f.write("i am coder learning ML.")
data = f.read()
print(data)
f.close()




'''
r+ : read write || pointer at the start || no truncate

w+ : read write || no matter where is pointer bcz data gone wiped || truncate

a+ : read append || pointer at the end || no truncate

'''