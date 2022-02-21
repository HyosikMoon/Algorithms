# 4TB3 Course, Syntax-Based Tools & Compilers

from typing import Union

pos: int; sym: str; src: str

def nxt():
    global pos, sym
    if pos < len(src): sym, pos = src[pos], pos + 1
    else: sym = chr(0) # end of input symbol

def expression() -> Union[bool, int]:
    ws(); v = simpleExpr()
    if sym == '=':
        nxt(); ws(); w = simpleExpr()
        if type(v) == type(w): v = v == w
        else: raise Exception("incompatible operands of '=' at " + str(pos))
    elif sym == '<':
        nxt(); ws(); w = simpleExpr()
        if type(v) == int == type(w): v = v < w
        else: raise Exception("not int operands of '<' at " + str(pos))
    return v

def simpleExpr() -> Union[bool, int]:
    v = term()
    while sym in '+|':
        if sym == '+':
            nxt(); ws(); w = term()
            if type(v) == int == type(w): v = v + w
            else: raise Exception("not int operands of '+' at " + str(pos))
        else: # sym == '|'
            nxt(); ws(); w = term()
            if type(v) == bool == type(w): v = v or w
            else: raise Exception("not bool operands of '|' at " + str(pos))
    return v

def term() -> Union[bool, int]:
    v = factor()
    while sym in '*&':
        if sym == '*':
            nxt(); ws(); w = factor()
            if type(v) == int == type(w): v = v * w
            else: raise Exception("not int operands of '*' at " + str(pos))
        else: # sym == '&'
            nxt(); ws(); w = factor()
            if type(v) == bool == type(w): v = v and w
            else: raise Exception("not bool operands of '&' at " + str(pos))
    return v

def factor() -> Union[bool, int]:
    if '0' <= sym <= '9': v = integer()
    elif sym == '(':
        nxt(); v = expression()
        if sym == ')': nxt(); ws()
        else: raise Exception("')' expected at " + str(pos))
    else: raise Exception("invalid character at " + str(pos))
    return v

def integer() -> int:
    v = digit()
    while '0' <= sym <= '9': v = 10 * v + digit()
    ws()
    return v

def digit() -> int:
    # '0' <= sym <= '9'
    v = ord(sym) - ord('0'); nxt()
    return v

def ws():
    while sym == ' ': nxt()

def evaluate(s: str) -> int:
    global src, pos;
    src, pos = s, 0; nxt(); v = expression()
    if sym != chr(0): raise Exception("unexpected characters at " + str(pos))
    return v


# evaluate("2 * (3 < 4)") # not int operands of '*' at 11
# evaluate("2 & 3") # not bool operands of '&' at 5
# evaluate("(2 < 3) = (3 < 4)") # returns True
evaluate("(2 < 3) = (3 = 4)") # returns False