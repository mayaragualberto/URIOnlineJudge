N1=input()
N2=input()
N3=input()
if N1=="vertebrado":
    if N2=="ave":
        if N3=="carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if N3=="onivoro":
            print("homem")
        else:
            print("vaca")
elif N1=="invertebrado":
    if N2=="inseto":
        if N3=="hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if N3=="hematofago":
            print("sanguessuga")
        else:
            print("minhoca")