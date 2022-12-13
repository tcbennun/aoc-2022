from functools import cmp_to_key

def pad(a, b):
    if len(a) > len(b):
        return a, b + [None] * (len(a) - len(b))
    elif len(a) < len(b):
        return a + [None] * (len(b) - len(a)), b
    else:
        return a, b

def cmp(a, b):
    a_l, b_l = isinstance(a, list), isinstance(b, list)
    if a is None:
        val = -1
    elif b is None:
        val = 1
    elif a_l and b_l:
        val = 0
        for c, d in zip(*pad(a, b)):
            val = cmp(c, d)
            if val != 0:
                break
    elif a_l:
        val = cmp(a, [b])
    elif b_l:
        val = cmp([a], b)
    else:
        val = a - b
    return val

d = [eval(l) for l in open("day13.txt") if len(l.strip()) != 0]

print(sum((i + 1) * (cmp(d[n], d[n + 1]) < 0) for i, n in enumerate(range(0, len(d), 2))))

o = sorted(d + [[[2]], [[6]]], key=cmp_to_key(cmp))
print((1 + o.index([[2]])) * (1 + o.index([[6]])))
