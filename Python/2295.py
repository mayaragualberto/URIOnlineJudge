A, G, Ra, Rg=map(float,input().split())

rendA=A/Ra
rendG=G/Rg

if rendA<rendG:
    print("A")
else:
    print("G")

