a=[7,8,9,2,1,6,11]
n=len(a)
for x in range(n-1):
        min=x
        for y in range(x+1,n):
            if a[min]>a[y]:
                 min=y
        if min!=x:
              a[x],a[min]=a[min],a[x]
        print(a)

        