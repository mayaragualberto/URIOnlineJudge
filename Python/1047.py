E=input().split()
HInicio=int(E[0])
HFim=int(E[2])
MInicio=int(E[1])
MFim=int(E[3])
if (HFim-HInicio==1) and MInicio>MFim:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(0,(60-MInicio)+MFim))
elif HInicio<HFim and MInicio<=MFim:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(HFim-HInicio,MFim-MInicio))
elif HInicio==HFim and MInicio==MFim:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24,0))
elif HInicio<HFim and MInicio>MFim:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format((HFim-HInicio)-1,60-MInicio+MFim))
elif HInicio==HFim and MInicio<MFim:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(0,MFim-MInicio))
elif HInicio==HFim and MInicio>MFim:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24-1,60-(MInicio-MFim)))
elif HInicio>HFim:
    if MInicio>MFim:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format((24-HInicio)+HFim-1,(60-MInicio)+MFim))
    else:
        print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24-(HInicio-HFim),MFim-MInicio))

