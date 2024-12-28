a = [4, 5, 6, 7, 8,4,5,6,7,4,3,3,5]
b=set()
for x in a:
    if x not in b:
        print(f"{x} frequnecy is {a.count(x)}")
    b.add(x)