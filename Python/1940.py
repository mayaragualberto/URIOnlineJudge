J,R=[int(x) for x in input().split()]
N=list(map(int, input().split()))
Pontos=[0]*J
for i in range(len(N)):
    Pontos[i%J]+=N[i]
Maior=Pontos[0]
for j in range(len(Pontos)):
    if Pontos[j]>=Maior:
        Maior=Pontos[j]
        Vencedor=j+1
print(Vencedor)
