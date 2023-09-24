with open('Parity.inp', 'r') as f:
    n1 = int(f.readline())
    n = []
    for _ in range(n1):
        n.append(f.readline().strip())


with open('Parity.out', 'w') as f:
    for i in n:
        t=0
        t=bin(int(i))
        t=t.count('1')
        if t%2==0:
            f.write('even\n')
        else:
            f.write('odd\n')
