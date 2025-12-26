import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file into a Pandas DataFrame.
    
    Args:
        path: Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data with shape information printed.
    """
    data = pd.read_csv(path)

    print("Data loaded successfully with shape:", data.shape)

    return data
