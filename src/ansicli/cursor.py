from .ansi import Ansi

class Cursor:
    @staticmethod
    def goto(ln:int|str,col:int|str): return f'{Ansi.CSI}{ln};{col}H'
    @staticmethod
    def up(n:int|str=1): return f'{Ansi.CSI}{n}A'
    @staticmethod
    def down(n:int|str=1): return f'{Ansi.CSI}{n}B'
    @staticmethod
    def right(n:int|str=1): return f'{Ansi.CSI}{n}C'
    @staticmethod
    def left(n:int|str=1): return f'{Ansi.CSI}{n}D'
    @staticmethod
    def upln(n:int|str): return f'{Ansi.CSI}{n}E'
    @staticmethod
    def downln(n:int|str): return f'{Ansi.CSI}{n}F'
    @staticmethod
    def clmn(n:int|str): return f'{Ansi.CSI}{n}G'

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