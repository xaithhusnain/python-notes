print("hello world")

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O using Java.\nI like programming in Java.")

with open("practice.txt","r") as f:
    data = f.read()

newdata = data.replace("Java","python")
print(newdata)

with open("practice.txt","w") as f:
    data = f.write(newdata)










with open("practice.txt","r") as f:
    data = f.read()
    if "learning" in data:
        print("exist")
    else:
        print("not exist")
    

word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if (data.find(word)) != -1:
        print("exist")
    else:
        print("not exist")



def check_for_word():
    with open("practice.txt","r") as f:
        data = f.read()
        if (data.find(word)) != -1:
            print("exist")
        else:
            print("not exist")











def checkforline():
    word = "puyth"
    lineno = 1
    data = True
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if word in data:
                print("exist",lineno)
                return
            lineno +=1
    return -1

print(checkforline())
















def count():
    cnt= 1
    with open("practice.txt","r") as f:
        data = f.read()
        print(data)
        print(type(data))
        print(len(data))


        num = ""
        for i in range(len(data)):
            if(data[i]==","):
                print(int(num))
                num = ""
            else:
                num +=data[i]
            


def count():
    with open("practice.txt", "r") as f:
        text = f.read()

    # Normalize newlines to commas, split, strip, and skip empties
    tokens = [t.strip() for t in text.replace("\n", ",").replace("\r", ",").split(",")]
    for t in tokens:
        if t:                  # skip empty pieces (e.g., consecutive commas)
            print(int(t))

count()



cnt = 0
with open("practice.txt", "r") as f:
    data = f.read()

    num = data.split(",")
    for val in num:
        if (int(val)%2 == 0):
            cnt += 1


print(cnt)






def count_even_numbers():
    with open("practice.txt", "r") as f:
        text = f.read()

    # Convert file content into a list of integers
    numbers = [int(t.strip()) for t in text.split(",") if t.strip()]

    # Count evens
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1

    print("Count of even numbers:", even_count)


count_even_numbers()





cnt = 0
with open("practice.txt", "r") as f:
    data = f.read()

    num = data.split(",")
    for val in num:
        val = val.strip()      # remove spaces/newlines
        if val:                # skip empty strings
            if int(val) % 2 == 0:
                cnt += 1

print(cnt)












with open("practice.txt","r") as f:
    data = f.read()
    print(data)
    num = data.split(",")
    print(num)
    

    count = 0
    for i in num:
        i = i.strip()
        if i:
            if int(i)%2 == 0:
                count += 1
    print(f"count of even numbers: {count}")


















