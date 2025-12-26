from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Load life expectancy data and plot France's projections over time."""
    data = load("life_expectancy_years.csv")

    plt.plot(data.columns[1:], data[data['country'] == 'France'].values[0][1:])
    plt.title("France Life Expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(data.columns[1:][::40])
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
