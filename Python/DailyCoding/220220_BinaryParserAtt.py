src: str; pos: int; sym: str

def nxt():
    global pos, sym
    if pos < len(src): sym, pos = src[pos], pos + 1
    else: sym = chr(0) # end of input symbol

def binary() -> int: # binary(v) → digit(v) { digit(w) « v := 2 × v + w » }
    v = digit()
    while sym in '01': w = digit(); v = v * 2 + w
    return v

def digit() -> int: # digit(v) → '0' « v := 0 » | '1' « v := 1 »
    if sym == '0': nxt(); w = 0
    elif sym == '1': nxt(); w = 1
    else: raise Exception("invalid character at " + str(pos))
    return w

def evaluate(s: str) -> int:
    global src, pos;
    src, pos = s, 0; nxt(); v = binary()
    if sym != chr(0): raise Exception("unexpected character at " + str(pos))
    return v

evaluate("101")