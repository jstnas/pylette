from urllib.parse import quote_plus
from .replacer import Replacer

class MtReplacer(Replacer):
    def replace(self):
        content = []
        colours = [0,  # Bg.
                   3,  # Main.
                   3,  # Caret.
                   7,  # Sub.
                   15, # Text.
                   9,  # Error.
                   1,  # Extra Error.
                   9,  # Colourful mode Error.
                   1,] # Colourful mode Extra Error.
        for i in range(len(colours)):
            colour = self.palette[colours[i]]
            content.append(colour)
        content = ','.join(content)
        content = quote_plus(content)
        self.content = f'https://monkeytype.com?customTheme={content}'
        return
