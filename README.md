# Byte-size string handler (for Python)

## Handle Python strings according to their size in bytes

String values may be limited by some libraries or APIs at a given char length
when encoded in UTF-8. Encoded chars may need from 1 to 4 bytes
([please refer to Wikipedia for details][1]):
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

## The `ByteSizeStringHandler` class

- `truncate_utf8()`: given a string and maximum size, this methods checks
string's UTF-8 byte-size and truncates if needed. Implementation is based on
StackOverflow [question][2] and [answers][3].

[1]: https://en.wikipedia.org/wiki/UTF-8
[2]: https://stackoverflow.com/questions/1809531/truncating-unicode-so-it-fits-a-maximum-size-when-encoded-for-wire-transfer
[3]: https://stackoverflow.com/a/1820949/7096300
