V=input().split()
V.sort(key=float, reverse=True)
A=float(V[0])
B=float(V[1])
C=float(V[2])
if A>=B+C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2==B**2+C**2:
        print('TRIANGULO RETANGULO')
    if A**2>B**2+C**2:
        print('TRIANGULO OBTUSANGULO')
    if A**2<B**2+C**2:
        print('TRIANGULO ACUTANGULO')
    if A==B==C:
        print('TRIANGULO EQUILATERO')
    elif A==B or B==C or C==A:
        print('TRIANGULO ISOSCELES')
