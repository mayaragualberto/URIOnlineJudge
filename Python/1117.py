notas_validas=0
soma=0
while notas_validas<2:
    N=float(input())
    if N>=0 and N<=10:
        notas_validas+=1
        soma=soma+N
    else:
        print ("nota invalida")
print("media = {:.2f}".format(soma/2))