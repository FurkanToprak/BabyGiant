import math
def babyStep(g, p, n):
    """ Calculates e, g^1, g^2, ..., g^n in mod ring p. """
    babyList = dict()
    for i in range(n + 1):
        baby = (g ** i) % p
        babyList[baby] = i
    return babyList

def giantStepIter(g, p, n, h, j):
    """ Calculates the j'th item of the giant"""
    return (h * g ** ((-j * n) % (p - 1))) % p

def shanksSolution(g, p, h):
    N = p - 1
    n = math.floor(math.sqrt(N)) + 1
    babyList = babyStep(g, p, n)
    for j in range(0, n):
        giant = giantStepIter(g, p, n, h, j)
        if giant in babyList:
            return babyList[giant] + j * n
    # no solution
    return None

print(shanksSolution(15, 13, 122))