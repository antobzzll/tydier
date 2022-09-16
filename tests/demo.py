import pandas as pd
import dfcleaner


dirty_cats = ['monday', 'Tusday', 'Wednesday', 'thurda', 'Firday', 'saty', 'Sunday']

clean_cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

df = pd.DataFrame({'dirty_cats': dirty_cats, 'clean_cats': clean_cats})


# print(f"\n{'*' * 5} dfcleaner.str_match_ratio: method = 'charbychar'")
# df['MatchRatio_charbychar'] = df.apply(
#     lambda row: dfcleaner.str_match_ratio(row['A'], row['B'],
#                                             method='charbychar'), axis=1)
# print(df)




# print(f"\n{'*' * 5} dfcleaner.str_match_ratio: method = 'sliceeach[n]'")
# df['MatchRatio_sliceeach[n]'] = df.apply(
#     lambda row: dfcleaner.str_match_ratio(row['A'], row['B'],
#                                             method='sliceeach2',
#                                             case_sensitive=False), axis=1)
# print(df)




# print(f"\n{'*' * 5} dfcleaner.remove_chars")
# print(dfcleaner.remove_chars(df['A'], ['c', 'a']))




print(f"\n{'*' * 5} dfcleaner.find_inconsistent_categories")
mapping = dfcleaner.find_inconsistent_categories(dirty_cats, clean_cats,
                                                mapping_dict=True, verbose=False)
print(mapping)
df['adj_cats'] = df['dirty_cats'].replace(mapping)
print(df)