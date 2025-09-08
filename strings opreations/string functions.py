print("hello world")

a = "hey $ coder,i am $ also a coder."


# str.endsWith()  #returns true if string ends with substr 
print(a.endswith("er."))



# str.capitalize()  #capitalizes 1st char
print(a.capitalize())
print(a)

#  here is a point that it dose not change the original string it createa new one with changes
# but if we want to change the original str we can store it again in the same str
a = a.capitalize()
print(a)



# a.replace( old, new )  #replaces all occurrences of old with new 
print(a.replace("coder","programmer"))
# we can also change  a single for in the whole str
print(a.replace("a","b"))



# str.find( word )  #returns 1st index of 1st occurrence 
print(a.find("coder"))
print(a.find("e"))




# str.count(“am“)  #counts the occurrence of substr in strin
print(a.count("am"))


# a = input("enter your name")
# print(len(a))

print(a.count("$"))

