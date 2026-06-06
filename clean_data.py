#!/usr/bin/env python3
"""Data cleaning script for 'Data Cleaning and Structural Validation' project.
This script loads sample_data.csv, performs cleaning, and writes cleaned_data.csv.
"""

# import the os module to work with file paths and check file existence
import os
# import pandas for DataFrame operations and date parsing
import pandas as pd
# import numpy to handle numeric operations and NaN values
import numpy as np


def load_csv(file_path):
    # Define a helper that reads a CSV into a pandas DataFrame and returns it
    return pd.read_csv(file_path)


def main():
    # Set the path to the input CSV file (workspace-relative file name)
    input_path = "sample_data.csv"

    # Check that the input file exists before attempting to read it
    if not os.path.exists(input_path):
        # If file is missing, print an error and exit with a non-zero code
        print(f"ERROR: input file '{input_path}' not found.")
        return

    # Load the CSV file into a DataFrame
    df_original = load_csv(input_path)

    # Print a clear header to indicate the original dataset
    print("Original dataset:")
    # Print the original DataFrame to the console (all rows, no index)
    print(df_original.to_string(index=False))

    # Make a copy of the DataFrame to perform cleaning (preserve original)
    df = df_original.copy()

    # Count how many rows are duplicates (exact duplicate rows)
    duplicates_before = df.duplicated().sum()
    # Remove duplicate rows in-place and keep the first occurrence
    df = df.drop_duplicates()

    # Convert the 'Age' column to numeric, coercing invalid/missing to NaN
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    # Convert the 'Salary' column to numeric, coercing invalid/missing to NaN
    df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

    # Record the count of missing values by column before filling
    missing_before = df.isnull().sum()

    # Compute the average (mean) age ignoring NaN values
    avg_age = df["Age"].mean()
    # If avg_age is NaN (all ages missing), set to 0 as a safe fallback
    if pd.isna(avg_age):
        avg_age = 0
    # Round average age to nearest integer for realistic age values
    avg_age_filled = int(round(avg_age))

    # Fill missing Age values with the computed rounded average age
    df["Age"] = df["Age"].fillna(avg_age_filled).astype(int)

    # Compute the average salary ignoring NaN values
    avg_salary = df["Salary"].mean()
    # If avg_salary is NaN (all salaries missing), set to 0.0 as fallback
    if pd.isna(avg_salary):
        avg_salary = 0.0
    # Round average salary to 2 decimal places to represent currency
    avg_salary_filled = round(float(avg_salary), 2)

    # Fill missing Salary values with the computed average salary
    df["Salary"] = df["Salary"].fillna(avg_salary_filled)
    # Ensure Salary column is float type and round values to 2 decimals
    df["Salary"] = df["Salary"].astype(float).round(2)

    # Parse and normalize the 'Date' column to pandas datetime objects
    # dayfirst=False treats ambiguous dates like 12/01/23 as month/day/year
    # Note: some pandas versions do not support `infer_datetime_format` in
    # `to_datetime`, so we omit that argument for compatibility.
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=False, errors="coerce")
    # Format the Date column as ISO YYYY-MM-DD strings (NaT becomes NaN)
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

    # Count how many missing values remain after filling/transformations
    missing_after = df.isnull().sum()

    # Save the cleaned DataFrame to a new CSV file without the index
    output_path = "cleaned_data.csv"
    df.to_csv(output_path, index=False)

    # Print a concise summary report showing what was done
    print("\nSummary report:")
    # Print original shape: rows and columns in the original dataset
    print(f"- Original rows: {df_original.shape[0]}, columns: {df_original.shape[1]}")
    # Print how many duplicate rows were removed
    print(f"- Duplicate rows removed: {duplicates_before}")
    # Print missing values per column before cleaning
    print(f"- Missing values before cleaning:\n  {missing_before.to_dict()}")
    # Print the values used to fill Age and Salary
    print(f"- Filled missing Age with: {avg_age_filled}")
    print(f"- Filled missing Salary with: {avg_salary_filled}")
    # Print missing values per column after cleaning
    print(f"- Missing values after cleaning:\n  {missing_after.to_dict()}")
    # Print the path where cleaned CSV was saved
    print(f"- Cleaned data saved to: {output_path}")
    # Print the first few rows of the cleaned DataFrame for quick inspection
    print("\nCleaned dataset preview:")
    print(df.to_string(index=False))


if __name__ == "__main__":
    # Run main() only when the script is executed directly
    main()
