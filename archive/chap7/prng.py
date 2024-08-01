x = 0
a = 81
c = 337
m = 1000

def rand():
    global x
    x = (a * x + c) % m
    return x

def reset(mult, inc, mod):
    global x,a,c,m
    x = 0
    a = mult
    c = inc
    m = mod
