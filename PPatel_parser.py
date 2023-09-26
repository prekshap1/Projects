import re
from argparse import ArgumentParser

def parse_address(address_line):
    """
    Parse a single line of text representing an address and return a dictionary of address components.
    
    Args:
        address_line (str): A line of text representing an address.
        
    Returns:
        dict: A dictionary containing the components of the address, including house number, street,
              city, state, and zip code. Keys are "house_number", "street", "city", "state", and "zip".
              If the address cannot be parsed, None is returned.
    """
    pattern = r'^(?P<house_number>.*?),\s*(?P<street>.*?)\s*,\s*(?P<city>.*?)\s*(?P<state>[A-Z]{2})\s*(?P<zip>\d{5})$'
    match = re.search(pattern, address_line)
    
    if match:
        return match.groupdict()
    else:
        return None

def parse_addresses(file_path):
    """
    Parse a file containing addresses and return a list of dictionaries representing each address.
    
    Args:
        file_path (str): The path to the file containing addresses.
        
    Returns:
        list: A list of dictionaries, where each dictionary represents an address with its components.
              If the file cannot be opened or the addresses cannot be parsed, an empty list is returned.
    """
    addresses = []
    
    try:
        with open(file_path, 'r') as address_file:
            for line in address_file:
                address = parse_address(line.strip())
                if address:
                    addresses.append(address)
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    
    return addresses

def parse_args(arglist):
    """
    Parse command-line arguments.
    
    Args:
        arglist (list): A list of command-line arguments.
        
    Returns:
        argparse.Namespace: An object containing the parsed command-line arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("file_path", help="file containing one address per line")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in parse_addresses(args.file_path):
        print(address)
