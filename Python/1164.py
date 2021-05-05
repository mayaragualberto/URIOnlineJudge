N=int(input())
for i in range(N):
    X=int(input())
    soma=0
    for j in range(1,X-1):
        if X%j==0:
            soma=soma+j
    if soma==X:
        print ("{} eh perfeito".format(X))
    else:
        print ("{} nao eh perfeito".format(X))