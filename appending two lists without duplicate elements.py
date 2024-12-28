a=[4,5,6,7,8]
b=[5,4,3,2,1]
c=[]
for x in a:
    if x not in c:
        c.append(x)
for y in b:
    if y not in c:
        c.append(y)
print(c)