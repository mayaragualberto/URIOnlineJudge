n1=0
n2=1
temp=0
F=[]
for i in range(61):
    if i!=61-1:
        F.append(n1)
        temp = n2+n1
        n1=n2
        n2=temp
    else:
        F.append(n1)
N=int(input())
for _ in range(N):
    indice=int(input())
    print("Fib({}) = {}".format(indice,F[indice]))