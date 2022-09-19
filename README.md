# tydier

`tydier` is a Python package that facilitates data cleaning and wrangling operations on `pandas` dataframes.

- Project repo hosted on [GitHub](https://github.com/antobzzll/tydier).
- Last version is [`0.1.1`](https://pypi.org/project/tydier/). Please refer to [CHANGELOG.md](https://github.com/antobzzll/tydier/blob/dev/CHANGELOG.md) for details on updates.

## Installation

```bash
$ pip install tydier
```

## Usage

For complete usage examples please check the [example notebook](https://github.com/antobzzll/tydier/blob/dev/docs/example.ipynb).

### Use `tydier` to automatically **identify and fix incorrect categorical variable values**

```python
from tydier import catvars as catvars # for methods operating on categorical variables 
import pandas as pd

dirty_cats = ['monday', 'Tusday', 'Wednesday', 'thurda', 'Firday', 'saty', 'Sunday']
clean_cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

df = pd.DataFrame({'dirty_cats': dirty_cats, 'clean_cats': clean_cats})

catvars.inconsistent_categories(dirty_cats, clean_cats, mapping_dict=True)
```
```
{'monday': 'Monday',
 'Firday': 'Friday',
 'thurda': 'Thursday',
 'Tusday': 'Tuesday',
 'saty': 'Saturday'}
```
Passing it to `pd.Series.replace()` will automatically replace inconsistent values with the correct predefined ones:
```python
mapping = catvars.inconsistent_categories(dirty_cats, clean_cats, mapping_dict=True)
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
prices = pd.Series([' $50,    00', '30, 00€'])
print(numvars.currency_to_float(prices))
```
```
0    50.0
1    30.0
dtype: float64
```

## Contributing

**Found a bug?** Please report it [here](https://github.com/antobzzll/tydier/issues).

**Interested in contributing?** Check out the [contributing guidelines](https://github.com/antobzzll/tydier/blob/dev/CONTRIBUTING.md). Please note that this project is released with a [Code of Conduct](https://github.com/antobzzll/tydier/blob/dev/CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`tydier` was created by [Antonio Buzzelli](https://github.com/antobzzll). It is licensed under the terms of the MIT license.

## Credits

`tydier` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the [`py-pkgs-cookiecutter` template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
