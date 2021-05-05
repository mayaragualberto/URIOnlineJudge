VALOR=int(input())
print(VALOR)
notas=[100, 50, 20, 10, 5, 2, 1]
for nota in notas:
    qtd_notas=int(VALOR/nota)
    print('{} nota(s) de R$ {},00'.format(qtd_notas, nota))
    VALOR-=qtd_notas*nota


    
