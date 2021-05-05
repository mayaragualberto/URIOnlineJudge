N=int(input())
teste=1
while N>0:
    Xa=-10000
    Ya=10000
    Ua=10000
    Va=-10000
    for i in range(N):
        X,Y,U,V=map(int,input().split())
        if (X>Xa):
            Xa=X
        if (Y<Ya):
            Ya=Y
        if (U<Ua):
            Ua=U
        if (V>Va):
            Va=V
    print("Teste",teste)
    if (Ua<Xa or Ya<Va):
        print("nenhum")
    else:
        print(Xa,Ya,Ua,Va)
    print()
    N=int(input())
    teste+=1