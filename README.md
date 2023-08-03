# purpleair-qc

This is a package to perform quality control and bias correction on PurpleAir data using AirNow data.

## Usage

To run the program, first clone the repository to your current working directory by running

  git clone https://github.com/JeffSMLee/purpleair-qc.git

Next, set up the conda environment by running

  conda env create -f environment.yml

and activate the environment by running

  conda activate rrfs

Finally, run the main script via

  python main.py --pa_dir <PurpleAir dir> --an_dir <AirNow dir> --output_dir <output dir>

Optional flags are
- `--p` percentage difference
- `--a` absolute difference
- `--m25` maximum threshold for PM2.5
- `--m10` maximum threshold for PM10
- `--r` maximum collocation radius
- `--g` generate flag, set to 0 if should skip generating hourly PurpleAir data
