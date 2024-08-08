import pandas as pd


def convert_to_number(value):
    """
    Converts a population value from string format to a numeric format.

    The function handles values with 'M' for millions, 'k' for thousands,
    or plain numbers. The result is a float representing the population
    in its numeric form.

    Parameters:
    value (str): The population value as a string, potentially containing 'M' or 'k'.

    Returns:
    float: The population value as a numeric float, or None if conversion fails.
    """
    try:
        if 'M' in value:
            return float(value.replace('M', '')) * 1e6
        elif 'k' in value:
            return float(value.replace('k', '')) * 1e3
        return float(value)
    except ValueError:
        return None


def load(filename):
    """
    Loads and processes a CSV file containing population data.

    The function reads the CSV file into a DataFrame, converts population values
    to numeric format, and melts the DataFrame from wide to long format for easier
    analysis and plotting.

    Parameters:
    filename (str): The path to the CSV file containing population data.

    Returns:
    pd.DataFrame: A DataFrame with columns 'country', 'Year', and 'Population'
                  where 'Population' is in numeric format.
    """
    df = pd.read_csv(filename)
    df = df.melt(id_vars=['country'], var_name='Year', value_name='Population')
    df['Population'] = df['Population'].apply(convert_to_number)
    df['Year'] = df['Year'].astype(int)
    return df
