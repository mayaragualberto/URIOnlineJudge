par=[]
impar=[]
for _ in range(15):
    N=int(input())
    if N%2==0:
        par.append(N)
        if len(par)==5:
            for i in range(5):
                print("par[{}] = {}".format(i, par[i]))
            par=[]
    else:
        impar.append(N)
        if len(impar)==5:
            for i in range(5):
                print("impar[{}] = {}".format(i, impar[i]))
            impar=[]
for i in range(len(impar)):
    print("impar[{}] = {}".format(i, impar[i]))
for i in range(len(par)):
    print("par[{}] = {}".format(i, par[i]))