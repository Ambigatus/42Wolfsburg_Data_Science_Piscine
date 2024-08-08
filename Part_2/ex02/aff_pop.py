import matplotlib.pyplot as plt
from load_csv import load


def filter_data(df, country1, country2):
    """
    Filters the DataFrame to include only data for the specified countries and years.

    Parameters:
    df (pd.DataFrame): The DataFrame containing population data.
    country1 (str): The name of the first country to filter.
    country2 (str): The name of the second country to filter.

    Returns:
    pd.DataFrame: A DataFrame containing only the rows for the specified countries
                  and within the year range of 1800 to 2100 respectively.
    """
    years = range(1800, 2101)
    filtered_df = df[(df['Year'].isin(years)) & ((df['country'] == country1) | (df['country'] == country2))]
    return filtered_df


def plot_data(df, country1, country2):
    """
    Plots the population data for two specified countries over time.

    The y-axis is scaled to millions of people, ranging from 0 to 100 million.

    Parameters:
    df (pd.DataFrame): The DataFrame containing population data for the selected countries.
    country1 (str): The name of the first country to plot.
    country2 (str): The name of the second country to plot.
    """
    plt.figure(figsize=(12, 6))

    for country in [country1, country2]:
        country_data = df[df['country'] == country]
        plt.plot(country_data['Year'], country_data['Population'], label=country)

    plt.xlabel('Year')
    plt.ylabel('Population (in millions)')
    plt.title(f'Population Growth: {country1} vs {country2}')

    # Set x-ticks to show every 40 years
    x_ticks = range(1800, 2101, 40)
    plt.xticks(ticks=x_ticks, labels=x_ticks, rotation=45)

    # Set y-axis limits and labels in millions
    plt.ylim(0, 100_000_000)  # Y-axis from 0 to 100 million
    y_ticks = range(0, 101_000_000, 20_000_000)  # Y-ticks every 20 million
    plt.yticks(ticks=y_ticks, labels=[f"{tick // 1_000_000}M" for tick in y_ticks])

    plt.grid(True)  # Add grid for better readability
    plt.tight_layout()  # Adjust layout to fit elements
    plt.legend()
    plt.show()


def main():
    """
    Main function to load the population data, filter it for specific countries,
    and plot the population trends.
    """
    filename = 'population_total.csv'
    df = load(filename)
    country1 = 'Germany'
    country2 = 'Ukraine'
    filtered_df = filter_data(df, country1, country2)
    plot_data(filtered_df, country1, country2)


if __name__ == "__main__":
    main()
