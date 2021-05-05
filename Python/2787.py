L=int(input())
C=int(input())

if L%2==0 and C%2!=0:
    print(0)
elif L%2!=0 and C%2==0:
    print(0)
else:
    print(1)