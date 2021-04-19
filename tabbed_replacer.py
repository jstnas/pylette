from replacer import Replacer

class TabbedReplacer(Replacer):
    def replace(self):
        content = self.content.split('"')
        colours = [0,  # Normal bg.
                   7,  # Normal fg.
                   3,  # Selected bg.
                   15, # Selected fg.
                   1,  # Important fg.
                   15] # Important bg.
        for i in range(len(colours)):
            content[2 * i + 1] = self.palette[colours[i]]
        self.content = '"'.join(content)
        return
