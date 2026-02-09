import pandas as pd
import sys
import os

def clean_data(input1, input2, output):
    print(f"Input1: {input1}")
    print(f"Input2: {input2}")
    print(f"Output: {output}")

    # Read input CSV files
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)


    # Merge the dataframes on 'respondent_id' and 'id'
    merged_df = pd.merge(df1, df2, left_on="respondent_id", right_on="id", how="inner")

    # Drop the redundant 'id' column
    merged_df = merged_df.loc[:, ~merged_df.columns.str.contains('^id$')]

    # Drop rows with missing values
    merged_df = merged_df.dropna()

    # Drop rows where 'job' contains 'insurance' or 'Insurance'
    merged_df = merged_df[~merged_df['job'].str.contains('insurance', case=False, na=False)]

    # Save the cleaned data to the specified output file
    merged_df.to_csv(output, index=False)  # Saving to CSV instead of Excel

   
if __name__ == "__main__":
    # Ensure enough arguments are passed
    if len(sys.argv) < 4:
        print("Error: Not enough arguments provided.")
        print("Usage: python clean.py <input1> <input2> <output>")
        sys.exit(1)

    # Get arguments from command line
    input1 = sys.argv[1]  # First input file
    input2 = sys.argv[2]  # Second input file
    output = sys.argv[3]  # Output file path

    print(f"Processing {input1}, {input2} and saving to {output}")
    clean_data(input1, input2, output)
