# Changelog

## v0.1.5 (31/10/2022)

- Fixed a bug in `utilities.clean_col_names()`.
- Fixed a bug in `numvars.currency_to_float()`.

## v0.1.4 (01/10/2022)

-`utilities.clean_col_names()` now also removes puntuaction marks.

## v0.1.3 (25/09/2022)

- Added `utilities.clean_col_names()`, a method for cleaning column names in a `pandas.DataFrame`.
- Significantly improved `numvars.currency_to_float()`. Now it takes into consideration different types of currency formatting situations, and returns values separated from currency codes.

## v0.1.2 (21/09/2022)

- Optimized `strings.remove_chars()` with `map()` vectorization.
- Changed the import statement in `import tydier as ty`. Now all methods are accessible from the main module.

## v0.1.1 (19/09/2022)

- Added `numvars.currency_to_float()` method
- Minor changes and bug fixes

## v0.1.0 (15/09/2022)

- First release of `tydier`!
