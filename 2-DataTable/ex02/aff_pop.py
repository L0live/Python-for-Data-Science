from matplotlib.ticker import FuncFormatter
from load_csv import load
import matplotlib.pyplot as plt

def convert_population(value):
    if isinstance(value, str):
        value = value.strip()
        if value.endswith('M'):
            return float(value[:-1]) * 1_000_000
        elif value.endswith('k'):
            return float(value[:-1]) * 1_000
    return float(value)

def main():
    data = load("population_total.csv")

    data = data.loc[:, ['country'] + [col for col in data.columns if col.isdigit() and 1800 <= int(col) <= 2050]]

    belgium_values = [convert_population(value) for value in data[data['country'] == 'Belgium'].values[0][1:]]
    france_values = [convert_population(value) for value in data[data['country'] == 'France'].values[0][1:]]

    plt.plot(data.columns[1:], belgium_values)
    plt.plot(data.columns[1:], france_values)
    plt.title("Population Projections")
    plt.legend(['Belgium', 'France'], loc='lower right')
    plt.xlabel("Year")
    plt.xticks(data.columns[1:][::40])
    plt.ylabel("Population")
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, pos: f'{int(x/1_000_000)}M'))
    plt.yticks(plt.yticks()[0][2:-2:2])
    plt.show()

if __name__ == "__main__":
    main()