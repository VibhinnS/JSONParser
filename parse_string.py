class StringParser:
    def __init__(self, main_parser):
        self.main_parser = main_parser

    def parse(self):
        result = ''
        self.main_parser.consume_char('"')
        while self.main_parser.get_next_char() != '"':
            char = self.main_parser.get_next_char()
            if char == '\\':
                result += char
                result += self.main_parser.get_next_char()
            else:
                result += char
            self.main_parser.index += 1
        self.main_parser.consume_char('"')
        return result
