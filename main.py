import argparse
import numpy as np
import utils
import model


def main():
    parser = argparse.ArgumentParser(description='Script to QC PurpleAir data, pair with AirNow data, and model.')
    parser.add_argument('pa_dir', type=str, help='Directory for all the PurpleAir data. Should include sensor list.')
    parser.add_argument('an_dir', type=str, help='Directory for all the AirNow data.')
    parser.add_argument('output_dir', type=str, help='Parent directory for all outputs.')
    parser.add_argument('--p', type=float, nargs='?', const=0.61,
                        help='Percentage difference threshold. Defaults to 0.61.')
    parser.add_argument('--a', type=float, nargs='?', const=5.,
                        help='Absolute difference threshold. Defaults to 5.')
    parser.add_argument('--m25', type=float, nargs='?', const=3000,
                        help='Maximum threshold for PM2.5. Defaults to 3000.')
    parser.add_argument('--m10', type=float, nargs='?', const=np.inf,
                        help='Maximum threshold for PM2.5. Defaults to infinity.')
    parser.add_argument('--r', type=float, nargs='?', const=500,
                        help='Collocation radius. Defaults to 500m.')
    parser.parse_args()

    utils.generate_pa_hourly(parser.pa_dir, parser.output_dir, parser.p, parser.a, parser.m25, parser.m10)
    df = utils.pair_data(f"{parser.output_dir}/hourly_qa_pm25", parser.an_dir)
    m = model.LinearRegression("PM25", ['pm25_pa','humidity_a'])
    m.fit(df, parser.output_dir)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
