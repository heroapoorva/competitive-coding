def change(x):
    ans=""
    for i in range(len(x)):
        if(x[i]=="S"):
            ans=ans+"E"
        else:
            ans=ans+"S"
    return ans

t=int(input())
for i in range(t):
    n=input()
    p=input()
    ans=change(p)
    output="Case #"+str(i+1)+": "+ans
    print(output)
