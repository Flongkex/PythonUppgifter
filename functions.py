def double(n):
    return n*2

def triple(n):
    return n*3

def quadrupel(n):
    return double(double(n)) # 2*2*n

def funky(n, m):
    return triple(n) + quadrupel(m)

a = 3
b = 14

#print(double(a))
#print(double(b))

#print(triple(a))
#print(triple(b))

#print(quadrupel(a))
#print(quadrupel(b))    

#print(funky(a,b))
#print(funky(b,b))
