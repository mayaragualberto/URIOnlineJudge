A,B,C,D=map(int, input().split())
existe=False
for n in range(A*2,A*4+55555,A):
    if n%A==0 and n%B!=0 and C%n==0 and D%n!=0:
        existe=True
        print(n)
        break
if not existe:
    print("-1")