# tydier

`tydier` is a Python package that facilitates data cleaning and wrangling operations on `pandas` dataframes.

- Project repo hosted on [GitHub](https://github.com/antobzzll/tydier).
- Last version is [`0.1.3`](https://pypi.org/project/tydier/). Please refer to [CHANGELOG.md](https://github.com/antobzzll/tydier/blob/dev/CHANGELOG.md) for details on updates.

## Installation

```bash
$ pip install tydier
```

## Why use `tydier`?



### Use `tydier` to automatically **identify and fix incorrect categorical variable values**

```python
import tydier as ty
import pandas as pd

dirty_cats = ['monday', 'Tusday', 'Wednesday', 'thurda', 'Firday', 'saty', 'Sunday']
clean_cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

df = pd.DataFrame({'dirty_cats': dirty_cats, 'clean_cats': clean_cats})

ty.inconsistent_categories(dirty_cats, clean_cats)
```
```
['Firday', 'Tusday', 'thurda', 'saty', 'monday']
```
Setting `mapping_dict` to `True`, will return a dictionary which we can pass to `pandas.Series.replace()` to automatically replace inconsistent categorical values in a `pandas.Series`:
```python
mapping = ty.inconsistent_categories(dirty_cats, clean_cats, mapping_dict=True)
df['cleaned_dirty_cats'] = df['dirty_cats'].replace(mapping)
df
```
|dirty_cats	| clean_cats | cleaned_dirty_cats|
| --- | ---| --- |
| monday | Monday | Monday|
| Tusday | Tuesday | Tuesday|
| Wednesday | Wednesday | Wednesday|
| thurda | Thursday | Thursday|
| Firday | Friday | Friday|
| saty | Saturday | Saturday|
| Sunday | Sunday | Sunday|

### Use `tydier` to automatically transform into `float` a **currency `string` variable**, containing symbols and inconsistent spaces
```python
prices = ["  23,000.12 $", "123,000.56USD", "$45", "$ 56,90"]

v, c = ty.currency_to_float(prices)
print("Values:")
print(v)
print("Currencies:")
print(c)
```
```
Values:
[23000.12, 123000.56, 45.0, 56.9]
Currencies:
['$', 'USD', '$', '$']
```

### Use `tydier` to automatically **clean column names**
```python
df.columns = ['    Dirty  categorieS', 'Clean Categories']
df.columns = ty.clean_col_names(df.columns)
print(df.columns)
```
```
Index(['dirty_categories', 'clean_categories'], dtype='object')
```
For complete usage examples please check the [example notebook](https://github.com/antobzzll/tydier/blob/dev/docs/example.ipynb).

## Contributing

**Found a bug?** Please report it [here](https://github.com/antobzzll/tydier/issues).

**Have an idea and want to make a suggestion?** Feel free to update the [TODO list](https://github.com/antobzzll/tydier/blob/dev/TODO.md).

**Interested in contributing?** Check out what's on the [TODO list](https://github.com/antobzzll/tydier/blob/dev/TODO.md) and the [contributing guidelines](https://github.com/antobzzll/tydier/blob/dev/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/antobzzll/tydier/blob/dev/CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`tydier` was created by [Antonio Buzzelli](https://github.com/antobzzll). It is licensed under the terms of the MIT license.

## Credits

`tydier` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the [`py-pkgs-cookiecutter` template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
