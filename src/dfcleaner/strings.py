import pandas


def match_ratio(str1: str, str2: str, method: str,
                    case_sensitive: bool = False) -> float:
    """Function that provides different methods for comparing two given 
    strings and return a match ratio.
    
    Args:
        str1 (str): string to be compared.
        str2 (str): string to be compared.
        method (str): options:
                            'charbychar': compares strings character by
                            character.
                            'sliceeach[n]': compares strings by dividing them 
                            into chunks [n].
                            'commonchars': compares strings by counting common
                            characters.
    Raises:
        ValueError: if invalid `method`.
        ValueError: if invalid `each` argument.

    Returns:
        [float]: match ratio.
    """
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
        len1 = len(str1)
        len2 = len(str2)
        max_len = len1 if len1 > len2 else len2
        
        s1 = set(str1)
        s2 = set(str2)
        common_chars = s1 & s2

        return len(common_chars) / max_len

    elif 'sliceeach' in method:
        try:
            each = int(method[-1])
        except ValueError:
            raise ValueError("Invalid `each` argument.")

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


def remove_chars(
        target: str | list | tuple | pandas.Series,
        chars: list | tuple | str) -> list | tuple | pandas.Series:
    """Simple method for cleaning recurrent unwanted characters or substrings
    from a target variable of type `str`, `list`, `tuple`, or `pandas.Series`.

    Args:
        target_vector (str | list | tuple | pandas.Series): target variable.
        chars (list): list of unwanted characters to be removed from the target
        variable.

    Returns:
        [str | list | tuple | set | pandas.Series]: cleaned target variable.
    """

    if type(target) is str:
        for c in chars:
            target = target.replace(c, '')
        return target

    elif type(target) is list:
        clean_vector = []
        for i in target:
            for c in chars:
                i = i.replace(c, '')
            clean_vector.append(i)
        return clean_vector

    elif type(target) is tuple:
        clean_vector = []
        for i in target:
            for c in chars:
                i = i.replace(c, '')
            clean_vector.append(i)
        return tuple(clean_vector)

    elif type(target) is pandas.Series:
        for c in chars:
            clean_vector = target.str.replace(c, '')
        return clean_vector

    else:
        raise ValueError("`target` must be of type "
                         "str | list | tuple | pandas.Series")


def _rec_slice_str(string: str, each: int) -> list:  # used for str_match_ratio sliceeach
    length = len(string)
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
        chunk = string[start:end]
        if len(chunk) == each:
            res.append(chunk)
            start += 1
            end += 1

    return res
