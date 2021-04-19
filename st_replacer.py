from replacer import Replacer

class StReplacer(Replacer):
    def replace(self):
        content = self.content.split('"')
        # Base colours.
        for i in range(16):
            content[2 * i + 1] = self.palette[i]
        # Cursor and background.
        content[33] = self.palette[3]
        content[35] = self.palette[11]
        content[37] = self.palette[0]
        self.content = '"'.join(content)
        return
