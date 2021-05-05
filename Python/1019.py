N=int(input())
horas=int(N/(60**2))
N-=horas*(60**2)
minutos=int(N/60)
N-=minutos*60
segundos=N
print('{}:{}:{}'.format(horas, minutos, segundos))
