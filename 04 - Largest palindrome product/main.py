
m = "0"

for r1 in range(999,99,-1):
    for r2 in range(999,99,-1):
        p = "%s"%(r1*r2)
        if p[(len(p)/2):] == p[:len(p)/2][::-1]:
            if p > m :
                m = p
print m