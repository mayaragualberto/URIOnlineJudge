DADOS=input().split()
A=float(DADOS[0])
B=float(DADOS[1])
C=float(DADOS[2])
print("TRIANGULO: {:.3f}".format((A*C)/2))
print("CIRCULO: {:.3f}".format(3.14159*(C**2)))
print("TRAPEZIO: {:.3f}".format(((A+B)*C)/2))
print("QUADRADO: {:.3f}".format(B**2))
print("RETANGULO: {:.3f}".format(A*B))
