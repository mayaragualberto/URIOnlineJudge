import string
N=int(input())
F=[]
for i in range(N):
    frase=input().replace(" ","").replace(".","").replace(",","")
    F.append(frase)
alfabeto=(string.ascii_lowercase) 
for i in range(N):
    presente=0
    for j in range(len(alfabeto)):
        if alfabeto[j] in F[i]:
            presente+=1
    if presente==26:
        print("frase completa")
    elif presente<26 and presente>=13:
        print("frase quase completa")
    elif presente<13:
        print("frase mal elaborada")