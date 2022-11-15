import pandas as pd
import sqlalchemy

"""
This script reads the NYC property data we've been working with and 
transforms it in various ways. This is a simple, but somewhat realistic
representation of the kinds of cleanup and transformations you might make 
in order to prepare a dataset for machine learning.

You should read through this code and determine what each of the transformations being applied are.

Confirm your understanding by running this code to produce the transformed data (as a CSV),
loading it into a dataframe, and viewing the results.
"""

def main():
    path_to_ny_sales = 'datasets/nyc-property/nyc-rolling-sales.csv'
    sales_df = pd.read_csv(path_to_ny_sales)


    # First transformation
    columns_to_drop = [
        'Unnamed: 0',
        'TAX CLASS AT PRESENT',
        'ZIP CODE',
        'BLOCK',
        'LOT',
        'EASE-MENT',
        'BUILDING CLASS AT PRESENT',
        'TAX CLASS AT TIME OF SALE',
        'BUILDING CLASS AT TIME OF SALE',
        'BUILDING CLASS CATEGORY',
        'NEIGHBORHOOD',
        'ADDRESS',
        'APARTMENT NUMBER',
        'SALE DATE'
    ]
    sales_df = sales_df.drop(columns=columns_to_drop)

    # Second transformation
    columns_to_convert = [
        'LAND SQUARE FEET',
        'GROSS SQUARE FEET',
        'SALE PRICE',
        'YEAR BUILT'
    ]
    for column_name in columns_to_convert:
        sales_df[column_name] = pd.to_numeric(sales_df[column_name], errors='coerce')
        sales_df = sales_df[sales_df[column_name].notna()]

    # Third transformation 
    # hint: look at the check_building_type function defined below
    # hint 2: read the "apply" function's documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
    sales_df['BUILDING TYPE'] = sales_df.apply(check_building_type, axis=1) 

    # Fourth transformation
    sales_df['BOROUGH'] = sales_df['BOROUGH'].map({
        1 : 'Manhattan',
        2 : 'Bronx',
        3 : 'Brooklyn',
        4 : 'Queens',
        5 : 'Staten Island',
    })


    # Fifth transformation
    # hint: read about scaling, normalization, and standardization:
    #       https://machinelearningmastery.com/how-to-improve-neural-network-stability-and-modeling-performance-with-data-scaling/ 
    columns_to_convert = [
        'LAND SQUARE FEET',
        'GROSS SQUARE FEET',
    ]
    for column_name in columns_to_convert:
        sales_df[column_name] = (sales_df[column_name] - sales_df[column_name].min()) / (sales_df[column_name].max() - sales_df[column_name].min())

    # Write the results to a csv
    sales_df.to_csv('datasets/nyc-property/transformed_nyc_housing.csv', index=False)


# It's better to define functions at the top level, rather than as
# inner functions inside main
def check_building_type(row):
    if row['COMMERCIAL UNITS'] > 0 and row['RESIDENTIAL UNITS'] > 0:
        return "MIXED USE"
    elif row['COMMERCIAL UNITS'] > 0:
        return "COMMERCIAL"
    elif row['RESIDENTIAL UNITS']:
        return "RESIDENTIAL"
    else:
        return "UNKNOWN - NO UNITS"


# This means "if the file was run as a script, run the main function"
# __name__ will be different if this file is being imported by another
# python file, for example.
if __name__ == '__main__':
    main()