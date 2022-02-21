# 4TB3 Course, Syntax-Based Tools & Compilers

src: str; pos: int; sym: str

def nxt():
    global pos, sym
    if pos < len(src): sym, pos = src[pos], pos + 1
    else: sym = chr(0) # end of input symbol

def expression() -> int: # expression(v) → ws term(v) { '+' ws term(w) « v := v + w » }
    ws(); v = term()
    while sym == '+': nxt(); ws(); w = term(); v = v + w
    return v

def term() -> int: # term(v) → factor(v) { '*' ws factor(w) « v := v * w » }
    v = factor()
    while sym == '*': nxt(); ws(); w = factor(); v = v * w
    return v

def factor() -> int: # factor(v) → integer(v) | '(' expression(v) ')' ws
    if '0' <= sym <= '9': v = integer()
    elif sym == '(':
        nxt(); v = expression()
        if sym == ')': nxt(); ws()
        else: raise Exception("')' expected at " + str(pos))
    else: raise Exception("invalid character at " + str(pos))
    return v

def integer() -> int: # integer(v) → digit(v) { digit(w) « v := 10 * v + w » } ws
    v = digit()
    while '0' <= sym <= '9': v = 10 * v + digit()
    ws()
    return v

def digit() -> int: # digit(v) → '0' « v := 0 » | … | '9' « v := 9 »
    # '0' <= sym <= '9'
    v = ord(sym) - ord('0'); nxt()
    return v

def ws(): # ws → { ' ' }
    while sym == ' ': nxt()

def evaluate(s: str) -> int:
    global src, pos;
    src, pos = s, 0; nxt(); v = expression()
    if sym != chr(0): raise Exception("unexpected character at " + str(pos))
    return v

evaluate("(2 + 3) * 4 + 5")