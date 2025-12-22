import pandas as pd

def load(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)

    print("Data loaded successfully with shape:", data.shape)

    return data