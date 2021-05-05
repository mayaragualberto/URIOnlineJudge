#Cálculo do imposto de renda. Menos que R$ 2.000 é isento, depois para as faixas de
#de R$ 2000.01 até R$ 3000.00 por 8%, de R$ 3000.01 até R$ 4500.00 por 18%
#acima de R$ 4500.00
Renda=float(input())
Taxa1,Taxa2,Taxa3=0, 0, 0
#Caso que é isento
if Renda<2000.00:
    print("Isento")
#Casos que variam as taxas de imposto
elif Renda>=2000.01 and Renda<=3000.00:
    Taxa1=Renda-2000.00
elif Renda>=3000.01 and Renda<=4500.00:
    Taxa1=1000.00
    Taxa2=Renda-3000.00
else:
    Taxa1=1000.00
    Taxa2=1500.00
    Taxa3=Renda-4500.00

if Taxa1 != 0:
    print("R$ {:.2f}".format(Taxa1*0.08+Taxa2*0.18+Taxa3*0.28))