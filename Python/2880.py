Mens=input()
Crib=input().replace(" ","").replace(".","")

def split(word):
    return [char for char in word]

letrasMens=split(Mens)
letrasCrib=split(Crib)

repete=False
cont=0
enigma=0
rodadas = len(letrasMens)-len(letrasCrib)+1
for i in range(rodadas):
    for j in range(len(letrasCrib)):
        if repete==False:
            if letrasCrib[j]!=letrasMens[j]:
                cont+=1
            else:
                repete==True
                break
        repete=False
    if cont==len(letrasCrib):
        enigma+=1
    cont=0
    del letrasMens[0]

print(enigma)