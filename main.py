import pandas as pd
from summarizer.summarizer import DataFrameSummarizer


def main():
    df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
                     names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"])

    summarizer = DataFrameSummarizer(df)

    # export the summary
    summarizer.export_summary(output_format="markdown", file_name="iris_summary")
    summarizer.export_summary(output_format="html", file_name="iris_summary")
    summarizer.export_summary(output_format="xlsx", file_name="iris_summary")

if __name__ == "__main__":
    main()
