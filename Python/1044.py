N=input().split()
N1=int(N[0])
N2=int(N[1])
if N2>N1:
    if N2%N1==0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
if N1>N2:
    if N1%N2==0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
if N1==N2:
    print('Sao Multiplos')
