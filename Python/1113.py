X=1
Y=2
while X!=Y:
    X,Y=map(int,input().split())
    if X<Y:
        print("Crescente")
    elif X>Y:
        print("Decrescente")
