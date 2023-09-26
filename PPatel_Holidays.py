import argparse
import requests
import sys

def get_holidays(country_code, year):
    url = f"https://date.nager.at/Api/v1/Get/{country_code}/{year}"
    response = requests.get(url)
    holidays = response.json()
    
    for holiday in holidays:
        date = holiday["date"]
        name = holiday["name"]
        print(f"{date}: {name}")

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("country_code", help="Two-letter country code")
    parser.add_argument("year", help="Four-digit year")
    return parser.parse_args(args)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    get_holidays(args.country_code, args.year)
