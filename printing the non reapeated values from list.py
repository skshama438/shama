a = [4, 5, 6, 7, 8,7,5,3,9,2,1,9]
c=[]
for x in a:
    if a.count(x)<2:
        c.append(x)
print(c)