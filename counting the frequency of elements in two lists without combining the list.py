a=[4,8,5,3,2,9]
b=[3,4,5,5,4,6,7,6,7,2]
c={}
for y in b:
    c[y]=b.count(y)
for x in c:
    if x in a:
        c[x]+=1
print(c)