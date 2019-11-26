def overlapping(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

print(overlapping(['a','b','c'],['d','e','b']))
print(overlapping(['it','worked','or','not'],['nope','false']))