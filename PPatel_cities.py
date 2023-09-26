from argparse import ArgumentParser
import sys
from haversine import haversine

class Cities:
    """A class that reads geographic information about cities and finds the nearest cities to a specified location."""

    def __init__(self, filename):
        """
        Initialize the Cities object with data 

        Args:
            filename (str): The path to the file containing city data.
        """
        self.cities = {}
        with open(filename, 'r') as file:
            for line in file:
                area, city, latitude, longitude = line.strip().split(',')
                lat_lon = (float(latitude), float(longitude))
                self.cities[(area, city)] = lat_lon

    def nearest(self, point):
        """
        Find the nearest cities to a specified latitude and longitude.

        Args:
            point (tuple): A tuple consisting of a latitude and longitude expressed as floats.

        Returns:
            list: A list of the five closest cities to the specified point.
        """
        sorted_cities = sorted(self.cities.keys(), key=lambda city: haversine(point, self.cities[city]))
        return sorted_cities[:5]

def main(filename, arg1, arg2):
    """
    Read city data from a file and find the closest cities to a specified location.

    Args:
        filename (str): Path to a file containing city data.
        arg1 (str): Either the name of an area in the file or a string representation of a latitude.
        arg2 (str): Either the name of a city in the file or a string representation of a longitude.

    Side effects:
        Writes to stdout.
    """
    cities = Cities(filename)
    try:
        lat = float(arg1)
        lon = float(arg2)
        point = (lat, lon)
    except ValueError:
        try:
            point = cities.cities[arg1, arg2]
        except KeyError:
            sys.exit(f"Error: could not look up {arg1}, {arg2}")
    print(f"For {arg1}, {arg2}, the nearest cities from the file are:")
    for result in cities.nearest(point):
        print(" " + ", ".join(result))

def parse_args(arglist):
    """
    Process command-line arguments and return the parsed values as a namespace.

    Args:
        arglist (list): A list of command-line arguments.

    Returns:
        namespace: A namespace containing the parsed argument values.
    """
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing city data")
    parser.add_argument("arg1", help="a latitude expressed in decimal degrees or an area (state, country) from the file")
    parser.add_argument("arg2", help="a longitude expressed in decimal degrees or a city name from the file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.arg1, args.arg2)
