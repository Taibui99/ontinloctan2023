with open('Parity.inp','r') as f:
    n1=int(f.readline())

    with open('Parity.out','w') as f:
        for _ in n1:
            n=[s.strip for s in f.readline()]
            t = bin(int(n))
            t=t.count('1')
            if t%2==0:
                f.write('even')
            else:
                f.write('odd')

