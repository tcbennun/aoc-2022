import numpy as np

f = list(open("day11.txt"))
monkeys = []
for i in range(0, len(f), 7):
    m = f[i:i + 7]
    op = m[2][23:].strip()
    n = 0
    if op == "* old":
        op = lambda w, _: w * w
    else:
        n = int(op[2:])
        if op[0] == "*":
            op = lambda w, n: w * n
        else:
            op = lambda w, n: w + n
    monkeys.append({
        "items": [int(x) for x in m[1][18:].strip().split(", ")],
        "op": (op, n),
        "test": int(m[3][21:]),
        "throw": (int(m[4][29:]), int(m[5][30:])),
        "count_p1": 0,
        "count_p2": 0,
    })
divs = np.array([m["test"] for m in monkeys])
for m in monkeys:
    m["items_mod"] = [x % divs for x in m["items"]]

for round in range(10000):
    for i, m in enumerate(monkeys):
        if round < 20:
            m["count_p1"] += len(m["items"])
            for w in m["items"]:
                func, param = m["op"]
                w = func(w, param) // 3
                if w % m["test"] == 0:
                    monkeys[m["throw"][0]]["items"].append(w)
                else:
                    monkeys[m["throw"][1]]["items"].append(w)
            m["items"] = []
        m["count_p2"] += len(m["items_mod"])
        for w in m["items_mod"]:
            func, param = m["op"]
            w = func(w, param % divs) % divs
            if w[i] == 0:
                monkeys[m["throw"][0]]["items_mod"].append(w)
            else:
                monkeys[m["throw"][1]]["items_mod"].append(w)
        m["items_mod"] = []

    if round == 19:
        print(np.prod((sorted(m["count_p1"] for m in monkeys))[-2:]))

print(np.prod((sorted(m["count_p2"] for m in monkeys))[-2:]))
