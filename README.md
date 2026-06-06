# Data Cleaning and Structural Validation

## Objective

This beginner-friendly project demonstrates how to perform basic data cleaning and structural validation using Python and Pandas. The script loads a small sample CSV file, identifies and fixes common data quality issues (duplicates, missing values, inconsistent date formats), and writes a cleaned CSV file.

## Problems found in `sample_data.csv`

- Duplicate rows (exact duplicates).
- Missing values in `Age` and `Salary` columns.
- Multiple date formats in the `Date` column (e.g., `12/01/23`, `2023-12-01`, `01-Dec-2023`, `2023/12/05`).

## Cleaning process (implemented in `clean_data.py`)

1. Load `sample_data.csv` into a pandas DataFrame.
2. Print the original dataset for visibility.
3. Remove exact duplicate rows, keeping the first occurrence.
4. Convert `Age` and `Salary` to numeric types (coerce invalid entries to NaN).
5. Fill missing `Age` values with the rounded mean age computed from the present values.
6. Fill missing `Salary` values with the mean salary (rounded to two decimals).
7. Parse all `Date` values with `pd.to_datetime` and normalize to `YYYY-MM-DD`.
8. Check for remaining missing values and write the cleaned dataset to `cleaned_data.csv`.
9. Print a summary report with counts and actions performed.

## Results

- A cleaned CSV `cleaned_data.csv` is produced with normalized date format and filled numeric fields.
- The script prints a summary report and a preview of the cleaned data.

## How to run

Run the script with Python 3.8+ in the project folder where the CSV files are located:

```bash
python clean_data.py
```

This will read `sample_data.csv` and write `cleaned_data.csv`.

## Notes for internship submission

- The code is written with clear, line-by-line comments explaining each step.
- It includes basic error checking for missing input files and uses pandas best-practices for parsing dates and numeric conversions.
