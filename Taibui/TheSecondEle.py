with open('TheSecondEle.inp','r') as f:
    t=int(f.readline())
    n=list(map(int,f.readline().strip().split()))
    t=[]
    for i in n:
        if i<max(n):
            t.append(i)
with open('TheSecondEle.out','w') as f:

    f.write(str(max(t)))