N=int(input())
Lista = [int(x) for x in input().split()]
Escadinha = 1
for x in range(2, N):
    if Lista[x] - Lista[x-1] != Lista[x-1] - Lista[x-2]:
        Escadinha += 1
print(Escadinha)