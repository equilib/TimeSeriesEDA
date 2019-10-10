import sys

sys.path.append("../")

from TimeSeriesEDA.src.BokehEDA import BokehEDAPlots


def main():

    test_plt = BokehEDAPlots()    # test default plot sizes for H / W

    test_plt.print_status()


if __name__ == "__main__":  main()
    