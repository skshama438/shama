a=[1,2,3,4,5]
b=[x**2 for x in a]
c=[]
for x in b:
    c=[x]+c
print(c)
    