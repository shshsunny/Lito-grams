import random
#This is a new configured IDE!
def fac(num):
    if num == 1:
        return 1
    return fac(num - 1) * num
def turn(ev, defa = '', log = False):
    re = ''
    count = 0
    while eval(ev):
        count += 1
        text = list(input()) if not defa else list(defa)
        new = []
        if not text:
            break
        for i in text:
            new.insert(random.randint(0, len(new)), i)
        re = list(new)
        re = ''.join(map(str, re))
        if log:
            print("(* . *) >> ", re)
    print("Bye!")
    return 1, count, fac(len(defa))

#turn('True')
def until(string, log = True):
    g = turn('re != "' + string + '"', string, log)
    return str(g[0] * 100.0 / g[1]) +' %', str(100.0 / g[2]) + ' %'

print (until("你好！"))
