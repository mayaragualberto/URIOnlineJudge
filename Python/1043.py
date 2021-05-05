V=input().split()
N1=float(V[0])
N2=float(V[1])
N3=float(V[2])
if abs(N2-N3)<N1<(N2+N3) and (N1-N3)<N2<(N1+N3) and (N1-N2)<N3<(N1+N2):
    print('Perimetro = {:.1f}'.format(N1+N2+N3))
else:
    print('Area = {:.1f}'.format(((N1+N2)*N3)/2))
    
