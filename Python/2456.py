A,B,C,D,E=map(int,input().split())

if A<B and B<C and C<D and D<E:
    print("C")
elif A>B and B>C and C>D and D>E:
    print("D")
else:
    print("N")