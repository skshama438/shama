a=[]
b=int(input("enter a number:"))
for x in range(b):
    b=int(input("enter a number:"))
    a.append(b)
max=a[0]
for y in range(len(a)):
    if max<a[y]:
        max=a[y]
print(max)