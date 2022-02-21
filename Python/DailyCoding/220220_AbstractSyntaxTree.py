# 4TB3 Course, Syntax-Based Tools & Compilers

from textwrap import indent

class Expr: pass

class Ident(Expr):
    def __init__(self, ident: str):
        self.ident = ident
    def __str__(self) -> str:
        return self.ident

class Minus(Expr):
    def __init__(self, arg: Expr):
        self.arg = arg
    def __str__(self) -> str:
        return '-\n' + indent(str(self.arg), '  ')

class Times(Expr):
    def __init__(self, left: Expr, right: Expr):
        self.left, self.right = left, right
    def __str__(self) -> str:
        return '*\n' + indent(str(self.left), '  ') + '\n' + indent(str(self.right), '  ')

class Plus(Expr):
    def __init__(self, left: Expr, right: Expr):
        self.left, self.right = left, right
    def __str__(self) -> str:
        return '+\n' + indent(str(self.left), '  ') + '\n' + indent(str(self.right), '  ')

pos: int; sym: str; src: str

def nxt():
    global pos, sym
    if pos < len(src): sym, pos = src[pos], pos + 1
    else: sym = chr(0) # end of input symbol

def expression() -> Expr:
    # expression(t) → ws term(t) { '+' ws term(u) « t := Plus(t, u) » }
    ws(); t = term()
    while sym == '+': nxt(); ws(); t = Plus(t, term())
    return t

def term() -> Expr:
    # term(t) → factor(t) { '*' ws factor(u) « t := Times(t, u) » }
    t = factor()
    while sym == '*': nxt(); ws(); t = Times(t, term())
    return t

def factor() -> Expr:
    # factor(t) →  '-' ws atom(t) « t := Minus(t) » | atom(t)
    if sym == '-': nxt(); ws(); t: Expr = Minus(atom())
    else: t = atom()
    return t

def atom() -> Expr:
    # atom(t) → identifier(i) « t := Ident(i) » | '(' expression(t) ')' ws
    if 'a' <= sym <= 'z': t: Expr = Ident(identifier())
    elif sym == '(':
        nxt(); t = expression()
        if sym == ')': nxt(); ws()
        else: raise Exception("')' expected at " + str(pos))
    else: raise Exception("invalid character at " + str(pos))
    return t

def identifier() -> str:
    # identfier(i) → letter(i) { letter(l) « i := i + l » } ws
    i = letter()
    while 'a' <= sym <= 'z': i += letter()
    ws()
    return i

def letter() -> str:
    # letter(l) → 'a' « l := 'a' » | … | 'z' « l := 'z' »
    # 'a' <= sym <= 'z'
    l = sym; nxt()
    return l

def ws():
    # ws → { ' ' }
    while sym == ' ': nxt()

def ast(s) -> Expr:
    global src, pos;
    src, pos = s, 0; nxt(); t = expression()
    if sym != chr(0): raise Exception("unexpected character at " + str(pos))
    return t

print(ast('- a + c * y'))