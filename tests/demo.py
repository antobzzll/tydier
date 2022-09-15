import pandas as pd
import dfcleaner

if __name__ == "__main__":

    df = pd.DataFrame({'A': ['Monday', 'Tuesday', 'Wdnesday', 'Thursday', 'Friay', 'Saturday', 'Sunday'],
                       'B': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']})
    dirty_cats = ['Monday', 'Tusday', 'Wednesday',
                  'Thursdy', 'Friday', 'Saturday', 'Sunday', 'mnday']
    clean_cats = ['Monday', 'Tuesday', 'Wednesday',
                  'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(dfcleaner.str_match_ratio("Monday", "mnday", method='commonchars'))

    print(f"\n{'*' * 5} dfcleaner.str_match_ratio: method = 'charbychar'")
    df['MatchRatio_charbychar'] = df.apply(
        lambda row: dfcleaner.str_match_ratio(row['A'], row['B'],
                                              method='charbychar'), axis=1)
    print(df)

    print(f"\n{'*' * 5} dfcleaner.str_match_ratio: method = 'sliceeach[n]'")
    df['MatchRatio_sliceeach[n]'] = df.apply(
        lambda row: dfcleaner.str_match_ratio(row['A'], row['B'],
                                              method='sliceeach2',
                                              case_sensitive=False), axis=1)
    print(df)

    print(f"\n{'*' * 5} dfcleaner.remove_chars")
    print(dfcleaner.remove_chars(df['A'], ['c', 'a']))

    print(f"\n{'*' * 5} dfcleaner.find_inconsistent_categories")
    print(dfcleaner.find_inconsistent_categories(dirty_cats, clean_cats,
                                                 mapping_dict=True))
