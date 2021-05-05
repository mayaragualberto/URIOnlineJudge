Teste_cont=1
while True:
    A,V=map(int,input().split())
    if A==V==0:
        break
    Aeroporto=[0]*A
    while V:
        V-=1
        X,Y=map(int,input().split())
        Aeroporto[X-1]+=1
        Aeroporto[Y-1]+=1
    Mais_frequente=max(Aeroporto)
    Maior=[str(i+1) for i in range(len(Aeroporto)) if Aeroporto[i]==Mais_frequente]
    print("Teste", Teste_cont)
    print(" ".join(Maior),"")
    print()
    Teste_cont+=1


