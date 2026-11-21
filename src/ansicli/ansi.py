class Ansi:
    ESC = '\x1B'
    CSI = '\x9B'
    CSI = '\x1B['
    DCS = '\x90'
    OSC = '\x9D'

    BEL = '\x07' # Terminal bell
    BS = '\x08' # Backspace
    HT = '\x09' # Horizontal Tab
    LF = '\x0A' # Linefeed/newline
    VT = '\x0B' # Vertical tab
    FF = '\x0C' # Formeed
    NP = '\x0C' # New Page
    CR = '\x0D' # Carriage Return
    ESC = '\x1B' # Escape
    DEL = '\x7F' # Delete

class AnsiStyle:
    RESET = 0
    
    BOLD = 1
    DIM = 2
    ITALIC = 3
    UNDER = 4
    BLINK = 5
    INV = 7
    HIDE = 8
    STRK = 9

    RBOLD = 22
    RDIM = 22
    RITALIC = 23
    RUNDER = 24
    RBLINK = 25
    RINV = 27
    RHIDE = 28
    RSTRK = 29

class AnsiColorBG:
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47
    DEFAULT = 49

    BRIGHTBLACK = 100
    BRIGHTRED = 101
    BRIGHTGREEN = 102
    BRIGHTYELLOW = 103
    BRIGHTBLUE = 104
    BRIGHTMAGENTA = 105
    BRIGHTCYAN = 106
    BRIGHTWHITE = 107

def col(n:int|str): return f'{Ansi.CSI}{n}m'

def col256(n:int|str): return f'{Ansi.CSI}38;5;{n}m'
def col256bg(n:int|str): return f'{Ansi.CSI}48;5;{n}m'

def colrgb(r:int|str,g:int|str,b:int|str): return f'{Ansi.CSI}38;2;{r};{g};{b}m'
def colrgbbg(r:int|str,g:int|str,b:int|str): return f'{Ansi.CSI}48;2;{r};{g};{b}m'

class AnsiColor:
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37
    DEFAULT = 39

    BRIGHTBLACK = 90
    BRIGHTRED = 91
    BRIGHTGREEN = 92
    BRIGHTYELLOW = 93
    BRIGHTBLUE = 94
    BRIGHTMAGENTA = 95
    BRIGHTCYAN = 96
    BRIGHTWHITE = 97

    bg = AnsiColorBG

    # col256 = _col256
    # col256bg = _col256bg
    # colrgb = _colrgb
    # colrgbbg = _colrgbbg


def _sgr(n:int|str): return f'{Ansi.CSI}{n}m'

def sgr(*n:int|str):
    s = f'{Ansi.CSI}'
    r = ''
    for i in n: r+=f'{i}{';' if len(r)/2 < len(n) else ''}'
    return f'{s}{r}m'

class AnsiSGR:
    RESET = _sgr(0)

    BOLD = _sgr(1)
    DIM = _sgr(2)
    ITALIC = _sgr(3)
    UNDER = _sgr(4)
    BLINK = _sgr(5)
    INV = _sgr(7)
    HIDE = _sgr(8)
    STRK = _sgr(9)

    RBOLD = _sgr(22)
    RDIM = _sgr(22)
    RITALIC = _sgr(23)
    RUNDER = _sgr(24)
    RBLINK = _sgr(25)
    RINV = _sgr(27)
    RHIDE = _sgr(28)
    RSTRK = _sgr(29)

    # sgr = _sgrgroup

def goto(ln:int|str,col:int|str): return f'{Ansi.CSI}{ln};{col}H'
def up(n:int|str=1): return f'{Ansi.CSI}{n}A'
def down(n:int|str=1): return f'{Ansi.CSI}{n}B'
def right(n:int|str=1): return f'{Ansi.CSI}{n}C'
def left(n:int|str=1): return f'{Ansi.CSI}{n}D'
def upln(n:int|str): return f'{Ansi.CSI}{n}E'
def downln(n:int|str): return f'{Ansi.CSI}{n}F'
def clmn(n:int|str): return f'{Ansi.CSI}{n}G'

class AnsiMove:
    HOME = f'{Ansi.CSI}H'

    UP = f'{Ansi.CSI}A'
    DOWN = f'{Ansi.CSI}B'
    RIGHT = f'{Ansi.CSI}C'
    LEFT = f'{Ansi.CSI}D'

    SCROLLUP = f'{Ansi.ESC} M'
    SAVE = f'{Ansi.ESC} 7'
    LD = f'{Ansi.ESC} 8'
    SAVESCO = f'{Ansi.CSI}s'
    LDSCO = f'{Ansi.CSI}u'

    # goto = _goto
    # up = _up
    # down = _down
    # right = _right
    # left = _left
    # upln = _upln
    # downln = _downln
    # col = _col

class AnsiErase:
    ER2END = f'{Ansi.CSI}J'
    ER2START = f'{Ansi.CSI}1J'
    ERSCREEN = f'{Ansi.CSI}2J'
    ERSAVED = f'{Ansi.CSI}3J'
    ER2EOL = f'{Ansi.CSI}K'
    ERSTART2CUR = f'{Ansi.CSI}1K'
    ERLNANDRETURN = f'{Ansi.CSI}2K{Ansi.CR}'

def resetscreen(n:int|str): return f'{Ansi.CSI}={n}l'

class AnsiScreen:
    MONO_TXT_40x25 = f'{Ansi.CSI}=0h'
    COL_TXT_40x25 = f'{Ansi.CSI}=1h'
    MONO_TXT_80x25 = f'{Ansi.CSI}=2h'
    COL_TXT_80x25 = f'{Ansi.CSI}=3h'
    COLOR4_GRPH_320x200 = f'{Ansi.CSI}=4h'
    MONO_GRPH_320x200 = f'{Ansi.CSI}=5h'
    MONO_GRPH_640x200 = f'{Ansi.CSI}=6h'
    LINEWRAP = f'{Ansi.CSI}=7h'
    COLOR_GRPH_320x200 = f'{Ansi.CSI}=13h'
    COLOR16_GRPH_640x200 = f'{Ansi.CSI}=14h'
    MONO2_GRPH_640x350 = f'{Ansi.CSI}=15h'
    COLOR16_GRPH_640x350 = f'{Ansi.CSI}=16h'
    MONO2_GRPH_640x380 = f'{Ansi.CSI}=17h'
    COLOR16_GRPH_640x480 = f'{Ansi.CSI}=18h'
    COLOR256_GRPH_320x200 = f'{Ansi.CSI}=19h'

    # reset = _resetscreen

class AnsiPrivateMode:
    CURINV = f'{Ansi.CSI}?25l'
    CURVIS = f'{Ansi.CSI}?25h'

    SCREENRESTORE = f'{Ansi.CSI}?47l'
    SAVESCREEN = f'{Ansi.CSI}?25h'

    SAVE_CURSOR_ENABLE_ALT_BUFF = f'{Ansi.CSI}?1049h'
    RESTORE_CURSORE_DISABLE_ALT_BUFF = f'{Ansi.CSI}?1049l'

def _AnsiKBcode(c:str,s:str|int) -> str: return f'{Ansi.CSI}{c};{s}p'

class AnsiKBShift:
    pass

class AnsiKBCtrl:
    pass

class AnsiKBAlt:
    pass

class AnsiKB:
    CODE = _AnsiKBcode
    shift = AnsiKBShift
    ctrl = AnsiKBCtrl
    alt = AnsiKBAlt

    F1 = '0;59'
    F2 = '0;60'
    F3 = '0;61'
    F4 = '0;62'
    F5 = '0;63'
    F6 = '0;64'
    F7 = '0;65'
    F8 = '0;66'
    F9 = '0;67'
    F10 = '0;68'
    F11 = '0;133'
    F12 = '0;134'

    NHOME = '0;71'
    NUP = '0;72'
    NPGUP = '0;73'
    NLEFT = '0;75'
    NRIGHT = '0;77'
    NEND = '0;79'
    NDOWN = '0;80'
    NPGDOWN = '0;81'
    NINS = '0;82'
    NDEL = '0;83'

    HOME = '224;71'
    UP = '224;72'
    PGUP = '224;73'
    LEFT = '224;75'
    RIGHT = '224;77'
    END = '224;79'
    DOWN = '224;80'
    PGDOWN = '224;81'
    INS = '224;82'
    DEL = '224;83'

    BACKSPACE = '8'
    ENTER = '13'
    TAB = '9'
    NULL = '0;3'

    A = '97'
    B = '98'
    C = '99'
    D = '100'
    E = '101'
    F = '102'
    G = '103'
    H = '104'
    I = '105'
    J = '106'
    K = '107'
    L = '108'
    M = '109'
    N = '110'
    O = '111'
    P = '112'
    Q = '113'
    R = '114'
    S = '115'
    T = '116'
    U = '117'
    V = '118'
    W = '119'
    X = '120'
    Y = '121'
    Z = '122'

    ONE = '49'
    TWO = '50'
    THREE = '51'
    FOUR = '52'
    FIVE = '53'
    SIX = '54'
    SEVEN = '55'
    EIGHT = '56'
    NINE = '57'
    ZERO = '48'

    HYPHEN = '45'
    EQUALS = '61'
    RBRACK = '91'
    LBRACK = '93'
    SPACE = '92' #????
    SEMICOLON = '59'
    APOSTROPHE = '39'
    COMMA = '44'
    PERIOD = '46'
    FSLASH = '47'
    BTICK = '96'

    NENTER = '13'
    NFSLASH = '47'
    NSTAR = '42'
    NHYPHEN = '45'
    NPLUS = '43'
    NFIVE = '0;76'


# Style = AnsiStyle
# SGR = AnsiSGR
# Color = AnsiColor
# Move = AnsiMove
# Erase = AnsiErase
# Screen = AnsiScreen
# Private = AnsiPrivateMode
# KB = AnsiKB