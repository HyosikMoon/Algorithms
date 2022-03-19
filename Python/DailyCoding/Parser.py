# 4TB3 Course, Parser.

IDENT = 0; NUMBER = 1; TRUE = 2; FALSE = 3; LET = 4; IN = 5; IF = 6
THEN = 7; ELSE = 8; DIV = 9; MOD = 10; NOT = 11; AND = 12; OR = 13
TIMES = 14; PLUS = 15; MINUS = 16; EQ = 17; NEQ = 18; LT= 19; GT = 20
LE = 21; GE = 22; LPAREN = 23; RPAREN = 24; COMMA = 25; EOF = 26

KEYWORDS = \
    {'true': TRUE, 'false': FALSE, 'let': LET, 'in': IN, 'if': IF,
    'then': THEN, 'else': ELSE, 'div': DIV, 'mod': MOD, 'not': NOT,
    'and': AND, 'or': OR}

# Scanner
# symbol ::=
#     {ws} (identifier | number | 'true' | 'false' | 'let' | 'in' |
#     'if' | 'then' | 'else' | 'div' | 'mod' | 'not' | 'and' | 'or' |
#     '×' | '+' | '-' | '=' | '≠' | '<' | '>' | '≤' | '≥' | '(' | ')' | ',')
# identifier ::= letter {letter | digit}
# number ::= digit {digit}
# letter ::= 'a' | ... | 'z'
# digit ::= '0' | ... | '9'
# ws ::= ' ' | '\t' | '\r' | '\n'

def getChar():
    global pos, ch
    if pos < len(src): ch, pos = src[pos], pos + 1
    else: ch, pos = chr(0), pos + 1

def error(msg):
    raise Exception(src + '\n' + (pos - 1) * ' ' + '^ ' + msg)

def getSym():
    global sym, val
    while ch in ' \t\r\n': getChar()
    pos0 = pos
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        start = pos - 1
        while ('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or \
              ('0' <= ch <= '9'): getChar()
        val = src[start: pos - 1]
        sym = KEYWORDS[val] if val in KEYWORDS else IDENT
    elif '0' <= ch <= '9':
        val = int(ch); getChar()
        while '0' <= ch <= '9':
            val = 10 * val + int(ch); getChar()
        sym = NUMBER
    elif ch == '×': getChar(); sym = TIMES
    elif ch == '+': getChar(); sym = PLUS
    elif ch == '-': getChar(); sym = MINUS
    elif ch == '=': getChar(); sym = EQ
    elif ch == '≠': getChar(); sym = NEQ
    elif ch == '<': getChar(); sym = LT
    elif ch == '>': getChar(); sym = GT
    elif ch == '≤': getChar(); sym = LE
    elif ch == '≥': getChar(); sym = GE
    elif ch == '(': getChar(); sym = LPAREN
    elif ch == ')': getChar(); sym = RPAREN
    elif ch == ',': getChar(); sym = COMMA
    elif ch == chr(0): sym = EOF
    else: error('unexpected character')
    
# Parser
# expression ::= relation 
#     | "let" identifier idList "=" expression "in" expression 
#     | "if" expression "then" expression "else" expression
# relation ::= arithmetic [("=" | "≠" | "<" | ">" | "≤" | "≥") arithmetic]
# arithmetic ::= ["+" | "-"] term {("+" | "-" | "or") term)}
# term ::= factor {("×" | "div" | "mod" | "and") factor}
# factor ::= integer 
#     | "true" 
#     | "false" 
#     | "(" expression ")" 
#     | "not" expression 
#     | identifier exprList
# exprList ::= ["(" expression {"," expression} ")"]
# idList ::= ["(" identifier {"," identifier} ")"]

class Call:
    def __init__(self, name, args):
        self.name, self.args = name, args
    def __repr__(self):
        return 'Call(' + self.name + ', [' + \
               ', '.join([str(x) for x in self.args]) + '])'

class Unary:
    def __init__(self, op, operand):
        self.op, self.operand = op, operand
    def __repr__(self):
        return 'Unary(' + str(self.op) + ', ' + str(self.operand) + ')'

class Binary:
    def __init__(self, op, left, right):
        self.op, self.left, self.right = op, left, right
    def __repr__(self):
        return 'Binary(' + str(self.op) + ', ' + str(self.left) + \
               ', ' + str(self.right) + ')'

class If:
    def __init__(self, cond, th, el):
        self.cond, self.th, self.el = cond, th, el
    def __repr__(self):
        return 'If(' + str(self.cond) + ', ' + str(self.th) + \
               ', ' + str(self.el) + ')'

class Let:
    def __init__(self, name, par, body, scope):
        self.name, self.par, self.body, self.scope = \
            name, par, body, scope
    def __repr__(self):
        return 'Let(' + self.name + ', ' + str(self.par) + \
               ', ' + str(self.body) + ', ' + str(self.scope) + ')'

# expression(e) ::=
#     relation(e) |
#     "let" identifier(name) idList(par) "=" expression(body)
#         "in" expression(scope) «e := Let(name, par, body, scope)» |
#     "if" expression(cond) "then" expression(th) "else" expression(el)
#         «e := If(cond, th, el)»

def expression():
    if sym in (PLUS, MINUS, NUMBER, TRUE, FALSE, LPAREN, NOT, IDENT):
        return relation()
    elif sym == LET:
        getSym()
        if sym == IDENT: getSym()
        else: error("identifier expected")
        name = val; par = idList();
        if sym == EQ: getSym()
        else: error("'=' expected")
        body = expression()
        if sym == IN: getSym()
        else: error("'in' expected")
        scope = expression()
        return Let(name, par, body, scope)
#### implementation of "if" missing
    else: error("expression expected")

# relation(r) ::=
#     arithmetic(r)
#     ["=" arithmetic(a) «r := Binary(EQ, r, a)» |
#       "≠" arithmetic(a) «r := Binary(NEQ, r, a)» |
#       "<" arithmetic(a) «r := Binary(LT, r, a)» |
#       ">" arithmetic(a) «r := Binary(GT, r, a)» |
#       "≤" arithmetic(a) «r := Binary(LE, r, a)» |
#       "≥" arithmetic(a) «r := Binary(GE, r, a)» ]

def relation():
    r = arithmetic()
    if sym in (EQ, NEQ, LT, GT, LE, GE):
        op = sym; getSym(); r = Binary(op, r, arithmetic())
    return r

# arithmetic(a) ::=
#     ("+" term(a) | "-" term(a) «a := Unary(MINUS, a)» | term(a))
#     { "+" term(t) «a := Binary(PLUS, a, t)» |
#       "-" term(t) «a := Binary(MINUS, a, t)» |
#       "or" term(t) «a := Binary(OR, a, t)» }

def arithmetic():
    if sym == PLUS:
        getSym(); a = term();
    elif sym == MINUS:
        getSym(); a = Unary(MINUS, term())
    else: a = term()
    while sym in (PLUS, MINUS, OR):
        op = sym; getSym(); a = Binary(op, a, term())
    return a

# term(t) ::=
#     factor(t)
#     { "×" factor(f) «t := Binary(TIMES, t, f)» |
#       "div" factor(f) «t := Binary(DIV, t, f)» |
#       "mod" factor(f) «t := Binary(MOD, t, f)» |
#       "and" factor(f) «t := Binary(MOD, t, f)» }

def term():
    t = factor()
    while sym in (TIMES, DIV, MOD, AND):
        op = sym; getSym(); t = Binary(op, t, factor())
    return t
    
# factor(f) ::=
#     integer(val) «f := val» |
#     "true" «f := true» |
#     "false" «f := false» |
#     "(" expression(f) ")" |
#     "not" expression(f) «f := not f» |
#     identifier(name) exprList(para) «f := Call(name, para)»

def factor():
    if sym == NUMBER: f = val; getSym()
    elif sym == TRUE: f = True; getSym()
    elif sym == FALSE: f = False; getSym()
    elif sym == LPAREN:
        getSym(); f = expression()
        if sym == RPAREN: getSym()
        else: error(') missing')
    elif sym == NOT:
        getSym(); f = Unary(NOT, expression())
    elif sym == IDENT:
        name = val; getSym()
        para = exprList()
        f = Call(name, para)
    else: error('unexpected symbol')
    return f

# exprList(el) ::=
#     ("(" expression(e) «el := [e]» {"," expression(e) «el := el + [e]»} ")") |
#     «el := []»

def exprList():
    if sym == LPAREN:
        getSym(); el = [expression()]
        while sym == COMMA:
            getSym(); el.append(expression())
        if sym == RPAREN: getSym()
        else: error(') expected')
    else: el = []
    return el

# idList(il) ::=
#     ("(" identifer(i) «il := [i]» {"," identifier(i) «il := il + [i]»} ")") |
#     «il := []»
    
def idList():
    if sym == LPAREN:
        getSym()
        if sym == IDENT: il = [val]; getSym()
        else: error('identifier expected')
        while sym == COMMA:
            getSym();
            if sym == IDENT: il.append(val); getSym()
            else: error('identifier expected')
        if sym == RPAREN: getSym()
        else: error(') expected')
    else: il = []
    return il

def ast(s):
    global src, pos;
    src, pos = s, 0; getChar(); getSym();
    return expression()

ast('(a)')

assert str(ast('(a)')) == 'Call(a, [])'