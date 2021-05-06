#Recebe o placar dos jogos Inter x Grêmio e informa a quantidade de partidas, 
#quantidade de gols de cada time e o vencedor
partidanova = 1
vit_gremio = vit_inter = empates = grenais = 0
while partidanova==1:
    grenais+=1   
    gols_inter, gols_gremio = map (int, input().split())
    print ("Novo grenal (1-sim 2-nao)")
    partidanova = int(input())
    if gols_gremio > gols_inter:
        vit_gremio+=1
    elif gols_inter > gols_gremio:
        vit_inter+=1
    else:
        empates+=1
print(grenais,"grenais")
print("Inter:{}".format(vit_inter))
print("Gremio:{}".format(vit_gremio))
print("Empates:{}".format(empates))
if (vit_inter>vit_gremio):
    print("Inter venceu mais")
elif (vit_gremio>vit_inter):
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")

