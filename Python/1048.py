S=float(input())

if S>=0 and S<=400:
    novo_salario=S+S*(15/100)
    reajuste=S*(15/100)
    percentual=15
elif S>400 and S<=800:
    novo_salario=S+S*(12/100)
    reajuste=S*(12/100)
    percentual=12
elif S>800 and S<=1200:
    novo_salario=S+S*(10/100)
    reajuste=S*(10/100)
    percentual=10
elif S>1200 and S<=2000:
    novo_salario=S+S*(7/100)
    reajuste=S*(7/100)
    percentual=7
elif S>2000:
    novo_salario=S+S*(4/100)
    reajuste=S*(4/100)
    percentual=4

print("Novo salario: {:.2f}".format(novo_salario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {:.0f} %".format(percentual))