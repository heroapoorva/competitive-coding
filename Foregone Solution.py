def change(x):
    output1=""
    output2=""
    for i in range(len(x)):
        if(x[i]!="4"):
            output1=output1+x[i]
            output2=output2+str(0)
        else:
            output1=output1+"1"
            output2=output2+"3"
    return(output1,output2)

def clear(x):
    for i in range(len(x)):
        if(x[i]!="0"):
            break
    return(x[i:])
    
t=int(input())    
for i in range(t):
    n=input()
    n=clear(n)
    ans=change(n)
    output="Case #"+str(i+1)+": "+clear(ans[0])+" "+clear(ans[1])
    print(output)
