# This module is part of the `tydier` project. Please find more information
# at https://github.com/antobzzll/tydier

import pandas
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def match_ratio(str1: str, str2: str, method: str,
                case_sensitive: bool = False) -> float:
    """Function that provides different methods for comparing two given 
    strings and returns a match ratio.

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

        grouped1 = slice(str1, each)
        grouped2 = slice(str2, each)
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
        target (str | list | tuple | pandas.Series): target variable.
        chars (list): list of unwanted characters to be removed from the target
        variable.

    Returns:
        [str | list | tuple | set | pandas.Series]: cleaned target variable.
    """

    def _iter_remove(substring, chars=chars):
        for c in chars:
            substring = substring.replace(c, '')
        return substring

    if type(target) is str:
        for c in chars:
            target = target.replace(c, '')
        return target

    elif type(target) is list:
        return list(map(_iter_remove, target))

    elif type(target) is tuple:
        return tuple(map(_iter_remove, target))

    elif type(target) is pandas.Series:
        for c in chars:
            target = target.str.replace(c, '')
        return target

    else:
        raise ValueError("`target` must be of type "
                         "str | list | tuple | pandas.Series")


def slice(target: str, chunk_size: int) -> list:  # used for match_ratio sliceeach
    """Returns a `target` string subdivided in chunks (in `list` type), 
    according to `chunk_size` variable.

    Args:
        target (str): target string to be subdivided in chunks.
        chunk_size (int): chunk size (in number of characters).

    Raises:
        ValueError: if `chunk_size` > lenght of target string
        ValueError: if `chunk_size` < 2

    Returns:
        list: list of chunks (target string subdivided)
    """
    length = len(target)
    positions = length - 1

    if chunk_size > length:
        raise ValueError(f"Invalid `chunk_size` int. Maximum allowed size"
                         f"for provided target string is {length}")
    if chunk_size < 2:
        raise ValueError(f"Invalid `chunk_size` int. Min allowed is 2")

    start = 0
    end = chunk_size
    chunks = list()
    for _ in range(positions):
        chunk = target[start:end]
        if len(chunk) == chunk_size:
            chunks.append(chunk)
            start += 1
            end += 1

    return chunks
