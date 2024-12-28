a=[(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in range(len(a)):
    for j in range(len(a) - i -1):
        if a[j][1]>a[j+1][1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)