import matplotlib.pyplot as plt
from load_csv import load


def plot_life_expectancy(df, country):
    """
    Plot the life expectancy for a specific country.

    Parameters:
    df (pd.DataFrame): The DataFrame containing life expectancy data.
    country (str): The name of the country to plot.
    """
    if country not in df['country'].values:
        print(f"Country '{country}' not found in the dataset.")
        return

    country_data = df[df['country'] == country].iloc[:, 1:]  # Exclude the 'country' column
    plt.figure(figsize=(12, 6))
    plt.plot(country_data.columns, country_data.values.flatten(), marker='o', label=country)

    plt.title(f'Life Expectancy in {country} Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy (years)')

    # Set x-ticks to show every 40 years
    x_ticks = range(0, len(country_data.columns), 40)
    plt.xticks(ticks=x_ticks, labels=country_data.columns[x_ticks], rotation=45)

    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


def main():
    """
    Main function to load the dataset and plot life expectancy for a specific country.
    """
    dataset = load("life_expectancy_years.csv")
    if dataset is not None:
        # Specify the country you want to visualize
        country = "France"  # Change this to your desired country
        plot_life_expectancy(dataset, country)


if __name__ == "__main__":
    main()
