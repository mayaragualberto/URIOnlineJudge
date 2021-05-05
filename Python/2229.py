N=int(input())
teste=1

while N!=-1:
    if N==0:
        D=4
    elif N==1:
        D=9
    else:
        D=(1+(2**N))*(1+(2**N))
    print("Teste",teste)
    print(D)
    print()
    N=int(input())
    teste+=1
    