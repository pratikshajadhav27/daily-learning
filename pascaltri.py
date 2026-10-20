def getRow(rowIndex: int):
    r = [1]
    for _ in range(rowIndex): r = [x + y for x, y in zip([0] + r, r + [0])]
    return r