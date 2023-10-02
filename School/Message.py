with open('Message.inp','r') as fi:
    T=int(fi.readline())
    with open('Message.out','w') as fo:
        for _ in range(T):
            n=int(fi.readline())
            fo.write(str(2*n-2)+'\n')