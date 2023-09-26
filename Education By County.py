import argparse
import pandas as pd
import sys

def most_educated(csv, state):
    """Find the county in a given state with the highest education level per capita."""
    data = pd.read_csv(csv)
    state_data = data[data['State'] == state]
    max_percent = state_data['Percent of adults with a bachelor’s degree or higher'].max()
    highest_county = state_data[state_data['Percent of adults with a bachelor’s degree or higher'] == max_percent]
    county_name = highest_county.iloc[0]['Area name']
    return county_name, max_percent

def parse_args(arglist):
    """Parse command-line arguments and return the parsed values as a namespace."""
    parser = argparse.ArgumentParser()
    parser.add_argument("csv", help="path to the CSV file")
    parser.add_argument("state", help="two-letter state code")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    county, percent = most_educated(args.csv, args.state)
    print(f"{percent}% of adults in {county} have at least a bachelor’s degree")
