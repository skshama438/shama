a = ["yellow", "black", "red", "pink", "blue","real"]  
b={}
for x in a:
    first=x[0]
    if first not in b:
        b[first]=[]
    b[first].append(x)
print(b)