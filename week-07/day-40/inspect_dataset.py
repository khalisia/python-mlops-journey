from pathlib import Path
import pandas as pd

dataset_path = Path("datasets")/ "iris.csv"

if dataset_path.exists():
    df = pd.read_csv(dataset_path)

    print("\nFirst five rows:")
    print(df.head())

    print("\nDataset shape:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns.tolist())
else:
    print("Dataset not found. Run dataset_downloader.py first.")