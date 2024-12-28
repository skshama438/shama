a = [2,5,7,8,9,4,5,6] 
b=3
for x in range(len(a)):
    s=a.count(a[x])
    if s>1:
        a[x]=b
print(a)