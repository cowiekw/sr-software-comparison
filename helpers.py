import openpyxl
import pandas as pd
import matplotlib.pyplot as plt

def verify_worksheet(file, sheet_name):
    workbook = openpyxl.load_workbook(file)
    try:
        worksheet = workbook[sheet_name]
    except KeyError:
        print("The sheet '{}' does not exist in your file'{}'.".format(sheet_name, file))

def replace_nulls(df):
    NaN = float("NaN")
    missingdata = ["null", "Null", "NULL", "."] # "", " ",
    for item in missingdata:
        df.replace(item, NaN, inplace=True)

    df.dropna(axis=0, how= 'all', thresh=None, subset=None, inplace=True) # Delete rows, where every value is null

def sum_features_per_software(df, min_features):
    counts = df.count(axis=1, numeric_only=True) # Count all nonmissing numeric feautures
    sums = df.sum(axis=1, skipna=True, numeric_only=True, min_count=min_features)
    df = df.assign(total_features=counts, number_of_features=sums) # Create new variables
    df = df.assign(percent_of_features=(df['number_of_features']/df['total_features']))
    df['percent_of_features'] = df['percent_of_features'].round(2) # Round percentages
    return df

def keep_top_software(df, variablename, count):
    # variablename: column to sort values by
    # count: number of software tools to keep
    df = df.sort_values(variablename, ascending=False)
    df = df.head(count).reset_index()
    del df['index']
    return df
