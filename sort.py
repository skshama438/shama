a=[12,3,23,1,4]
n=len(a)
for x in range (n-1):
    swap=0
    for y in range (n-x-1):
        if a[y]>a[y+1]:
            a[y],a[y+1]=a[y+1],a[y]
        swap=1

    if swap==0:
        break

print(a)