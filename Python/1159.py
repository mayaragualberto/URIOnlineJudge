while 1:
    soma=0
    X=int(input())
    if X==0:
        break
    if X%2==0:
        for i in range(5):
            soma=soma+X
            X+=2    
        print(soma)    
    elif X%2!=0:
        X+=1
        for i in range(5):
            soma=soma+X
            X+=2
        print(soma)

