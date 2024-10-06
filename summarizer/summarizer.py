import pandas as pd
import numpy as np

class DataFrameSummarizer:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Expected a pandas DataFrame.")
        
        if df.empty:
            raise ValueError("The DataFrame is empty.")
        
        self.df = df

    def _check_column_exists(self, column):
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")

    def _check_numeric_column(self, column):
        self._check_column_exists(column)
        if not pd.api.types.is_numeric_dtype(self.df[column]):
            raise TypeError(f"Column '{column}' is not numeric.")

    def _check_non_empty_column(self, column):
        if self.df[column].empty:
            raise ValueError(f"Column '{column}' is empty.")

    def _get_column_type(self, column):
        self._check_column_exists(column)
        return self.df[column].dtype

    def _get_min_value(self, column):
        if pd.api.types.is_numeric_dtype(self.df[column]) or pd.api.types.is_datetime64_any_dtype(self.df[column]):
            return self.df[column].min()
        return None

    def _get_max_value(self, column):
        if pd.api.types.is_numeric_dtype(self.df[column]) or pd.api.types.is_datetime64_any_dtype(self.df[column]):
            return self.df[column].max()
        return None


    def _calculate_mean(self, column):
        self._check_numeric_column(column)
        self._check_non_empty_column(column)
        return self.df[column].mean()

    def _calculate_median(self, column):
        self._check_numeric_column(column)
        return self.df[column].median()

    def _calculate_mode(self, column):
        # Returns the mode of any column (numeric categorical dt)
        self._check_column_exists(column)
        self._check_non_empty_column(column)
        mode_series = self.df[column].mode()
        return mode_series[0] if not mode_series.empty else None

    def _zero_percentage(self, column):
        # Calculate percentage of zero values in numeric columns
        self._check_numeric_column(column)
        zero_count = (self.df[column] == 0).sum()
        total = len(self.df[column])
        if total == 0:
            raise ValueError(f"Column '{column}' has no rows to calculate zero percentage.")
        return (zero_count / total) * 100

    def _calculate_variance(self, column):
        self._check_numeric_column(column)
        return self.df[column].var()

    def _std_deviation(self, column):
        self._check_numeric_column(column)
        return self.df[column].std()

    def _interquartile_range(self, column):
        # Calculate IQR = Q3 - Q1
        self._check_numeric_column(column)
        Q1 = self.df[column].quantile(0.25)
        Q3 = self.df[column].quantile(0.75)
        return Q3 - Q1

    def _coefficient_of_variation(self, column):
        # calculate variation. Note: assume that there is no zero division issue
        self._check_numeric_column(column)
        mean_val = self._calculate_mean(column)
        if mean_val == 0:
            raise ZeroDivisionError(f"Cannot calculate coefficient of variation: mean of column '{column}' is 0.")
        return self._std_deviation(column) / mean_val

    def _distinct_value_count(self, column):
        # calculate unique values count per column
        self._check_column_exists(column)
        return self.df[column].nunique()

    def generate_summary(self):
        if self.df.empty:
            raise ValueError("Cannot generate summary: The DataFrame is empty.")

        # Save summary in dictionary to convert any filetype easily

        summary = {}
        for column in self.df.columns:
            col_summary = {
                "Data Type": self._get_column_type(column),
                "Min": self._get_min_value(column) if pd.api.types.is_numeric_dtype(self.df[column]) or pd.api.types.is_datetime64_any_dtype(self.df[column]) else None,
                "Max": self._get_max_value(column) if pd.api.types.is_numeric_dtype(self.df[column]) or pd.api.types.is_datetime64_any_dtype(self.df[column]) else None,
                "Mean": self._calculate_mean(column) if pd.api.types.is_numeric_dtype(self.df[column]) else None,
                "Median": self._calculate_median(column) if pd.api.types.is_numeric_dtype(self.df[column]) else None,
                "Mode": self._calculate_mode(column),
                "Zero %": self._zero_percentage(column) if pd.api.types.is_numeric_dtype(self.df[column]) else None,
                "Variance": self._calculate_variance(column) if pd.api.types.is_numeric_dtype(self.df[column]) else None,
                "Std Dev": self._std_deviation(column) if pd.api.types.is_numeric_dtype(self.df[column]) else None,
                "IQR": self._interquartile_range(column) if pd.api.types.is_numeric_dtype(self.df[column]) else None,
                "Coeff. of Variation": self._coefficient_of_variation(column) if pd.api.types.is_numeric_dtype(self.df[column]) else None,
                "Unique Values": self._distinct_value_count(column),
            }

            if pd.api.types.is_datetime64_any_dtype(self.df[column]):
                col_summary["Date Range"] = self._get_max_value(column) - self._get_min_value(column)

            summary[column] = col_summary

        return pd.DataFrame(summary).T

    def export_summary(self, output_format="markdown", file_name="summary", **kwargs):
        # Export the summary in the requested format (xslx html or md)

        supported_formats = ["markdown", "html", "xlsx"]
        if output_format not in supported_formats:
            raise ValueError(f"Unsupported format: {output_format}. Supported formats are: {', '.join(supported_formats)}")

        summary_data = self.generate_summary()

        if output_format == "markdown":
            with open(f"{file_name}.md", "w") as f:
                f.write(summary_data.to_markdown())
        elif output_format == "html":
            summary_data.to_html(f"{file_name}.html", **kwargs)
        elif output_format == "xlsx":
            summary_data.to_excel(f"{file_name}.xlsx", **kwargs)
        else:
            raise ValueError(f"Unsupported format: {output_format}")

        print(f"Summary saved as {file_name}.{output_format}")

