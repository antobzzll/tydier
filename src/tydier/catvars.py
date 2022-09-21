# This module is part of the `tydier` project. Please find more information
# at https://github.com/antobzzll/tydier

from .strings import *
from .utilities import *
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def categorical_variables(dataframe: pd.DataFrame,
                          display: bool = False) -> dict:
    """Retrieves a `pandas.DataFrame`'s categorical variables 
    and their unique values.

    Args:
        dataframe (pd.DataFrame): target `pandas.DataFrame`.
        display (bool, optional): if set to `True` prints out dataframe's 
        categorical variables and their unique values. Defaults to `False`.

    Returns:
        dict: dictionary of categorical variables and their unique values
        (only if `display` is set to `False`).
    """
    cat_vars = {k: dataframe[k].unique()
                for k in dataframe.columns
                if dataframe[k].dtype in ["object", "category"]}

    if display:
        n = 0
        for k, v in cat_vars.items():
            n += 1
            print(f"({n}) {k} | {len(v)} unique values:\n{v}\n")
    else:
        return cat_vars


def inconsistent_categories(dirty_series: list | pd.Series,
                            clean_categories: list | pd.Series,
                            mapping_dict: bool = False,
                            verbose: bool = False) -> list | dict | None:
    """Find inconsistent categorical values in a `pd.Series` by checking it 
    against a correct list of permitted parameters.

    Args:
        dirty_series (list | pd.Series): categorical variable column to check
        against `clean_categories`.
        clean_categories (list | pd.Series): set of clean and permitted options
        for the categorical variable.
        mapping_dict (bool, optional): dictionary of possible replacements for 
        incorrect values found.
        verbose (bool, optional): prints out analysis and selection process of
        replacement candidates for incorrent category values. 

    Returns:
        list | dict | None: `list` of different categories, or `dict` of
        mapping of possible replacements. `None` if there are no differences.
    """
    diff = list(set(dirty_series).difference(clean_categories))

    if verbose:
        print("Categorical variables to fix: ")
        print(diff)

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
                        match_ratio(tofix, cat, case_sensitive=False,
                                    method='charbychar'))

                    match_ratio_common_ls.append(
                        match_ratio(tofix, cat, case_sensitive=False,
                                    method='commonchars'))

                    match_ratio_sliceeach_ls.append(
                        match_ratio(tofix, cat, case_sensitive=False,
                                    method='sliceeach2'))

                res = pd.DataFrame(
                    {'tofix': tofix_ls, 'cat': cat_ls,
                     'match_ratio_charbychar': match_ratio_charbychar_ls,
                     'match_ratio_common': match_ratio_common_ls,
                     'match_ratio_sliceeach': match_ratio_sliceeach_ls})

                res['match_ratio'] = res['match_ratio_charbychar'] + \
                    res['match_ratio_sliceeach'] + res['match_ratio_common']

                if verbose:
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
