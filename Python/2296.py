menor_final = 1000 * 1000 
indice_final = -1
n=int(input())

for t in range(n):
    linha=input()
    palavras=linha.split()
    m=int(palavras[0])
    h=[]
    for i in range(1,m+1):
        altura=int(palavras[i])
        h.append(altura)
    
    esforco_ida=0
    for i in range (0, m-1):
        desnivel=h[i+1]-h[i]
        if desnivel>0:
            esforco_ida+=desnivel
    
    esforco_volta=0
    for i in range (m-1,0,-1):
        desnivel=h[i-1]-h[i]
        if desnivel>0:
            esforco_volta+=desnivel
    
    if esforco_ida<esforco_volta:
        menor_atual=esforco_ida
    else:
        menor_atual=esforco_volta

    if menor_atual<menor_final:
        menor_final=menor_atual
        indice_final=t

print(indice_final+1)
    
