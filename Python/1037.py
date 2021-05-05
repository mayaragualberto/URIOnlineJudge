N=float(input())
if 0<=N<=100:
    if 0<=N<=25:
        print("Intervalo [0,25]")
    if 25<N<=50:
        print("Intervalo (25,50]")
    if 50<N<=75:
        print("Intervalo (50,75]")
    if 75<N<=100:
        print("Intervalo (75,100]")
else:
    print('Fora de intervalo')
