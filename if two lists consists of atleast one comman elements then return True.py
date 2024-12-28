def shama(a,b):
    c=0
    for x in a:
        for y in b:
            if x==y:
                c=1
    if c==1:
        return True
    else:
        return False
            
a=[3,4,5,6]
b=[2,8,9,1]
print(shama(a,b))
    