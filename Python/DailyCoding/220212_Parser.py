src: str; pos: int; sym: str

def nxt():
    global pos, sym
    if pos < len(src): sym, pos = src[pos], pos + 1
    else: sym = chr(0) # end of input symbol

def A(): # A → a A c | b
    if sym == 'a':
        nxt(); A();
        if sym == 'c': nxt()
        else: raise Exception("'c' expected at " + str(pos))
    elif sym == 'b': nxt()
    else: raise Exception("'a' or 'b' expected at " + str(pos))

def parse(s: str):
    global src, pos;
    src, pos = s, 0; nxt(); A()
    if sym != chr(0): raise Exception("unexpected characters at " + str(pos))

parse("aabcc")