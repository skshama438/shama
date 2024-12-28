a=123
reverse=0
while(a!=0):
    s=a%10
    reverse=reverse*10+s
    a=a//10
print(reverse)