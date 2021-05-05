N=input().split()
A=int(N[0])
B=int(N[1])
C=int(N[2])
D=int(N[3])
if B>C and D>A and C+D > A+B and C>0 and D>0 and A%2==0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
