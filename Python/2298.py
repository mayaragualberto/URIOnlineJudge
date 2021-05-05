n = int(input())
teste = 1
cartas=[]
for i in range(n):
    carta=[int(x) for x in input().split()]
    carta.sort()
    cartas.append(carta)
for i in range(n):
    print("Teste",teste)
    teste+=1
    crescente=0
    # cinco cartas estão em seqüência a partir da carta x
    for j in range(5-1):
        if cartas[i][j+1]==cartas[i][j]+1:
            crescente+=1
    if crescente==4:
        print(200+(int(cartas[i][0])))
    #há quatro cartas iguais x
    elif (cartas[i][0]==cartas[i][1] and cartas[i][1]==cartas[i][2] and cartas[i][2]==cartas[i][3]) and (cartas[i][3]!=cartas[i][4]):
        print(180+(int(cartas[i][0])))
    elif (cartas[i][1]==cartas[i][2] and cartas[i][2]==cartas[i][3] and cartas[i][3]==cartas[i][4]) and (cartas[i][0]!=cartas[i][1]):
        print(180+(int(cartas[i][1])))
    #há três cartas iguais x e duas outras cartas iguais y
    elif (cartas[i][0]==cartas[i][1] and cartas[i][1]==cartas[i][2]) and (cartas[i][3]==cartas[i][4]):
        print(160+(int(cartas[i][0])))
    elif (cartas[i][2]==cartas[i][3] and cartas[i][3]==cartas[i][4]) and (cartas[i][0]==cartas[i][1]):
        print(160+(int(cartas[i][2]))) 
    #há três cartas iguais x e duas outras cartas diferentes y e z 
    elif (cartas[i][0]==cartas[i][1] and cartas[i][1]==cartas[i][2]) and (cartas[i][2]!=cartas[i][3] and cartas[i][3]!=cartas[i][4] and cartas[i][4]!=cartas[i][0]):
        print(140+(int(cartas[i][0])))
    elif (cartas[i][1]==cartas[i][2] and cartas[i][2]==cartas[i][3]) and (cartas[i][0]!=cartas[i][1] and cartas[i][3]!=cartas[i][4] and cartas[i][4]!=cartas[i][1]):
        print(140+(int(cartas[i][2])))
    elif (cartas[i][2]==cartas[i][3] and cartas[i][3]==cartas[i][4]) and (cartas[i][0]!=cartas[i][1] and cartas[i][1]!=cartas[i][2] and cartas[i][1]!=cartas[i][2]):
        print(140+(int(cartas[i][2])))
    #há duas cartas iguais x, duas outras cartas iguais y (x != y) e uma outra carta distinta z 
    elif (cartas[i][0]==cartas[i][1]) and (cartas[i][2]==cartas[i][3]) and (cartas[i][4]!=cartas[i][0] and cartas[i][4]!=cartas[i][2]):
        print(20+2*(int(cartas[i][0]))+3*(int(cartas[i][2])))    
    elif (cartas[i][1]==cartas[i][2]) and (cartas[i][3]==cartas[i][4]) and (cartas[i][0]!=cartas[i][1] and cartas[i][0]!=cartas[i][3]):
        print(20+2*(int(cartas[i][1]))+3*(int(cartas[i][3])))
    elif (cartas[i][0]==cartas[i][1]) and (cartas[i][3]==cartas[i][4]) and (cartas[i][2]!=cartas[i][0] and cartas[i][2]!=cartas[i][3]):
        print(20+2*(int(cartas[i][0]))+3*(int(cartas[i][3])))  
    #há apenas duas cartas iguais x e as outras são todas distintas
    elif (cartas[i][0]==cartas[i][1]) and (cartas[i][2]!=cartas[i][0] and cartas[i][2]!=cartas[i][3] and cartas[i][2]!=cartas[i][4] and cartas[i][3]!=cartas[i][0] and cartas[i][3]!=cartas[i][4]):
        print(int(cartas[i][0]))
    elif (cartas[i][1]==cartas[i][2]) and (cartas[i][0]!=cartas[i][1] and cartas[i][0]!=cartas[i][3] and cartas[i][0]!=cartas[i][4] and cartas[i][3]!=cartas[i][0] and cartas[i][3]!=cartas[i][4]):
        print(int(cartas[i][1]))
    elif (cartas[i][2]==cartas[i][3]) and (cartas[i][0]!=cartas[i][2] and cartas[i][0]!=cartas[i][1] and cartas[i][0]!=cartas[i][4] and cartas[i][1]!=cartas[i][2] and cartas[i][1]!=cartas[i][4]):
        print(int(cartas[i][2]))
    elif (cartas[i][3]==cartas[i][4]) and (cartas[i][0]!=cartas[i][3] and cartas[i][0]!=cartas[i][1] and cartas[i][0]!=cartas[i][2] and cartas[i][1]!=cartas[i][2] and cartas[i][1]!=cartas[i][3]):
        print(int(cartas[i][3]))
    #todas as cartas são distintas, não há pontuação
    else:
        print(0) 
    print()