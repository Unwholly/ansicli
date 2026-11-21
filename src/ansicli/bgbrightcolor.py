from .ansi import AnsiColorBG, col

class BgBrightColor:
    BLACK = col(AnsiColorBG.BRIGHTBLACK)
    RED = col(AnsiColorBG.BRIGHTRED)
    GREEN = col(AnsiColorBG.BRIGHTGREEN)
    YELLOW = col(AnsiColorBG.BRIGHTYELLOW)
    BLUE = col(AnsiColorBG.BRIGHTBLUE)
    MAGENTA = col(AnsiColorBG.BRIGHTMAGENTA)
    CYAN = col(AnsiColorBG.BRIGHTCYAN)
    WHITE = col(AnsiColorBG.BRIGHTWHITE)
    DEFAULT = col(AnsiColorBG.DEFAULT)