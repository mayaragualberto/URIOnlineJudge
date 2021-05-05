N=int(input())
n1=0
n2=1
temp=0
if N<46:
    for i in range(N):
        if i!=N-1:
            print(n1,end=" ")
            temp = n2+n1
            n1=n2
            n2=temp
        else:
            print(n1)
