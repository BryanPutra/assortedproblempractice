def is_member(value,list):
    return any(value == i for i in list)
myList = ["a","b","c",1,2,3]

print(is_member("a",myList))
print(is_member(3,myList))
print(is_member(5,myList))
