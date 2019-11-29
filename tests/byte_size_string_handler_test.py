import unittest

import byte_size_string_handler


class ByteSizeStringHandlerTest(unittest.TestCase):
    def test_truncate_utf8_should_truncate(self):
        """
        - Input string: 2001 'a' chars;
        - Expected field value: '1997 "a" chars + ...' since each char needs
        1 byte when encoded in UTF-8.
        """
        input_string = 'a' * 2001
        result = byte_size_string_handler.truncate_utf8(input_string, 2000)

        self.assertEqual(2000, len(result))
        self.assertEqual(f'{"a" * 1997}...', result)
        self.assertEqual(2000, len(result.encode('UTF-8')))

    def test_truncate_utf8_should_truncate_intl(self):
        """
        - Input string: 1010 'ã' chars;
        - Expected field value: '998 "ã" chars + ...' since each 'ã' char
        needs 2 bytes and dots need 1 byte when encoded in UTF-8.
        """
        input_string = 'ã' * 1010
        result = byte_size_string_handler.truncate_utf8(input_string, 2000)

        self.assertEqual(1001, len(result))
        self.assertEqual(f'{"ã" * 998}...', result)
        self.assertEqual(1999, len(result.encode('UTF-8')))

    def test_truncate_utf8_should_truncate_mixed(self):
        """
        - Input string: 1990 'a' chars + 10 'ã' chars;
        - Expected field value: '1990 "a" chars + 3 "ã" chars + ...' since
        each 'ã' char needs 2 bytes, 'a' chars and dots need 1 byte when
        encoded in UTF-8.
        """
        input_string = f'{"a" * 1990}{"ã" * 10}'
        result = byte_size_string_handler.truncate_utf8(input_string, 2000)

        self.assertEqual(1996, len(result))
        self.assertEqual(f'{"a" * 1990}{"ã" * 3}...', result)
        self.assertEqual(1999, len(result.encode('UTF-8')))
