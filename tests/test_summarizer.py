import pandas as pd
from summarizer.summarizer import DataFrameSummarizer
import pytest

## Test 1: testing summary. Tested features which are not available in iris dataframe 
def test_summary():
    data = {
        'A': [1, 2, 3, 0, 5],  # numeric column
        'B': [1, 1, 1, 1, 1],  # numeric column (constant)
        'C': ['a', 'b', 'a', 'a', 'c'],  # categorical column
        'D': pd.to_datetime([
            '2020-01-01',
            '2020-01-02',
            '2020-01-03',
            '2020-01-04',
            '2020-01-05'  # datetime column
        ])
    }
    
    df = pd.DataFrame(data)
    summarizer = DataFrameSummarizer(df)
    summary = summarizer.generate_summary()

    # numeric column summaries
    assert summary.loc['A', 'Min'] == 0
    assert summary.loc['A', 'Max'] == 5
    assert summary.loc['A', 'Mean'] == pytest.approx(2.2) 
    assert summary.loc['B', 'Mean'] == 1
    assert summary.loc['B', 'Variance'] == 0  #variance should be 0 for constant values

    # categorical column summary
    assert summary.loc['C', 'Unique Values'] == 3

    # datetime column summaries
    assert summary.loc['D', 'Data Type'] == 'datetime64[ns]'
    assert summary.loc['D', 'Min'] == pd.Timestamp('2020-01-01')
    assert summary.loc['D', 'Max'] == pd.Timestamp('2020-01-05')
    
    # expected date range check
    expected_date_range = pd.Timestamp('2020-01-05') - pd.Timestamp('2020-01-01')
    assert summary.loc['D', 'Date Range'] == expected_date_range


# Test 2. Testing for invalid inputs
def test_empty_dataframe():
    df_empty = pd.DataFrame()
    with pytest.raises(ValueError, match="The DataFrame is empty."):
        summarizer = DataFrameSummarizer(df_empty)
        summarizer.generate_summary()

# Test 3. Testing for corner cases
def test_invalid_column():
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    summarizer = DataFrameSummarizer(df)

    with pytest.raises(ValueError, match="Column 'C' does not exist in the DataFrame."):
        summarizer._get_column_type('C')
