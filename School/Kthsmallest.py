with open('Kthsmallest.inp','r') as f:
    T=int(f.readline())
    t=[]
    for _ in range(T):
        N=int(f.readline())
        n=list(map(int,f.readline().split()))
        k=int(f.readline())
        n.sort()
        t.append(n[k-1])
with open('Kthsmallest.out','w') as f:
    for i in t:
        f.write(str(i )+ '\n')