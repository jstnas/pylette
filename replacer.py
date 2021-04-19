class Replacer:
    def __init__(self, filepath: str, palette: list):
        self.palette = palette
        print(f'Replacing {filepath}')
        with open(filepath, 'r') as config_file:
            self.content = config_file.read()
        self.replace()
        with open(filepath, 'w') as config_file:
            config_file.write(self.content)
        return

    def replace(self):
        return
