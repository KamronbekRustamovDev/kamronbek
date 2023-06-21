def fun():
    global a,b
    return a*b,2*(a+b)
a,b=map(int,input().split())
print(*fun())
