import math
def babyStep(g, p, n):
    """ Calculates e, g^1, g^2, ..., g^n in mod ring p. """
    babyList = dict()
    for i in range(n + 1):
        baby = pow(g, i, p)
        babyList[baby] = i
    return babyList

def shanksSolution(g, p, h):
    """ 
    Uses Shank's Babystep Giantstep Algorithm to calculate the discrete log problem
    *** find x in g^x=h mod p ***
    Returns solutions in the form of congruency class x mod (p-1)
    """
    n = math.ceil(math.sqrt(p - 1))
    babyList = babyStep(g, p, n)
    # use fermat's little theorem to compute negative powers
    base = pow(g, (p - 2) * n, p)
    for j in range(0, n + 1):
        giant = (h * pow(base, j, p)) % p
        if giant in babyList:
            return babyList[giant] + j * n
    # no solution
    return None

def testShanksSolution():
    assert(shanksSolution(15, 13, 122) == 9)
    assert(shanksSolution(11, 137, 1226) == 31)
    assert(shanksSolution(113, 137, 1226) == 122)
    assert(shanksSolution(17777, 1823, 4) == 560)
    print("All tests passed; the algorithm seems to be implemented correctly.")

testShanksSolution()