#!/usr/bin/env python3

import re
from datetime import datetime
import argparse
from sys import exit

from jmbg_validator.exceptions import (
    InvalidJMBG,
    InvalidJMBGLength,
    InvalidDateException,
    NotANumber,
    InvalidRegion,
)
from jmbg_validator.matrices import REGION_MATRIX
from jmbg_validator.output import JMBG

REGEX = r"(\d{2})(\d{2})(\d{3})(\d{2})(\d{3})(\d{1})"
DATETIME_FORMAT = "%d.%m.%Y."
OUTPUT_CHOICES = ["table", "text", "json"]


def verify_date(day, month, year):
    try:
        if isinstance(day, str):
            day = int(day)

        if isinstance(month, str):
            month = int(month)

        datetime(year, month, day)

        return True

    except (ValueError, TypeError):
        raise InvalidDateException(f"Datum {day}.{month}.{year} nije validan.")


def verify_length(jmbg):
    try:
        if len(jmbg) != 13:
            raise InvalidJMBGLength(f"JMBG mora da ima 13 znakova, ne {len(jmbg)}.")
        else:
            return True
    except TypeError:
        raise InvalidJMBGLength(f"JMBG mora biti string, ne {type(jmbg)}.")


def verify_is_number(jmbg):
    try:
        if not jmbg.isdigit():
            raise NotANumber(f"JMBG ne može da sadrži slova.")

    except AttributeError:
        raise NotANumber(f"JMBG mora biti string, ne {type(jmbg)}.")

    return True


def get_sum(jmbg):
    first = jmbg[0:6]
    second = jmbg[6:-1]
    multiplier = [7, 6, 5, 4, 3, 2]

    first_sum = sum([int(a) * b for a, b in zip(first, multiplier)])
    second_sum = sum([int(a) * b for a, b in zip(second, multiplier)])

    return first_sum + second_sum


def verify_control(jmbg_sum, control):
    control = int(control)
    remainder = jmbg_sum % 11

    if remainder > 1:
        return control == 11 - remainder

    elif remainder == 0 and remainder == control:
        return True

    return False


def split_fields(jmbg):
    match = re.match(REGEX, jmbg)

    if not match:
        raise InvalidJMBG(f"JMBG '{jmbg}' nije ispravan")

    return match.groups()


def get_sex(sex):
    sex = int(sex)

    if 0 <= sex <= 499:
        return "muški"

    elif 500 <= sex <= 999:
        return "ženski"

    else:
        raise Exception(f"Pol mora biti u rasponu od 0-499 i 500-999, ne '{sex}'")


def get_dob(day, month, year):
    return datetime(int(year), int(month), int(day)).strftime(DATETIME_FORMAT)


def get_region(region):
    region = str(region)
    try:
        return REGION_MATRIX[region]

    except KeyError:
        raise InvalidRegion(f"Region '{region}' ne postoji")


def _parse_args():
    parser = argparse.ArgumentParser(description="Validira i ispisuje osnovne podatke o JMBGu")
    parser.add_argument("jmbg", help="13 karaktera JMBGa")
    parser.add_argument(
        "--output",
        "-o",
        default="table",
        required=False,
        choices=OUTPUT_CHOICES,
    )

    return parser.parse_args()


def validate(jmbg):
    if verify_length(jmbg) and verify_is_number(jmbg):
        day, month, year, region, sex, control = split_fields(jmbg)
        human_year = int(f"1{year}")

        if verify_date(day, month, human_year):
            sex = get_sex(sex)
            dob = get_dob(day, month, human_year)
            region = get_region(region)

            jmbg_sum = get_sum(jmbg)
            valid = verify_control(jmbg_sum, control)

            return JMBG(sex, dob, valid, region)


def cli():
    args = _parse_args()

    try:
        if args.output.lower() == "table":
            print(validate(args.jmbg).to_table())

        elif args.output.lower() == "json":
            print(validate(args.jmbg).to_json().decode())

        else:
            print(validate(args.jmbg).to_text())

    except Exception as ex:
        exit(ex)


if __name__ == "__main__":
    cli()
