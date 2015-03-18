import math
count = 0

def containOrigin(A,B,C):
    AB = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
    AC = math.sqrt((A[0]-C[0])**2 + (A[1]-C[1])**2)
    BC = math.sqrt((C[0]-B[0])**2 + (C[1]-B[1])**2)

    AO = math.sqrt((A[0])**2 + (A[1])**2)
    CO = math.sqrt((C[0])**2 + (C[1])**2)
    BO = math.sqrt((B[0])**2 + (B[1])**2)

    AOC = math.acos((AO**2 + CO**2 - AC**2 )/(2*AO*CO))
    AOB = math.acos((AO**2 + BO**2 - AB**2 )/(2*AO*BO))
    BOC = math.acos((BO**2 + CO**2 - BC**2 )/(2*BO*CO))

    return "%s"%(AOC+AOB+BOC) == "%s"%(2*math.pi)

with file('triangles.txt') as f:
    for l in f.readlines():
        sl = [int(x) for x in l.strip().split(",")]
        count += containOrigin((sl[0],sl[1]),(sl[2],sl[3]),(sl[4],sl[5]))
print count