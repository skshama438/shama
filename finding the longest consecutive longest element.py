a=[(1,2,3),(5,6),(8,9,10,11,12),(15,)]
b={}
for x in range(0,len(a)):
    b[len(a[x])]=a[x]
max_length = max(b)
longest_tuple = b[max_length]
print(longest_tuple)