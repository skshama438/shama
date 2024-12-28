a=[5,6,7,2,3]
product=1
count=0
for x in a:
    if x%2!=0:
        product=product*x
        count=1
if count==1:
    print(product)
else:
    print("0")