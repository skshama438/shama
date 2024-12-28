a = [4, 5, 6, 7, 8,4,5,6,7,4,3,3,5]
b=[]
for x in a:
    if x not in b:
        b.append(x)
print(b)
