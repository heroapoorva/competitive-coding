#https://codeforces.com/contest/1157/problem/A
n=int(input())
r=1
def modify(n):
    m=n+1
    if(m%10==0):
        while(m%10==0):
            m=int(m/10)
    return(m)
def count(n,r):
    l=[n]
    while(True):
        if(modify(n)==1):
            break
        else:
            n=modify(n)
            l.append(n)
    l=l+[1,2,3,4,5,6,7,8,9]
    l=list(set(l))
    return(len(l))
print(count(n,r))
