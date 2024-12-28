a=["abc","xyz","aba","1221"]
count=0
for x in a:
    if x[0]==x[-1] and len(a)>=2:
        count=count+1
print(count)