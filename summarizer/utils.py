import pandas as pd

# Check column type 

def is_numeric_column(df, column):
    return pd.api.types.is_numeric_dtype(df[column])

def is_datetime_column(df, column):
    return pd.api.types.is_datetime64_any_dtype(df[column])
