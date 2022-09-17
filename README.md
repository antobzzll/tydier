# tydier

`tydier` is a Python package that facilitates data cleaning and wrangling operations on `pandas` dataframes.

## Installation

```bash
$ pip install tydier
```

## Usage

For complete usage examples please check the [example notebook](https://github.com/antobzzll/tydier/blob/dev/docs/example.ipynb).

### Automatically identify and fix incorrect categorical variable values

```python
from tydier import catvars as catvars # for methods operating on categorical variables 
import pandas as pd

dirty_cats = ['monday', 'Tusday', 'Wednesday', 'thurda', 'Firday', 'saty', 'Sunday']
clean_cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

df = pd.DataFrame({'dirty_cats': dirty_cats, 'clean_cats': clean_cats})

catvars.find_inconsistent_categories(dirty_cats, clean_cats, mapping_dict=True)
```
```
{'monday': 'Monday',
 'Firday': 'Friday',
 'thurda': 'Thursday',
 'Tusday': 'Tuesday',
 'saty': 'Saturday'}
```
Passing it to `pd.Series.replace()` to automatically replace inconsistent values with the correct predefined ones.
```python
mapping = catvars.find_inconsistent_categories(dirty_cats, clean_cats, mapping_dict=True)
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


## Contributing

Interested in contributing? Check out the [contributing guidelines](https://github.com/antobzzll/tydier/blob/dev/CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`tydier` was created by [Antonio Buzzelli](https://github.com/antobzzll). It is licensed under the terms of the MIT license.

## Credits

`tydier` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
