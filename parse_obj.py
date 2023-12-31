from parse_string import StringParser


class ObjectParser:
    def __init__(self, main_parser):
        self.main_parser = main_parser

    def parse(self):
        obj = {}
        self.main_parser.consume_char('{')
        while self.main_parser.get_next_char() != '}':
            key = StringParser(self.main_parser).parse()
            self.main_parser.consume_char(':')
            value = self.main_parser.parse_value()
            obj[key] = value
            if self.main_parser.get_next_char() == ',':
                self.main_parser.consume_char(',')
        self.main_parser.consume_char('}')
        return obj
