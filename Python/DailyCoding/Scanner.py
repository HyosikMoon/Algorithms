# 4TB3 Course, Sanner.

IDENT = 0; NUMBER = 1; TRUE = 2; FALSE = 3; LET = 4; IN = 5; IF = 6
THEN = 7; ELSE = 8; DIV = 9; MOD = 10; NOT = 11; AND = 12; OR = 13
TIMES = 14; PLUS = 15; MINUS = 16; EQ = 17; NEQ = 18; LT= 19; GT = 20
LE = 21; GE = 22; LPAREN = 23; RPAREN = 24; COMMA = 25; EOF = 26

KEYWORDS = \
    {'true': TRUE, 'false': FALSE, 'let': LET, 'in': IN, 'if': IF,
    'then': THEN, 'else': ELSE, 'div': DIV, 'mod': MOD, 'not': NOT,
    'and': AND, 'or': OR}

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