# import numpy as np
import pandas as pd
import prova.strings
import catvars

def remove_chars(obj_series: pd.Series, chars: list):
    for c in chars:
        obj_series = obj_series.str.replace(c, '')
    return obj_series


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


def find_inconsistent_categories(dirty_series: pd.Series,
                                 clean_categories: pd.Series,
                                 mapping_dict: bool = False,
                                 verbose: bool = False):

    diff = list(set(dirty_series).difference(clean_categories))

    if diff:

        if mapping_dict:
            mapping = {}

            for tofix in diff:
                tofix_ls = []
                cat_ls = []
                match_ratio_charbychar_ls = []
                match_ratio_common_ls = []
                match_ratio_sliceeach_ls = []

                for cat in clean_categories:
                    tofix_ls.append(tofix)
                    cat_ls.append(cat)
                    match_ratio_charbychar_ls.append(
                        str_match_ratio(tofix, cat, case_sensitive=False,
                                        method='charbychar'))

                    match_ratio_common_ls.append(
                        str_match_ratio(tofix, cat, case_sensitive=False,
                                        method='commonchars'))

                    match_ratio_sliceeach_ls.append(
                        str_match_ratio(tofix, cat, case_sensitive=False,
                                        method='sliceeach2'))

                res = pd.DataFrame(
                    {'tofix': tofix_ls, 'cat': cat_ls,
                     'match_ratio_charbychar': match_ratio_charbychar_ls,
                     'match_ratio_common': match_ratio_common_ls,
                     'match_ratio_sliceeach': match_ratio_sliceeach_ls})

                res['match_ratio'] = res['match_ratio_charbychar'] + \
                    res['match_ratio_sliceeach'] + res['match_ratio_common']

                if verbose:
                    print("Categorical variables to fix: ")
                    print(diff)
                    print(res)

                max_ratio = res['match_ratio'].max()
                replacement = res.loc[res['match_ratio']
                                      == max_ratio]['cat'].item()

                mapping[tofix] = replacement

            return mapping  # if mapping
        else:
            return diff

    else:
        return None



