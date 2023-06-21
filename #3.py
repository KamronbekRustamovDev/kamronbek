from math import*
def fun(a,b,c,w,q):
    if a<w and a>q:
        return q,a,w
    elif b<w and b>q:
        return q,b,w
    elif c<w and c>q:
        return q,c,w
    else:
        return a,b,c
a,b,c=map(int,input().split())
q=min(a,b,c)
w=max(a,b,c)
print(*fun(a,b,c,w,q))
