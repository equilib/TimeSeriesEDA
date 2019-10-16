import sys
import os

sys.path.append("../")

import pandas as pd

from TimeSeriesEDA.src.BokehEDA import BokehEDAPlots
from TimeSeriesEDA.src.MatplotlibEDA import MatplotlibEDAPlots


def main():

    bk_plt = BokehEDAPlots()    # test default plot sizes for H / W

    weather_df = pd.read_csv("./test/" + "TestWeatherData.csv")

    print(weather_df.head())

    bk_plt.plot_hist(weather_df.dewPoint, bins=20, title = 'dewPoint')


if __name__ == "__main__":  main()
    