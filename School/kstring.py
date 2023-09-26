with open('kstring.inp','r') as f:
    k=int(f.readline())
    s= f.readline()
with open('kstring.out','w') as f:
    cnt=[0]*26
    for c in s:
        cnt[ord(c)-ord('a')] += 1
    s=''
    ok = True
    for i in range(26):
        if cnt[i]:
            if cnt[i] % k:
                ok =False
            for j in range(cnt[i]//k):
                s += chr(i+ord('a'))
    if ok:
        for i in range(k):
            f.write(s+'')
        f.write('')
    else:
        f.write('-1')