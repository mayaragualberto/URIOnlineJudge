N=int(input())
Operacao=input().split()
P=int(Operacao[0])
C=Operacao[1]
Q=int(Operacao[2])

if C=="*":
    resultado=P*Q
elif C=="+":
    resultado=P+Q
if N>=resultado:
    print("OK")
else:
    print("OVERFLOW")
