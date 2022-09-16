# import numpy as np
import pandas as pd


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


def remove_chars(obj_series: pd.Series, chars: list):
    """Removes a list of chars from a pandas object series.

    Args:
        obj_series (pd.Series): Target pd.Series
        chars (list): Chars to be removed

    Returns:
        pd.Series: Cleaned object series
    """
    for c in chars:
        obj_series = obj_series.str.replace(c, '')
    return obj_series


def find_inconsistent_categories(series: pd.Series,
                                 categories: pd.Series,
                                 mapping_dict: bool = False):
    """Spots incorrect categories in a categorical variable, by checking it
    against a correct set of pre-defined categories.

    Args:
        series (pd.Series): Column of categories to check against the 
                            default ones.
        categories (pd.Series): Default (permitted) categories.
        print_mapping_dict (bool): Prepares and prints a mapping dictionary 
                            string to use with pd.Series.str.replace(mapping). 

    Returns:
        dict: Set of non-permitted categories
    """
    diff = list(set(series).difference(categories))

    if mapping_dict:

        mapping = {}

        for tofix in diff:
            tofix_ls = []
            cat_ls = []
            match_ratio_ls = []

            for cat in categories:
                tofix_ls.append(tofix)
                cat_ls.append(cat)
                match_ratio_ls.append(str_match_ratio(tofix, cat,
                                                      case_sensitive=False,
                                                      method='sliceeach2'))

            res = pd.DataFrame({'tofix': tofix_ls, 'cat': cat_ls,
                                'match_ratio': match_ratio_ls})

            max_ratio = res['match_ratio'].max()

            try:
                replacement = res.loc[res['match_ratio']
                                      == max_ratio]['cat'].item()
            except ValueError:  # if replacements are more than 1 ... use 'commonchars'
                pot_replacements = res.loc[res['match_ratio']
                                           == max_ratio]['cat'].to_list()

                tofix_ls = []
                cat_ls = []
                match_ratio_ls = []

                for rep in pot_replacements:
                    tofix_ls.append(tofix)
                    cat_ls.append(rep)
                    match_ratio_ls.append(str_match_ratio(
                        rep, tofix, method='commonchars'))

                res = pd.DataFrame({'tofix': tofix_ls, 'cat': cat_ls,
                                    'match_ratio': match_ratio_ls})

                max_ratio = res['match_ratio'].max()

                replacement = res.loc[res['match_ratio']
                                      == max_ratio]['cat'].item()

            mapping[tofix] = replacement

        return mapping

    else:
        return diff if diff else False


def _rec_slice_str(str1, each):

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
