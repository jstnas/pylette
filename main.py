from replacer.slock import SlockReplacer
from replacer.st import StReplacer
from replacer.dwm import DwmReplacer
from replacer.tabbed import TabbedReplacer
from replacer.mt import MtReplacer

def load_palette(palette_filepath: str):
    with open(palette_filepath, 'r') as palette_file:
        palette = palette_file.read().split('\n')
    palette.pop()
    return palette

if __name__ == '__main__':
    palette = load_palette('palettes/fellow.txt')
    SlockReplacer('/home/iota/repos/slock/config.def.h', palette)
    StReplacer('/home/iota/repos/st/palette.c', palette)
    DwmReplacer('/home/iota/repos/dwm/palette.c', palette)
    DwmReplacer('/home/iota/repos/dmenu/palette.c', palette)
    TabbedReplacer('/home/iota/repos/tabbed/palette.c', palette)
    MtReplacer('monkeytype.txt', palette)

