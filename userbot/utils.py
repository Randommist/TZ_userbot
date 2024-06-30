from pathlib import Path
import re
import sys
import unittest
import phonenumbers


def get_work_dir() -> str:
    return str(Path(sys.argv[0]).parent.parent)


def parse_commnand(text: str) -> tuple[str, str]:
    if text[0] != "#":
        raise ValueError("Not a command")
    text = text[1:]
    s = text.split(" ")
    command = s[0]
    args = " ".join(s[1:])
    return command, args


def parse_check_args(text: str) -> str:
    return text


def parse_ban_args(text: str) -> tuple[str, str]:
    two_args_regex = r"([\d+\-\(\)\s]+)\s([а-яА-Яa-zA-Z_].+)"
    one_args_regex = r"([\d+\-\(\)\s]+)"
    args_match = re.search(two_args_regex, text)
    if args_match:
        phone_number = args_match.group(1)
        ban_text = args_match.group(2)
        return phone_number, ban_text
    args_match = re.search(one_args_regex, text)
    if args_match:
        phone_number = args_match.group(1)
        return phone_number, ""
    raise ValueError("Not a ban args")


def parse_phone_number(text: str) -> str | None:
    try:
        phone = phonenumbers.parse(text, "RU")
        if phone.country_code is None or phone.national_number is None:
            return
        return str(phone.country_code) + str(phone.national_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return
