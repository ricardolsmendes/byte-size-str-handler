# Byte-size string handler (for Python)

[![CircleCI][1]][2]

## Handle Python strings according to their size in bytes

Encoded strings may need to fit a specific size in bytes to be accepted by some
libraries or APIs. Let's take UTF-8 chars, for instance, they may need from 1
to 4 bytes ([please refer to Wikipedia for details][3]):

- the first 128 characters (US-ASCII) need one byte;
- the next 1,920 characters need two bytes to encode, which covers the
  remainder of almost all Latin-script alphabets, and also Greek, Cyrillic,
  Coptic, Armenian, Hebrew, Arabic, Syriac, Thaana and N'Ko alphabets, as well as
  Combining Diacritical Marks;
- three bytes are needed for characters in the rest of the Basic Multilingual
  Plane, which contains virtually all characters in common use, including most
  Chinese, Japanese and Korean characters;
- four bytes are needed for characters in the other planes of Unicode, which
  include less common CJK characters, various historic scripts, mathematical
  symbols, and emoji (pictographic symbols).

## The `byte_size_string_handler` module

- `truncate_utf8()`: given a string and maximum size, the function checks
  string's UTF-8 byte-size and truncates if needed. Implementation is based on
  StackOverflow [question][4] and [answers][5].

## How to contribute

Please make sure to take a moment and read the [Code of
Conduct](https://github.com/ricardolsmendes/byte-size-string-handler/blob/master/.github/CODE_OF_CONDUCT.md).

### Report issues

Please report bugs and suggest features via the [GitHub
Issues](https://github.com/ricardolsmendes/byte-size-string-handler/issues).

Before opening an issue, search the tracker for possible duplicates. If you find a duplicate, please
add a comment saying that you encountered the problem as well.

### Contribute code

Please make sure to read the [Contributing
Guide](https://github.com/ricardolsmendes/byte-size-string-handler/blob/master/.github/CONTRIBUTING.md)
before making a pull request.

[1]: https://circleci.com/gh/ricardolsmendes/byte-size-string-handler.svg?style=svg
[2]: https://circleci.com/gh/ricardolsmendes/byte-size-string-handler
[3]: https://en.wikipedia.org/wiki/UTF-8
[4]: https://stackoverflow.com/questions/1809531/truncating-unicode-so-it-fits-a-maximum-size-when-encoded-for-wire-transfer
[5]: https://stackoverflow.com/a/1820949/7096300
