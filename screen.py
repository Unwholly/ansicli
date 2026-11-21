from ansi import Ansi

class Screen:
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