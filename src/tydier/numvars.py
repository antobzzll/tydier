import pandas as pd
from .strings import *
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def currency_to_float(
    target: str | list | tuple | pd.Series) -> list | tuple | pd.Series:
    """Simple method for automatically cleaning a currency variable 
    and transform it in `float`. Target variable of type `str`, `list`, `tuple`, 
    or `pandas.Series`.

    Args:
        target (str | list | tuple | pandas.Series): target variable.

    Returns:
        [str | list | tuple | set | pandas.Series]: cleaned target variable.
    """
    symbols = ['$', '€', '£', '¥', '₣', '₹', 'د.ك', 'د.إ', '﷼', '₻','₽',
               '₾', '₺', '₼', '₸', '₴', '₷', '฿', '원', '₫', '₮', '₯',
               '₱', '₳', '₵', '₲', '₪', '₰']
    
    if type(target) is str:
        target = target.replace(' ', '')
        target = target.replace(',', '.')
        return remove_chars(target, symbols)

    elif type(target) is list:
        clean_vector = []
        for i in target:
            i = i.replace(' ', '')
            i = i.replace(',', '.')
            clean_vector.append(i)
        return remove_chars(clean_vector, symbols)

    elif type(target) is tuple:
        clean_vector = []
        for i in target:
            i = i.replace(' ', '')
            i = i.replace(',', '.')
            clean_vector.append(i)
        return tuple(remove_chars(clean_vector, symbols))

    elif type(target) is pd.Series:
        target = remove_chars(target, [' '])
        target = target.str.replace(',', '.')
        return remove_chars(target, symbols)
