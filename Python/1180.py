N=int(input())
X=input().split()
for i in range(len(X)):
    X[i] = int(X[i])
Menor_valor=min(X)
print("Menor valor:",Menor_valor)
Posicao=X.index(Menor_valor)
print("Posicao:",Posicao)