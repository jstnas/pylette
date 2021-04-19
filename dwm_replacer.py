from replacer import Replacer

class DwmReplacer(Replacer):
    def replace(self):
        content = self.content.split('"')
        # Grays.
        grays = [self.palette[0],
                self.palette[8],
                self.palette[7],
                self.palette[15]]
        for i in range(4):
            content[2 * i + 1] = grays[i]
        # Accent.
        content[9] = self.palette[3]
        self.content = '"'.join(content)
        return
