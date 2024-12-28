a=["shama","shaik","","","babu"]
for x in a[:]:
    if len(x)==0:
        a.remove(x)
print(a)