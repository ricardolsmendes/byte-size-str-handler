def truncate_utf8(string, max_size):
    """
    Given a string and maximum size, this function checks string's UTF-8
    byte-size and truncates if needed. When it happens, ellipses are appended
    to the result string so users will know it's different from the original
    value.
    """
    assert string

    encoding = 'UTF-8'
    encoded = string.encode(encoding)
    decoded = f'{encoded[:max_size - 3].decode(encoding, "ignore")}...' \
        if len(encoded) > max_size \
        else encoded.decode(encoding, 'ignore')

    return decoded
