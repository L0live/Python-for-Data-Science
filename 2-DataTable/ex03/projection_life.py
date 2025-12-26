from matplotlib.ticker import FuncFormatter
from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    """Analyze correlation between GDP and life expectancy in 1900.
    
    Creates a scatter plot with logarithmic scale showing the relationship
    between gross national product per capita and life expectancy.
    """
    life_expectancy = load("life_expectancy_years.csv")
    gross_national_product = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    # Select data for the year 1900
    life_expectancy_data = life_expectancy.loc[:, ["country", "1900"]]
    gross_national_product_data = gross_national_product.loc[:, ["country", "1900"]]

    data = life_expectancy_data.merge(gross_national_product_data, on="country", suffixes=('_life_expectancy', '_gdp'))
    data.columns = ["country", "life_expectancy", "gdp"]
    data = data.dropna()

    # Create scatter plot
    plt.figure(figsize=(8, 6))
    # plt.scatter(data["gdp"], data["life_expectancy"]) # matplotlib
    sns.scatterplot(data=data, x="gdp", y="life_expectancy")  # seaborn
    plt.xscale("log")
    plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1_000)}k'))
    plt.xlabel("Gross National Product per Person (log scale)")
    plt.ylabel("Life Expectancy (years)")
    plt.title("Life Expectancy vs Gross National Product per Person in 1900")
    plt.show()


if __name__ == "__main__":
    main()
