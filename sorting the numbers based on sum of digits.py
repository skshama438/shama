a=[2,35,99,68,10]
c=[]
for x in a:
    sum=0
    while(x!=0):
        s=x%10
        sum=sum+s
        x=x//10
    c.append(sum)
sorted_list1 = [x for _, x in sorted(zip(c,a))]
print(sorted_list1)