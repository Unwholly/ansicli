from .ansi import AnsiColor, col
from .ansi import Ansi

class Color:
    BLACK = col(AnsiColor.BLACK)
    RED = col(AnsiColor.RED)
    GREEN = col(AnsiColor.GREEN)
    YELLOW = col(AnsiColor.YELLOW)
    BLUE = col(AnsiColor.BLUE)
    MAGENTA = col(AnsiColor.MAGENTA)
    CYAN = col(AnsiColor.CYAN)
    WHITE = col(AnsiColor.WHITE)
    DEFAULT = col(AnsiColor.DEFAULT)

    OFF = col(AnsiColor.OFF)

    @staticmethod
    def col256(n:int|str): return f'{Ansi.CSI}38;5;{n}m'
    @staticmethod
    def colrgb(r:int|str,g:int|str,b:int|str): return f'{Ansi.CSI}38;2;{r};{g};{b}m'