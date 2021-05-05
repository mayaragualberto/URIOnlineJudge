n=int(input())
igual=0
quadrante=[[0]*501 for x in range(501)] #definir os limites do quadrante
while n>0:
    coord=input().split() #receber par de coordenadas
    x=int(coord[0])
    y=int(coord[1])
    if igual==0:
        if quadrante[int(x)][int(y)] == 0: 
            quadrante[int(x)][int(y)] = 1 #marcar par de coordenadas no mapa
        else:
            igual+=1 
    n-=1
print(igual)