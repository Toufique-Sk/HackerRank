import sys

def catAndMouse(x, y, z):
    if abs(z-x)<abs(z-y):
        return "Cat A"
    elif abs(z-x)>abs(z-y):
        return "Cat B"
    if abs(z-x)==abs(z-y):
        return "Mouse C"

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        x, y, z = raw_input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print result