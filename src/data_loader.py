# data_loader.py
import pandas as pd

def load_natural_gas_data(file_path: str) -> pd.DataFrame:
    """
    Loads natural gas market data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The loaded data.
    """
    try:
        data = pd.read_csv(file_path, index_col=0, parse_dates=True)
        print(f"Data loaded successfully from {file_path}")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def preprocess_data(data: pd.DataFrame, variables: list) -> pd.DataFrame:
    """
    Selects and preprocesses the data (e.g., taking first differences).

    Args:
        data (pd.DataFrame): The input DataFrame.
        variables (list):  List of variables to keep.

    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """
    processed_data = data[variables].copy()
    processed_data = processed_data.dropna()

    # Example: Calculate percentage change (first difference of log)
    for var in variables:
        processed_data[var] = (processed_data[var].apply(np.log).diff()) * 100

    processed_data = processed_data.dropna()
    return processed_data
