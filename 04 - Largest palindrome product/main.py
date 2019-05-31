
m = "0"
for r1 in range(999,99,-1):
    for r2 in range(999,99,-1):
        p = str(r1*r2)
        if  p == p[::-1]:
            if int(p) > int(m) :
                m = p
print(m)