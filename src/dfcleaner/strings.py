def str_match_ratio(str1: str, str2: str, method: str,
                    case_sensitive: bool = False):

    if not case_sensitive:
        str1 = str1.lower()
        str2 = str2.lower()

    if method == 'charbychar':
        len1 = len(str1)
        len2 = len(str2)
        max_len = len1 if len1 > len2 else len2

        if len1 < max_len:
            str1 = str1 + "*" * (max_len - len1)
        if len2 < max_len:
            str2 = str2 + "*" * (max_len - len2)

        same_chars = 0
        for x, y in zip(str1, str2):
            if x == y:
                same_chars += 1

        return same_chars / max_len

    elif method == 'commonchars':
        s1 = set(str1)
        s2 = set(str2)
        common_chars = s1 & s2

        return len(common_chars)

    elif 'sliceeach' in method:
        try:
            each = int(method[-1])
        except ValueError:
            raise ValueError("Invalid method.")

        grouped1 = _rec_slice_str(str1, each)
        grouped2 = _rec_slice_str(str2, each)
        longest = grouped1 if grouped1 > grouped2 else grouped2

        matching_chunks = []
        for chunk in grouped2:
            if chunk in grouped1:
                matching_chunks.append(chunk)

        return len(matching_chunks) / len(longest)

    else:
        raise ValueError("Invalid method.")


def remove_chars(obj_series, chars: list):
    for c in chars:
        obj_series = obj_series.str.replace(c, '')
    return obj_series


def _rec_slice_str(str1, each):  # used for str_match_ratio sliceeach
    length = len(str1)
    positions = length - 1

    if each > length:
        raise ValueError(f"Invalid each number. Max allowed for provided "
                         f"string is {length}")
    if each < 2:
        raise ValueError(f"Invalid each number. Min allowed is 2")

    start = 0
    end = each
    res = list()
    for _ in range(positions):
        chunk = str1[start:end]
        if len(chunk) == each:
            res.append(chunk)
            start += 1
            end += 1

    return res
