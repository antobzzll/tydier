import pandas as pd
from .strings import *

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
