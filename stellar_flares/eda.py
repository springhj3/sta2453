import pandas as pd

# Load the datasets to inspect their contents
file_paths = {
    "TIC_031381302": "031381302.csv",
    "TIC_129646813": "129646813.csv",
    "TIC_0131799991": "0131799991.csv",
}

# Load the data into dataframes and check the first few rows of each
datasets = {name: pd.read_csv(path) for name, path in file_paths.items()}
dataset_summaries = {name: df.head() for name, df in datasets.items()}
column_summaries = {name: df.columns.tolist() for name, df in datasets.items()}

print(dataset_summaries)
print(column_summaries)
