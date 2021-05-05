V=1
cont=1
while V!=0:
    V=int(input())
    if V==0:
        break
    I=V//50
    resto=V%50
    if resto!=0:
        J=resto//10
        resto=resto%10
    else: 
        J=0
    if resto!=0:
        K=resto//5
        resto=resto%5
    else:
        K=0
    if resto!=0:
        L=resto
    else:
        L=0
    print("Teste",cont)
    print(I,J,K,L)
    print()
    cont+=1