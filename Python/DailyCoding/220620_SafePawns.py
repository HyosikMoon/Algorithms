def safe_pawns(pawns: set) -> int:
    safe = []
    low = '12345678'
    col = 'abcdefgh'
    for p in pawns:
        # Initial condition
        if p[1] == '1': continue

        # Check if the leftDown and rightDown pawns exist
        leftDown = ''
        colIndex = col.index(p[0])
        lowIndex = low.index(p[1])
        if colIndex != 0:   # not 'a_'
            leftDown = col[colIndex-1] + low[lowIndex-1]
            if leftDown in pawns: safe.append(p)
        
        rightDown = ''
        if colIndex != 7:   # not 'h_'
            rightDown = col[colIndex+1] + low[lowIndex-1]
            if rightDown in pawns: safe.append(p)

    return len(set(safe))

print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))