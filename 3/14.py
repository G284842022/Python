def pairset2setdict(s):
    result = {}
    for c, n in s:
        if not n in result:
            result[n] = set()
        result[n].add(c)
    return result


s1 = {("x", 1), ("x", 2), ("y", 1), ("y", 3), ("z", 1), ("z", 2)}

print(pairset2setdict(s1))