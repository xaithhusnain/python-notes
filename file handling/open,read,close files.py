print("hello world")


'''
We have to open a file before reading or writing.

f = open( “file_name”, “mode”)

sample.txt
demo.docx

r : read mode
w : write mode

data = f.read( )

f.close( )

'''



f = open("demo.txt","r")
content = f.read()
print(content)
f.close()


# we can also use multiple modes at a time 

f = open("demo.txt","rt")
content = f.read()
print(content)
f.close()

# both will give same output bcz "t" is emplicitly added or we can say it is by default







f = open("demo.txt","r")
content = f.readlines()
print(content)
f.close()




f = open("demo.txt","r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
f.close()

# we can read all data also line by line and also all lines at once






f = open("demo.txt","r")
content = f.read()
print(content)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
f.close()


# but if we already read data whole after that we can't it read line by line bcz its prints nothing 
# this is happen bcz here is a concept of reading with cursor 
# when we read all data already then cursor\pointer with came at the end 
# and only the print the newline character \n  which print a newline always

# same thing happen in the case of read line by line when we read first line it done the task 
# and came to the end after that read second line and came to the end 
# after if there is no line it will print empty line every time 





f = open("demo.txt","r")
content = f.read(6)
print(content)
f.close()

# we can also read data by giving parameters
# here we give 6 then it will print only first 6 letters



