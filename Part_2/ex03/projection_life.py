import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Main function to load data, filter for the year 1900, merge datasets, and plot life expectancy
    against GDP per capita for each country.

    The function loads the income and life expectancy datasets, extracts data for the year 1900,
    merges the datasets on the country name, and then creates a scatter plot to visualize the
    relationship between GDP per capita and life expectancy.
    """
    # Load the datasets
    income_df = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    life_expectancy_df = load('life_expectancy_years.csv')

    # Filter for the year 1900
    income_1900 = filter_year(income_df, '1900', 'GDP per Capita (1900)')
    life_expectancy_1900 = filter_year(life_expectancy_df, '1900', 'Life Expectancy (1900)')

    # Merge the datasets on 'country'
    merged_df = merge_datasets(income_1900, life_expectancy_1900)

    # Plot the data
    plot_data(merged_df)


def filter_year(df, year, new_column_name):
    """
    Filters a DataFrame to include only data for the specified year.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    year (str): The year for which data should be filtered.
    new_column_name (str): The name to assign to the filtered column in the resulting DataFrame.

    Returns:
    pd.DataFrame: A DataFrame containing the country and the data for the specified year.
    """
    filtered_df = df[['country', year]].dropna().rename(columns={year: new_column_name})
    return filtered_df


def merge_datasets(df1, df2):
    """
    Merges two DataFrames on the 'country' column.

    Parameters:
    df1 (pd.DataFrame): The first DataFrame to merge.
    df2 (pd.DataFrame): The second DataFrame to merge.

    Returns:
    pd.DataFrame: The merged DataFrame containing data from both input DataFrames.
    """
    merged_df = pd.merge(df1, df2, on='country')
    return merged_df


def plot_data(df):
    """
    Creates a scatter plot of GDP per capita versus life expectancy.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data to plot, with columns for GDP per capita and life expectancy.

    Returns:
    None
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(df['GDP per Capita (1900)'], df['Life Expectancy (1900)'])

    # Add titles and labels
    plt.title('Life Expectancy vs GDP per Capita in 1900')
    plt.xlabel('GDP per Capita (PPP, Inflation Adjusted)')
    plt.ylabel('Life Expectancy (Years)')
    plt.grid(True)

    # Show plot
    plt.show()


if __name__ == "__main__":
    main()
