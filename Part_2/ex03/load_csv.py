import pandas as pd


def convert_to_number(value):
    """
    Convert a string value with 'M' or 'k' to a float value.
    """
    try:
        if 'M' in value:
            return float(value.replace('M', '')) * 1e6
        elif 'k' in value:
            return float(value.replace('k', '')) * 1e3
        return float(value)
    except ValueError:
        return None


def load(file_path):
    df = pd.read_csv(file_path)
    return df
