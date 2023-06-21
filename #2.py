from math import*
def fun(a,b,c):  
    return (2*pi*a)+(2*pi*b)+(2*pi*c)
a,b,c=map(int,input().split())
print(format(fun(a,b,c),".2f"))
