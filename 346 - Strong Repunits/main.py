def repunit(limit):
    setof = set()
    setFin = set()
    for r in range(2,limit+1):
        n = 1
        k = 0
        while k <= limit and r<36: 
            k= int("1"*n,r)
            if not (k <= limit):
                break;
            setof.add(k)
            n+=1
    return setFin
print repunit(50)
