from replacer import Replacer

class DwmReplacer(Replacer):
    def replace(self):
        content = self.content.split('"')
        # Grays.
        grays = [0,
                 8,
                 7,
                 15]
        for i in range(4):
            content[2 * i + 1] = self.palette[grays[i]]
        # Accent.
        content[9] = self.palette[3]
        self.content = '"'.join(content)
        return
