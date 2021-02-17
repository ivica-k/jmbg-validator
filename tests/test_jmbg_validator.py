import unittest

from parameterized import parameterized

from jmbg_validator.exceptions import InvalidJMBG, InvalidJMBGLength, InvalidDateException, NotANumber, InvalidRegion
from jmbg_validator.main import (
    verify_length,
    verify_is_number,
    verify_date,
    split_fields,
    get_region,
    get_sex,
    get_dob,
    get_sum,
    verify_control,
)


class TestJMBGValidator(unittest.TestCase):
    def setUp(self):
        pass

    @parameterized.expand(
        [
            ("1234567890123",),
            ("3210987654321",),
        ]
    )
    def test_verify_length_pass(self, input_string):
        actual_result = verify_length(input_string)

        self.assertTrue(actual_result)

    @parameterized.expand(
        [
            ("123456",),
            ("32109876543212",),
            (32109876543212,),
        ]
    )
    def test_verify_length_fail(self, input_string):
        self.assertRaises(InvalidJMBGLength, verify_length, input_string)

    @parameterized.expand(
        [
            ("123456",),
            ("32109876543212",),
            ("400",),
        ]
    )
    def test_verify_is_number_pass(self, input_string):
        actual_result = verify_is_number(input_string)

        self.assertTrue(actual_result)

    @parameterized.expand(
        [
            ("123456a",),
            ("32109876543212k",),
            ("jmbg",),
            ("Ӝ",),
        ]
    )
    def test_verify_is_number_fail(self, input_string):
        self.assertRaises(NotANumber, verify_is_number, input_string)

    @parameterized.expand(
        [
            (28, 10, 1986),
            (4, 4, 2018),
            (12, 12, 1974),
            (31, 12, 1822),
            (29, 12, 1222),
            (28, 2, 1679),
        ]
    )
    def test_verify_date_pass(self, day, month, year):
        actual_result = verify_date(day, month, year)

        self.assertTrue(actual_result)

    @parameterized.expand(
        [
            (30, 102, 1986),
            (4, 13, 2018),
            (32, 12, 1974),
            (31, 12, 12345),
            (29, 12, "aaaa"),
            (28, "bbbb", 1679),
        ]
    )
    def test_verify_date_fail(self, day, month, year):
        self.assertRaises(InvalidDateException, verify_date, day, month, year)

    @parameterized.expand(
        [
            ("1234567890123", ("12", "34", "567", "89", "012", "3")),
            ("3210987654321", ("32", "10", "987", "65", "432", "1")),
        ]
    )
    def test_split_fields_pass(self, input_string, expected_result):
        actual_result = split_fields(input_string)

        self.assertEqual(actual_result, expected_result)

    @parameterized.expand(
        [
            ("abcdefghjklmn",),
            ("321098765432",),
            ("12345",),
        ]
    )
    def test_split_fields_fail(self, input_string):
        self.assertRaises(InvalidJMBG, split_fields, input_string)

    @parameterized.expand(
        [
            ("89", "Vojvodina, Sremska Mitrovica"),
            ("47", "Severna Makedonija, Tetovo"),
            ("27", "Crna Gora, Berane, Rožaje, Plav, Andrijevica"),
            ("08", "stranci u Vojvodini"),
        ]
    )
    def test_get_region_pass(self, input_string, expected_result):
        actual_result = get_region(input_string)

        self.assertEqual(actual_result, expected_result)

    @parameterized.expand(
        [
            ("97",),
            ("40",),
            ("97",),
            ("54",),
            ("20",),
            ("90",),
        ]
    )
    def test_get_region_fail(self, input_string):
        self.assertRaises(InvalidRegion, get_region, input_string)

    @parameterized.expand(
        [
            ("212", "muški"),
            ("499", "muški"),
            ("001", "muški"),
            ("630", "ženski"),
            ("999", "ženski"),
            ("500", "ženski"),
        ]
    )
    def test_get_sex_pass(self, input_string, expected_result):
        actual_result = get_sex(input_string)

        self.assertEqual(actual_result, expected_result)

    @parameterized.expand(
        [
            ("-970",),
            ("1040",),
            ("2222",),
            ("98123",),
            ("a",),
        ]
    )
    def test_get_sex_fail(self, input_string):
        self.assertRaises(Exception, get_sex, input_string)

    @parameterized.expand(
        [
            (24, 10, 1973, "24.10.1973."),
            (5, 12, 2012, "05.12.2012."),
            (30, 3, 1990, "30.03.1990."),
            ("24", "10", "1973", "24.10.1973."),
            ("5", 12, 2012, "05.12.2012."),
            (30, "03", 1990, "30.03.1990."),
        ]
    )
    def test_get_dob_pass(self, day, month, year, expected_result):
        actual_result = get_dob(day, month, year)

        self.assertEqual(actual_result, expected_result)

    @parameterized.expand(
        [
            (
                24,
                10,
                19730,
            ),
            (
                24,
                "a",
                999,
            ),
            (
                5,
                132.4,
                "2012",
            ),
            (
                300,
                3.5,
                1990,
            ),
        ]
    )
    def test_get_dob_fail(self, day, month, year):
        self.assertRaises(Exception, get_dob, day, month, year)

    @parameterized.expand(
        [
            ("1234567890123", 226),
            ("2345678921234", 240),
            ("5298529051067", 247),
            ("6339638162178", 252),
        ]
    )
    def test_get_sum_pass(self, input_string, expected_result):
        actual_result = get_sum(input_string)

        self.assertEqual(actual_result, expected_result)

    @parameterized.expand(
        [
            (229, 2),
            (233, 9),
            (213, 7),
            (234, 8),
        ]
    )
    def test_verify_control_pass(self, sum, control):
        self.assertTrue(verify_control(sum, control))


if __name__ == "__main__":
    unittest.main()
