a=[3,4,5,6,7]
lower=int(input("enter a number:"))
upper=int(input("enter a number:"))
count=0
for x in a:
    if x>=lower and x<=upper:
        count=count+1
print(count)