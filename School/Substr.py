with open('Substr.inp','r') as f:
    with open('Substr.out','w') as fo:
        x,y=map(str,f.read().split())
        lx=len(x)
        x*=2
        for i in range(lx):
            s=x[i:i+len(y)]
            if s==y:
                fo.write(str(i+1) + ' ')


