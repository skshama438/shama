a=[5,6,7,8,4,3,2,1]
mid=(0+len(a)-1)//2
print(mid)
b=[]
c=[]
b.append(a[0:(mid+1)])
c.append(a[(mid+1):len(a)])
print("the first list:",b)
print("the second list:",c)