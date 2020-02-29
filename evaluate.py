import csv
import click
import numpy as np
import scipy.signal
from pathlib import Path


def load(fn):
    with open(fn) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            yield(int(row["xAcc_mma7455"]))


def get_peaks(x):
    _ = np.negative(x)
    _ = scipy.signal.savgol_filter(_, 51, 3)
    peaks, properties = scipy.signal.find_peaks(_, prominence=4, width=40)
    return sum(map(lambda i: i > 12, properties["prominences"]))


@click.command()
@click.option("--filename", default="", help="use newest if empty")
def main(filename):
    if not filename:
        # get newest file in folder
        filename = max((f.stat().st_mtime, f) for f in Path("logs").glob("*.csv"))[1]

    print("peaks:", get_peaks(list(load(filename))))


if __name__ == "__main__":
    main()
