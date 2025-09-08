print("hello world")

f = open("demo.txt","w")
f.write("i want to learn ML.")
f.close()

# write mode also called overwrite mode bcz it overwrite the whole data
# first it delete the previous data then add the new data 



f = open("demo.txt","a")
f.write("\nThen i will go to NLP.")
f.close()

# append means "add at the end" which means append mode add new data after the previous data 
# it dose not delete the old data





f = open("sample.txt","a")
f.close()

# when we open a file with "w" or "a" mode and it dose not exist then it will create a new file 

