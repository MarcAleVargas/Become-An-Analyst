print("\nhello, world\n")

def soluction(data):
    values = max([x*data[i] for i, x in enumerate(data[1:])])
    return values
print(soluction([3, 6, -2, -5, 7, 3]))