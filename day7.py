def mkdir(parent): return {"tot": 0, "parent": parent}
dirs = [mkdir(None)]
cwd = dirs[0]
for line in open("day7.txt"):
    tks = [t.strip() for t in line.split(" ")]
    if line.startswith("$ cd"):
        if tks[2] == "..":
            cwd = cwd["parent"]
        elif tks[2] != "/":
            dirs.append(mkdir(cwd))
            cwd = dirs[-1]
    elif tks[0].isdigit():
        walk = cwd
        while walk != None:
            walk["tot"] += int(tks[0])
            walk = walk["parent"]

print(sum(d["tot"] for d in dirs if d["tot"] <= 100000))
print(min(d["tot"] for d in dirs if d["tot"] >= dirs[0]["tot"] - 40000000))
