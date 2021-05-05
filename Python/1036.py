import math
N=input().split()
A=float(N[0])
B=float(N[1])
C=float(N[2])
D=B**2 - 4*A*C
if D<0 or A==0:
    print("Impossivel calcular")
else:
    X1=(-B+math.sqrt(D))/(2*A)
    X2=(-B-math.sqrt(D))/(2*A)
    print('R1 = {:.5f}'.format(X1))
    print('R2 = {:.5f}'.format(X2))
    
