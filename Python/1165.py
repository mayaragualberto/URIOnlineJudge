N=int(input())
Numeros=[]
for i in range(N):
    Num=int(input())
    divisores=1
    for j in range(1,Num):
        if Num%j==0:
            divisores+=1
    if divisores==2:
        print("{} eh primo".format(Num))
    else:
        print("{} nao eh primo".format(Num))


