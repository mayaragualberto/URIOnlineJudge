t = 1
n = int(input())
while n != 0:
    nome_par = input()
    nome_impar = input()
    print('Teste', t)
    for _ in range(n):
        a,b=map(int, input().split())
        s = a + b
        if s % 2 == 0:
            print(nome_par)
        else:
            print(nome_impar)
    print()
    t += 1
    n = int(input())        