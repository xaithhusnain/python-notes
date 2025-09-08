print("hello world")

dict = {
    "table" : "a piece of furniture",
    "cat" : "a small animal",
    "list of facts & figures":["earth is round","sun sets in west"]
}

print(dict)
print(type(dict))
print(dict.keys())
print(dict.values())





classrooms = {"python", "java", "C++", "python", "javascript","java", "python", "java", "C++","C"}
print(classrooms)
print(len(classrooms))








marks = {}


a = int(input("enter your phy marks:"))
marks.update({"phy": a})

a = int(input("enter your maths marks:"))
marks.update({"maths": a})

a = int(input("enter your chem marks:"))
marks.update({"chem": a})

print(marks)




marks_dict = {}

for i in range(3):
    subject = input("Enter subject name: ")
    mark = float(input("Enter marks: "))
    marks_dict[subject] = mark

print("Dictionary of subjects and marks:")
print(marks_dict)




marks_dict = {}

for _ in range(3):
    subject = input("Enter subject name: ")
    mark = float(input("Enter marks: "))
    marks_dict.update({subject: mark})

print("Dictionary of subjects and marks:")
print(marks_dict)









a : int = 9
b : float = 9.0
c = set()
# c.add(a)
# print(c)
# c.add(b)
# print(c)


s = {9,"9.0"}
print(s)


x = {
    ("float",9.0),
    ("int",9)
}
print(x)





distinct_set = set()

# Add values with their types
distinct_set.add((type(9), 9))
distinct_set.add((type(9.0), 9.0))

print(distinct_set)