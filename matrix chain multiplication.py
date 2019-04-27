p=list( map( lambda x : int(x), input().split(" ")))
n=len(p)-1
a=[]
for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(0)
    a.append(temp)
for i in range(n-1):
    a[i][i+1]=p[i]*p[i+1]*p[i+2]

for diff in range(2,n):
    for i in range(n):
        if(i+diff<n):
            temp= a[i][i]+a[i+1][i+diff]+p[i]*p[i+1]*p[i+diff+1]
            for k in range(i,i+diff):   
                temp= min(temp,a[i][k]+a[k+1][i+diff]+p[i]*p[k+1]*p[i+diff+1])
            a[i][i+diff]=temp
print(a[0][n-1])
