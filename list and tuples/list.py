print("hello world")

marks = [23,34,56,67,85,90,]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[3])
print(marks[5])


# list are mutable 

data = ["ali",90,"BSCS",92.2,]
print(data)
data[0] = "husnian"
print(data)




# list slicing

# like str we can also acess elements by its index

print(marks[0:4])
print(marks[:4])

print(marks[2:6])
print(marks[2:])

print(marks[-4:-1])




#list methods
marks.append(7)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(4,800)
print(marks)


list = [2, 1, 3, 1]
list.remove(1)  #removes first occurrence of element
print(list)
list.pop(2)  #removes element at idx
print(list)