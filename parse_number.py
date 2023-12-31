class NumberParser:
    def __init__(self, main_parser):
        self.main_parser = main_parser

    def parse(self):
        result = ''
        while self.main_parser.get_next_char().isdigit() or self.main_parser.get_next_char() in ('.', '-'):
            result += self.main_parser.get_next_char()
            self.main_parser.index += 1

        try:
            return float(result) if '.' in result else int(result)
        except ValueError:
            raise ValueError(f"Invalid number format: {result}")
