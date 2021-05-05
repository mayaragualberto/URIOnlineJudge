N=input().split()
N1=float(N[0])
N2=float(N[1])
N3=float(N[2])
N4=float(N[3])
Media=(N1*2+N2*3+N3*4+N4*1)/10
print('Media: {:.1f}'.format(Media))
if Media>=7.0 or Media<5.0:
    if Media>=7.0:
        print('Aluno aprovado.')
    if Media<5.0:
        print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    Ne=float(input())
    print('Nota do exame:',Ne)
    Media=(Ne+Media)/2
    if Media>=5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(Media))
    
    
