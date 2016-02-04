# encoding: utf8

from os.path import dirname, join
import unittest

from pyshgck.bin import read_cstring, read_struct, pad_data


FILES_DIR = join(dirname(__file__), "files")

CSTRING_FILE_PATH = join(FILES_DIR, "utf8.bin")
ASCII_CONTENT = "test string".encode("utf8")

UTF16LE_FILE_PATH = join(FILES_DIR, "utf16le.bin")
UTF16LE_CONTENT = "ソウルシリーズ".encode("utf16")

UTF16_FILE_PATH = os.path.join(FILES_DIR, "utf16_and_garbage.bin")
UTF16_CONTENT = "ソウルシリーズ".encode("utf16")

FOUR_BYTES = b"aaaa"


class BinTests(unittest.TestCase):

    def test_read_cstring(self):
        with open(CSTRING_FILE_PATH, "rb") as ascii_file:
            utf8_string = read_cstring(ascii_file)
            self.assertEquals(utf8_string, ASCII_CONTENT)

        with open(UTF16LE_FILE_PATH, "rb") as utf16_file:
            utf16_string = read_cstring(utf16_file)
            self.assertEquals(utf16_string, UTF16LE_CONTENT)

            utf16_file.seek(25)
            utf16_string = read_cstring(utf16_file)
            self.assertEquals(utf16_string, UTF16LE_CONTENT)

    def test_pad_data(self):
        padded_to_16 = pad_data(FOUR_BYTES, 16)
        padded_to_16_expected = FOUR_BYTES + (12 * b"\x00")
        self.assertEquals(padded_to_16, padded_to_16_expected)

        padded_to_16_plus_8 = pad_data(FOUR_BYTES, 16, start_at = 8)
        padded_to_16_plus_8_expected = FOUR_BYTES + (4 * b"\x00")
        self.assertEquals(padded_to_16_plus_8, padded_to_16_plus_8_expected)


if __name__ == '__main__':
    unittest.main()
