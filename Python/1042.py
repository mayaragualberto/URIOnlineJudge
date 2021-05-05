N=input().split()
Nmenor=sorted(N,key=int)
for i in range(len(N)):
    print(Nmenor[i])
    i+=1
print()
for j in range(len(N)):
    print(N[j])
    j-=1
    
        
        
