from ansi import _sgr

class SGR:
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