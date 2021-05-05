A, B, C = map(int,input().split())
if((A-B==0) or (A-C==0) or (B-C==0)):
    print('S')
else:
    if((A+B-C==0) or (B-A+C==0) or (C-A+B==0)):
        print('S')
    elif((A-B-C==0) or (B-A-C==0) or (C-A-B==0)):
        print('S')
    else:
        print('N')