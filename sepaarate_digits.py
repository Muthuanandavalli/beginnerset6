N=int(input())
lt=[]
while(N>0):
    r=N%10
    lt.append(r)
    N=N//10
for i in range(len(lt)-1,-1,-1):
    x=lt[i]
    if i==0:
        print(x,end="")
    else:
        print(x,end=" ")
