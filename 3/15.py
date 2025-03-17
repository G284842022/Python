def setdict2pairset(d):
    result = { (char, num) for num, value in d.items() for char in value }
    return result

d2 = { 1:{"x", "y", "z"}, 2:{"x", "z"}, 3:{"y"}}
print(setdict2pairset(d2))
