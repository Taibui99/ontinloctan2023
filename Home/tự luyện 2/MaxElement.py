with open('MaxElement.inp','r') as f:
    t=int(f.readline())
    n=list(map(int,f.readline().strip().split()))
with open('MaxElement.out','w') as f:
    f.write(str(max(n)))