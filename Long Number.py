#https://codeforces.com/contest/1157/problem/B
l=int(input())
#n=list( map( lambda x : int(x), input()))
n=input()
m=list( map( lambda x : int(x), n))
#f=list( map( lambda x : int(x), input().split(" ")))
f=input().split(" ")
worth=[0]
for i in range(len(f)):
    if(f[i]>=str(i+1)):
        worth.append(1)
    else:
        worth.append(0)
nworth=[]
for i in range(len(m)):
    if(worth[m[i]]==1):
        nworth.append(1)
    else:
        nworth.append(0)
seen=0
for i in range(len(m)):
    if(seen==0):
        if(nworth[i]==1):
            seen=1
    elif(seen==1):
        if(nworth[i]==0):
            seen=2
    else:
        nworth[i]==0
output=""
for i in range(len(n)):
    if(nworth[i]==0):
        output=output+n[i]
    else:
        output=output+f[m[i]-1]
print(output)
