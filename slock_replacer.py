from replacer import Replacer

class SlockReplacer(Replacer):
    def replace(self):
        content = self.content.split('"')
        content[5] = self.palette[0]
        content[7] = self.palette[3]
        content[9] = self.palette[1]
        self.content = '"'.join(content)
        return
