N=10
X=[]
while N>0:
    N-=1
    x=int(input())
    if x<=0:
        x=1
    X.append(x)
for i in range(len(X)):
    print("X[{}] = {}".format(i,X[i]))
