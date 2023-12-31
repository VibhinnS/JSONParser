class ArrayParser:
    def __init__(self, main_parser):
        self.main_parser = main_parser

    def parse(self):
        arr = []
        self.main_parser.consume_char('[')
        while self.main_parser.get_next_char() != ']':
            value = self.main_parser.parse_value()
            arr.append(value)
            if self.main_parser.get_next_char() == ',':
                self.main_parser.consume_char(',')
        self.main_parser.consume_char(']')
        return arr
