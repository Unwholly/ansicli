from .ansi import AnsiColorBG, col
from .ansi import Ansi

class BgColor:
    BLACK = col(AnsiColorBG.BLACK)
    RED = col(AnsiColorBG.RED)
    GREEN = col(AnsiColorBG.GREEN)
    YELLOW = col(AnsiColorBG.YELLOW)
    BLUE = col(AnsiColorBG.BLUE)
    MAGENTA = col(AnsiColorBG.MAGENTA)
    CYAN = col(AnsiColorBG.CYAN)
    WHITE = col(AnsiColorBG.WHITE)
    DEFAULT = col(AnsiColorBG.DEFAULT)

    OFF = col(AnsiColorBG.OFF)

    @staticmethod
    def col256(n:int|str): return f'{Ansi.CSI}48;5;{n}m'
    @staticmethod
    def colrgb(r:int|str,g:int|str,b:int|str): return f'{Ansi.CSI}48;2;{r};{g};{b}m'