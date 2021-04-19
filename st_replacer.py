from replacer import Replacer

class StReplacer(Replacer):
    def replace(self):
        content = self.content.split('"')
        # Base colours.
        for i in range(16):
            content[2 * i + 1] = self.palette[i]
        # Cursor and background.
        colours = [3,  # cursor.
                   11, # reverse cursor.
                   0]  # background.
        for i in range(3):
            content[2 * i + 33] = self.palette[colours[i]]
        self.content = '"'.join(content)
        return
