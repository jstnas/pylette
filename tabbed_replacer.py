from replacer import Replacer

class TabbedReplacer(Replacer):
    def replace(self):
        content = self.content.split('"')
        colours = [self.palette[0],
                self.palette[7],
                self.palette[3],
                self.palette[15],
                self.palette[1],
                self.palette[15]]
        for i in range(len(colours)):
            content[2 * i + 1] = colours[i]
        self.content = '"'.join(content)
        return
