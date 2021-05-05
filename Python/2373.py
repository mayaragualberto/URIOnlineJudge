N=int(input())
Soma=0
while N>0:
    L,C=map(int,input().split())
    if L>C:
        Soma=Soma+C
    N-=1
print(Soma)