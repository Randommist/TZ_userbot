import unittest
from utils import *


class TestParsePhoneNumber(unittest.TestCase):
    def test_parse_number(self):
        self.assertEqual(parse_phone_number("89656523432"), "79656523432")
        self.assertEqual(parse_phone_number("+7 929 361-55-57"), "79293615557")
        self.assertEqual(parse_phone_number("7976-(343)-42-55"), "79763434255")
        self.assertEqual(parse_phone_number("foo baz"), None)


class TestParseCommand(unittest.TestCase):
    def test_parse_command(self):
        self.assertEqual(parse_commnand("#check 89656523432"), ("check", "89656523432"))
        self.assertEqual(
            parse_commnand("#ban +7 929 361-55-57"), ("ban", "+7 929 361-55-57")
        )
        self.assertEqual(parse_commnand("#ban foo baz"), ("ban", "foo baz"))


class TestParseCheckArgs(unittest.TestCase):
    def test_parse_check_args(self):
        self.assertEqual(parse_check_args("89656523432"), "89656523432")


class TestParseBanArgs(unittest.TestCase):
    def test_parse_ban_args(self):
        self.assertEqual(
            parse_ban_args("+7 929 361-55-57 любой текст one two three 10 20 30"),
            ("+7 929 361-55-57", "любой текст one two three 10 20 30"),
        )
        self.assertEqual(
            parse_ban_args("+7 929 361 55 57 a10 b20 c30"),
            ("+7 929 361 55 57", "a10 b20 c30"),
        )
        self.assertEqual(
            parse_ban_args("+7 929 361 55 57"),
            ("+7 929 361 55 57", ""),
        )
