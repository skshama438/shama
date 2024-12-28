a=[1,2,3,3,4]
b=[5,6,7,8,9]
c=[]
n=len(a)
m=len(b)
i=0
j=0
while(i<n)&(j<m):
    if a[i]<b[j]:
        c.append(a[i])
        i=i+1
    else:
        c.append(b[j])
        j=j+1
while(i<n):
    c.append(a[i])
    i=i+1
while(j<m):
    c.append(b[j])
    j=j+1
x=len(c)
if x%2==0:
    even_median=((x/2)+((x/2)+1))//2
    print("the even number of median is",even_median)
else:
    odd_median=(n+1)//2
    print("the odd number of median is",odd_median)
print(c)