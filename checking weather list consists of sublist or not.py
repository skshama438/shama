a=[[3,4,5,6],7,6,7,4,3,4,5]
count=0
for x in a:
    if type(x)==list:
        count=1
if count==1:
    print(True)
else:
    print(False)