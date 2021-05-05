DADOS1=input().split()
DADOS2=input().split()
x1=float(DADOS1[0])
y1=float(DADOS1[1])
x2=float(DADOS2[0])
y2=float(DADOS2[1])
import math
Distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f'{Distancia:.4f}')
