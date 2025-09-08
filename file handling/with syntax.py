print("hello world")


with open( "demo.txt", "r") as f:
    data = f.read()
    print(data)

with open( "demo.txt", "w") as f:
    f.write("learning python.")


with open( "demo.txt", "a") as f:
    f.write("\nAre you okay.")
