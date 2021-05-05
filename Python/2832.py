N,F=map(int,input().split())
pilulas=[int(x) for x in input().split()]

def busca_binaria(N,F):
    esquerda=1
    direita=100000000

    while (esquerda<direita):
        meio=(esquerda+direita)//2
        if (dinheiro(meio) >= F):
            direita=meio
        else:
            esquerda=meio+1
    return (round(esquerda))

def dinheiro(x):
    total=0
    for i in range(len(pilulas)):
        total+=x//pilulas[i]
    return total

print(busca_binaria(pilulas, F))