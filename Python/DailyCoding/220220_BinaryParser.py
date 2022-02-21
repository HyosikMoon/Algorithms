# 4TB3 Course, Syntax-Based Tools & Compilers

src: str; pos: int; sym: str

def nxt():
    global pos, sym
    if pos < len(src): sym, pos = src[pos], pos + 1
    else: sym = chr(0) # end of input symbol

def binary(): # binary → digit { digit }
    digit()
    while sym in '01': digit()

def digit(): # digit → '0' | '1'
    if sym == '0': nxt()
    elif sym == '1': nxt()
    else: raise Exception("invalid character at " + str(pos))

def parse(s: str):
    global src, pos;
    src, pos = s, 0; nxt(); binary()
    if sym != chr(0): raise Exception("unexpected character at " + str(pos))

parse("101")