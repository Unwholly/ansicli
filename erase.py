from ansi import Ansi

class Erase:
    ER2END = f'{Ansi.CSI}J'
    ER2START = f'{Ansi.CSI}1J'
    ERSCREEN = f'{Ansi.CSI}2J'
    ERSAVED = f'{Ansi.CSI}3J'
    ER2EOL = f'{Ansi.CSI}K'
    ERSTART2CUR = f'{Ansi.CSI}1K'
    ERLNANDRETURN = f'{Ansi.CSI}2K{Ansi.CR}'

    @staticmethod
    def resetscreen(n:int|str): return f'{Ansi.CSI}={n}l'