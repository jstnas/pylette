class Replacer:
    def __init__(self, filepath: str, palette: list):
        self.palette = palette
        print(f'Replacing {filepath}')
        try:
            with open(filepath, 'r') as config_file:
                self.content = config_file.read()
        except FileNotFoundError:
            print(f'{filepath} not found')
        self.replace()
        with open(filepath, 'w') as config_file:
            config_file.write(self.content)
        return

    def replace(self):
        return
