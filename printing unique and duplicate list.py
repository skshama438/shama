a=[7,3,4,2,6,3]
unique=[]
duplicate=[]
for x in a:
    if x not in unique:
        unique.append(x)
    elif x not in duplicate:
        duplicate.append(x)
print("the unique element list is",unique)
print("the duplicate element list",duplicate)