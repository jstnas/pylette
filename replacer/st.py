from .replacer import Replacer

class StReplacer(Replacer):
    def replace(self):
        content = self.content.split('\n')
        colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 3, 11, 0]
        c = 0
        for l in range(len(content)):
            if content[l][:3] == '\t"#':
                color = self.palette[colors[c]]
                content[l] = f'\t"{color}",'
                c += 1
        self.content = '\n'.join(content)
        return
