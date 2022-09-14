# import numpy as np
import pandas as pd


class CatVar:
    
    
    @staticmethod
    def remove_char(s: pd.Series):
        pass
    
    
    @staticmethod
    def str_match_ratio(str1:str, str2:str):
        """Compares two strings and returns a match ratio.

        Args:
            str1 (str): String
            str2 (str): String
            
        Returns:
            float: Match ratio
        """
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

    @staticmethod
    def find_inconsistent_categories(series: pd.Series, 
                                        categories: pd.Series):
        """Spots incorrect categories in a cat variable, by checking it
        against a correct set of pre-defined categories

        Args:
            series (pd.Series): Column of categories to check against the 
                                default ones
            categories (pd.Series): Default (permitted) categories

        Returns:
            dict: Dictionary of non-permitted categories
        """
        diff = set(series).difference(categories)
        
        return diff if diff else False
        
        
if __name__ == "__main__":
    s1 = pd.Series(['ciao', 'come', 'butta', 'male', 'malee'])
    s2 = pd.Series(['ciao', 'come', 'butta', 'male'])
    df = pd.DataFrame({'A': ['ciao', 'come', 'butta', 'male'], 'B': ['ciao', 'come', 'stai', 'bene']})
    print(CatVar.find_inconsistent_categories(s1, s2))