import math

def primetestfermat(p):
    rlist = []
    u = p
    b = 2
    
    while u > 10 and b > 2:
        a = round(math.log(p,b)+0.5)
        rlist.append((b,u%a))
        b = b**a % p
        u = p//a
    rlist.append((b,u))

    rmult = 1
    for i in rlist:
        rmult *= i[0]**i[1]
        rmult = rmult % p

    if rmult == b:
        return True
    else:
        return False



print(primetestfermat(2*3*5*7*11*13*7*19*23))
    
