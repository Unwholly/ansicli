from ansi import Ansi

class Private:
    CURINV = f'{Ansi.CSI}?25l'
    CURVIS = f'{Ansi.CSI}?25h'

    SCREENRESTORE = f'{Ansi.CSI}?47l'
    SAVESCREEN = f'{Ansi.CSI}?25h'

    SAVE_CURSOR_ENABLE_ALT_BUFF = f'{Ansi.CSI}?1049h'
    RESTORE_CURSORE_DISABLE_ALT_BUFF = f'{Ansi.CSI}?1049l'