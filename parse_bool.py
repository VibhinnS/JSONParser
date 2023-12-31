class BoolParser:
    def __init__(self, main_parser):
        self.main_parser = main_parser

    def parse(self):
        word = ''
        while self.main_parser.get_next_char().isalpha():
            word += self.main_parser.get_next_char()
            self.main_parser.index += 1
        if word.lower() == 'true':
            return True
        elif word.lower() == 'false':
            return False
        elif word.lower() == 'null' or word.lower() == 'none':
            return None
        else:
            raise ValueError(f"Unexpected word: {word}")
