print("hello world")

info = {
    "key" : "value",
    "name" : "ali",
    "student" : "BSCS",
    "learning" : "coding",
    "marks" : 874,
    "Is adult" : True
}

print(info)
print(info["name"])
print(info["Is adult"])
print(info["marks"])



# we can also store a list or tuple in a dict as a value
# dic are unordered bcz it has not a index system as list str and tuple
info = {
    "key" : "value",
    "name" : "ali",
    "name" : "husnain",
    "student" : "BSCS",
    "learning" : "coding",
    "subjects" : ["pyhton","java","c++","maths"],
    "marks" : (80,87,92,89)
}

print(info)
print(info["subjects"])
print(info["marks"])
print(info["name"])

print(info["religion"])  #it will create a key error which key not exist



# we can replace a value of a key 

info["learning"] = "programing"
print(info["learning"])

# create a new key value

info["college"] = "kips"
print(info["college"])



# creating a null dict

null_dict = {}
print(null_dict)





# nested dictionary

# nesteddict={
#     "name":"harry",
#     "class":10,
#     "subjects":{
#         "maths":89,
#         "physics":90,
#         "english":87,
#         "chemistry":96
#     }
# }

# print(nesteddict["subjects"])
# print(nesteddict["subjects"]["physics"])








# dictionary methods

nesteddict={
    "name":"harry",
    "class":10,
    "subjects":"science group",
    "maths":89,
    "physics":90,
    "english":87,
    "chemistry":96
}


# print(nesteddict.keys())
# print(nesteddict.values())
# print(nesteddict.items())        #returns all (key, val) pairs as tuples
# print(nesteddict.get("name"))
# print(len(nesteddict))
nesteddict.update({"city":"skp"})
# print(nesteddict)
nesteddict.pop("city")
print(nesteddict)




# here is an important point we have two methods to get a value 
# but why we need two methods what is the difference btw them

# print(nesteddict["name2"])      # it will gives an error if name key not exist
# print(nesteddict.get("name2"))      # it will just none it name key not exist




# we can also update with a new dict

newdict = {
    "city":"sp",
    "country": "pak"
}
nesteddict.update(newdict)
print(nesteddict)
# nesteddict.pop(newdict)    # it will gives an error bcz we can't do that 
