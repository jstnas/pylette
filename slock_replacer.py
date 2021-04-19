from replacer import Replacer

class SlockReplacer(Replacer):
    def replace(self):
        content = self.content.split('"')
        colours = [0, # Init.
                   3, # Input.
                   1] # Error.
        for i in range(3):
            content[2 * i + 5] = self.palette[colours[i]]
        self.content = '"'.join(content)
        return
