from argparse import ArgumentParser
import sqlite3
import sys


class EnergyDB:
    """Build a database of energy sources in the US."""

    def __init__(self, filename):
        """Initialize the EnergyDB object and create the database."""
        self.conn = sqlite3.connect(":memory:")
        self.read(filename)

    def __del__(self):
        """Clean up the database connection."""
        try:
            self.conn.close()
        except:
            pass

    def read(self, filename):
        """Read data from the CSV file and insert it into the database."""
        self.conn.execute(
            "CREATE TABLE production (year INTEGER, state TEXT, source TEXT, mwh REAL)"
        )
        with open(filename, "r") as file:
            next(file)  # Skip the header line
            for line in file:
                year, state, source, mwh = line.strip().split(",")
                self.conn.execute(
                    "INSERT INTO production VALUES (?,?,?,?)",
                    (int(year), state, source, float(mwh)),
                )
        self.conn.commit()

    def production_by_source(self, source, year):
        """Calculate the total production of a specific energy source in a given year."""
        cursor = self.conn.execute(
            "SELECT SUM(mwh) FROM production WHERE source=? AND year=?",
            (source, year),
        )
        total_production = cursor.fetchone()[0]
        return total_production


def main(filename):
    """Build a database of energy sources and calculate the total production
    of solar and wind energy.
    """
    e = EnergyDB(filename)
    sources = [("solar", "Solar Thermal and Photovoltaic"), ("wind", "Wind")]
    for source_lbl, source_str in sources:
        total_production = e.production_by_source(source_str, 2017)
        print(f"Total {source_lbl} production in 2017: {total_production}")


def parse_args(arglist):
    """Parse command-line arguments."""
    parser = ArgumentParser()
    parser.add_argument("file", help="path to energy CSV file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
