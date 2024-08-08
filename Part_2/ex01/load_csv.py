import pandas as pd


def load(path: str):
    """
    Load a CSV file and return its contents as a pandas DataFrame.

    Parameters:
    path (str): The file path to the CSV file.

    Returns:
    pd.DataFrame: The contents of the CSV file as a DataFrame.
    None: If an error occurs (e.g., file not found, bad format).
    """
    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def main():
    """
    Main function to test the load functionality and handle errors.
    """
    dataset = load("life_expectancy_years.csv")
    if dataset is not None:
        print(dataset)


if __name__ == "__main__":
    main()
