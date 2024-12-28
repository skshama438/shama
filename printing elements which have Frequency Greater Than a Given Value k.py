a=[4,5,6,7,8,4,5,6,3,3,3,4,4,5,5,7]
b=3
c=[]
for x in a:
    s=a.count(x)
    if s>b:
        if x not in c:
            c.append(x)
print(c)