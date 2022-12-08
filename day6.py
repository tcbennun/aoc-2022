d = open("day6.txt").read()

def do_it(n):
    for i in range(len(d) - n):
        if len(set(d[i:i + n])) == n:
            print(i + n)
            break

do_it(4)
do_it(14)
