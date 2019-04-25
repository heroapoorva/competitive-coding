def gcd(x,y):
    if(max(x,y)%min(x,y)==0):
        return(min(x,y))
    else:
        return(gcd(min(x,y),max(x,y)%min(x,y)))

t=int(input())
for i in range(t):
    [n,l]=input().split(" ")
    c=input().split(" ")
    mem=[]
    for i in range(len(c)):
        mem.append([0,0])
    for i in range(len(c)-1):
        if(c[i]!=c[i+1]):
            temp=gcd(c[i],c[i+1])
            mem[i][1]=temp
            mem[i+1][0]=temp
            break
    for j in range(i+1,len(c)-1):
        mem[j]
