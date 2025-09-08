print("hello world")

fav_movies=[]
a = input("enter your fav movies:")
fav_movies.append(a.split(","))
print(fav_movies)


fav_movies=[]
a = input("enter your 1st fav movies:")
b = input("enter your 2nd fav movies:")
c = input("enter your 3rd fav movies:")
fav_movies.append(a)
fav_movies.append(b)
fav_movies.append(c)
print(fav_movies)




a = [1,2,3,2,1]
b = a.copy()
b.reverse()
if a==b:
    print("its palindrome")
else:
    print("not a palindrome")


a = [1, 'abc', 'abc']
b = a.copy()
b.reverse()
if a==b:
    print("its palindrome")
else:
    print("not a palindrome")





a = ("C", "D", "A", "A", "B", "B", "A")
print(a.count("A"))


b = list(a)
print(type(b))
b.sort()
print(b)