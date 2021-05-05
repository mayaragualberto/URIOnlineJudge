N = int(input())
P = [int(x) for x in input().split()]
Elevador=False
for i in range(N):
    if i == 0:
        if (P[i]-0)<=8:
            Elevador=True
        else:
            Elevador=False
            break
    else:
        if (P[i]-P[i-1])<=8:
            Elevador=True
        else:
            Elevador=False
            break
if Elevador:
    print("S")
else:
    print("N")
