with open('Countpairs.inp','r') as f:
    with open('Countpairs.out','w') as fo:
        t=int(f.readline())
        for _ in range(t):
            n=int(f.readline())
            N=list(map(int,f.readline().split()))
            d=0
            for i in range(0,n-1):
                for j in range(i+1,n):
                    if i*N[i]>j*N[j]:
                        d+=1

            fo.write(str(d)+' ')
                        