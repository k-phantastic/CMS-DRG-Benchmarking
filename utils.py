import numpy as np
import pandas as pd

# From the cleaned dataframes 
CATEGORICALS = ["state", "urbanicity"]
ID_DTYPES = {"provider_ccn": str, "drg_code": str}

def load_clean(path):
    """Reload a saved table with the same dtypes it had before saving."""
    df = pd.read_csv(path, dtype=ID_DTYPES)
    return df.astype({c: "category" for c in CATEGORICALS if c in df.columns})