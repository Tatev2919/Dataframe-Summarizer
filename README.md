# Dataframe-Summarizer
Dataframe Statistics exporter program


**Overview:**

The DataFrame Summarizer is a Python tool that measures descriptions of Pandas DataFrames. It provides basic statistics summary outputs like min, max, mean, variance, etc., for each column and also allows the summary to be output in different formats including markdown, HTML and excel.

This summarizer is useful when one has a large dataset with various types of data; numerical data, date, and categorical data. When each column is summed based on the data type of columns it offers a fast and handy statistical summary of the DataFrame.

**Features:**
    Summarizes various statistics for each column of the DataFrame:
    
        - Data Type
        - It options contain Min/Max in case of numeric and datetime columns.
        - Regarding the numeric data, we need to consider the properties of Mean, Median and Mode.
        - Range and Deviation (for numeric columns)
        - Zero Percentage (for numeric columns)
        - IQR – Interquartile Range which is applicable for the numeric fields only.
        - Coefficient of variation (numeric)
        - Number of Unique Values 
        - Date Range (should be used when working with datetime fields)
    
    Export summary in multiple formats:
        - Markdown
        - HTML
        - Excel (XLSX)
    
    Handles normal edge cases such as DataFrames with no data, or columns with no data.

**Requirements:**
    Python 3.9 or higher
    Pandas
    NumPy

**Installation:**
  Clone the repository:
    git clone https://github.com/Tatev2919/Dataframe-Summarizer.git
    cd Dataframe-Summarizer
    
  Install the required dependencies:
    pip install -r requirements.txt

**Usage:**

  1. Prepare your DataFrame
  It means that the summarizer can work with any Pandas DataFrame. For illustration purposes, you can use the Iris Dataset which is available in the ‘main.py’ script as is loaded below.
  
  2. Running the Summarizer
  The summarizer can be executed by running the main.py script starting the application. This script loads the Iris dataset, generates a statistical summary, and exports it in three formats: Markdown, HTML, and Excel.
      python main.py
  
  3. Customizing Output
  You can customize the output format and file name by modifying the export_summary method in main.py:
  
    Supported formats:
    
    "markdown"
    "html"
    "xlsx"
    The files will be saved with the corresponding extensions (.md, .html, .xlsx).

**Project Structure**

    summarizer/
    ├── __init__.py             # Package initialization
    ├── summarizer.py           # Contains the DataFrameSummarizer class
    ├── utils.py                # Helper functions for type checking
    tests/                      # Unit tests for the summarizer
    main.py                     # Script to run the summarizer
    requirements.txt            # Dependencies
    README.md                   # Project documentation

**Methods in DataFrameSummarizer:**

  Internal Methods
    _get_column_type(column) – Returns the data type of the specified column.
    _get_min_value(column) – Returns the minimum value for numeric or datetime columns.
    _get_max_value(column) – Returns the maximum value for numeric or datetime columns.
    _calculate_mean(column) – Returns the mean of a numeric column.
    _calculate_median(column) – Returns the median of a numeric column.
    _calculate_mode(column) – Returns the mode of any column.
    _zero_percentage(column) – Calculates the percentage of zero values in numeric columns.
    _calculate_variance(column) – Returns the variance of a numeric column.
    _std_deviation(column) – Returns the standard deviation of a numeric column.
    _interquartile_range(column) – Returns the interquartile range for numeric columns.
    _coefficient_of_variation(column) – Returns the coefficient of variation for numeric columns.
    _distinct_value_count(column) – Returns the count of unique values in any column.
    
  Public meethods
    generate_summary() – Generates a summary of all columns in the DataFrame.
    export_summary(output_format, file_name, **kwargs) – Exports the summary in Markdown, HTML, or XLSX format.
    
**Testing:**
    Added 3 pytest cases which are not covered in scope or Iris dataset. To run the tests there is need to run only pytest command.
  
