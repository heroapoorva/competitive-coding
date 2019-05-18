#http://codeforces.com/contest/1166/problem/A
def c2(x):
    return (x*(x-1))/2

n=int(input())
d={}
for i in range(n):
    temp=input()
    temp=temp[0]
    if(temp in d):
        d[temp]=d[temp]+1
    else:
        d[temp]=1

ans=0
for i in d.values():
    if(i%2==0):
        temp1=i/2
        temp2=i/2
    else:
        temp1=int(i/2)
        temp2=int(i/2)+1
    ans=ans+c2(temp1)+c2(temp2)
ans=int(ans)
print(ans)
