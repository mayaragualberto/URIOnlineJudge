DADOS=input().split()
X=float(DADOS[0])
Y=float(DADOS[1])
if X==Y==0:
    print('Origem')
elif X>0 and Y>0:
    print('Q1')
elif X>0 and Y<0:
    print('Q4')
elif X<0 and Y<0:
    print('Q3')
elif X<0 and Y>0:
    print('Q2')
elif Y==0 and X!=0:
    print('Eixo X')
elif X==0 and Y!=0:
    print('Eixo Y')
