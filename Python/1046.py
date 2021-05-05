E=input().split()
Inicio=int(E[0])
Fim=int(E[1])
if Inicio>=Fim:
    print('O JOGO DUROU {} HORA(S)'.format(24-Inicio+Fim))
else:
    print('O JOGO DUROU {} HORA(S)'.format(Fim-Inicio))

