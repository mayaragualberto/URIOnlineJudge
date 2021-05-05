N = int(input())

while N>0:
    Palavras =input().split(' ')
    Texto = ""

    for Palavra in Palavras:
        if Palavra != '':
            Texto += Palavra[0]
    print (Texto)
    N-=1
