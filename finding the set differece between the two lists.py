a=[4,8,5,3,2,9]
b=[6,5,4,3,1,7]
c={}
for y in b:
    c[y]=b.count(y)
for x in a:
    if x not in c.keys():
       print(x)