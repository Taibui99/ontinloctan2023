with open('MaxPositive.inp','r') as fi:
    N=int(fi.readline())
    with open('MaxPositive.out','w') as fo:
        for _ in range(N):
            x=float(fi.readline())
            n=0
            t=0.0
            while t<x:
                n+=1
                t+=1.0/(2*n-1)
            fo.write(str(n-1)+'\n')