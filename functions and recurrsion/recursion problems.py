print("hello world")


def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)


totalsum = sum(10)
print(totalsum)

num = ["a","b","c","d","e","f","g","h"]

def print_element(list,idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_element(list,idx+1)

print_element(num)