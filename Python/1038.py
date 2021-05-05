DADOS=input().split()
Cod=int(DADOS[0])
Qtd=int(DADOS[1])
Codigos=[1,2,3,4,5]
Precos=[4, 4.5 ,5 ,2 ,1.5]
if Cod in Codigos:
    Valor=Qtd*Precos[Cod-1]
    print('Total: R$ {:.2f}'.format(Valor))
