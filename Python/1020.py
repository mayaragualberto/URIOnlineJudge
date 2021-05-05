dia=int(input())
ano=int(dia/365)
dia-=ano*365
print(ano, 'ano(s)')
mes=int(dia/30)
dia-=mes*30
print(mes, 'mes(es)')
print(dia, 'dia(s)')

