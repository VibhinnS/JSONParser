from parse_obj import ObjectParser
from parse_array import ArrayParser
from parse_number import NumberParser
from parse_bool import BoolParser
from parse_string import StringParser


class MyJSONParser:
    def __init__(self, json_string):
        self.json_string = json_string
        self.index = 0

    def parse(self):
        if not self.json_string:
            return None

        self.index = 0
        return self.parse_value()

    def parse_value(self):
        char = self.get_next_char()
        if char == '{':
            return ObjectParser(self).parse()
        elif char == '[':
            return ArrayParser(self).parse()
        elif char == '"':
            return StringParser(self).parse()
        elif char.isdigit() or char == '-':
            return NumberParser(self).parse()
        elif char.isalpha():
            return BoolParser(self).parse()
        else:
            raise ValueError(f"Unexpected character: {char}")

    def get_next_char(self):
        if self.index < len(self.json_string):
            return self.json_string[self.index]
        else:
            return None

    def consume_char(self, expected_char):
        if self.get_next_char() == expected_char:
            self.index += 1
        else:
            raise ValueError(f"Expected '{expected_char}', got '{self.get_next_char()}' at position {self.index}")


# Example usage
json_string = '{"key1":true,"key2":false,"key3":{"inner-obj":"vibhinn"},"key4":"value","key7":["list values"]}'
my_parser = MyJSONParser(json_string)
parsed_data = my_parser.parse()
print(parsed_data)
