with open('rotation.inp','r') as f:
    s = f.read()
    rotated = s
with open('rotation.out','w') as f:
        for i in range(len(s)):
                rotated = s[i:] + s[:i]
                f.write(rotated +'\n')



