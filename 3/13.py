def swap_dict(d1):
    return {j: i for i, j in d1.items()}

d1 = {1:"a", 2:"b", 3:"c", 4:"d"}
print( swap_dict(d1) )