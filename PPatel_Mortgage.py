from argparse import ArgumentParser
import math
import sys


def get_min_payment(total_amount, annual_interest_rate, years, num_payments_per_year):
    """Compute the minimum mortgage payment.

    Arguments:
        total_amount (float): total amount of the mortgage
        annual_interest_rate (float): The annual interest rate 
        years (int): The term of the mortgage in years.
        num_payments_per_year (int): The number of payments per year.

    Returns:
        int: The minimum mortgage payment.

    """
    interest_rate_per_payment = annual_interest_rate / num_payments_per_year
    total_payments = years * num_payments_per_year
    payment_amount = total_amount * (interest_rate_per_payment * math.pow(1 + interest_rate_per_payment, total_payments)) / (math.pow(1 + interest_rate_per_payment, total_payments) - 1)
    return math.ceil(payment_amount)


def interest_due(balance, annual_interest_rate, num_payments_per_year):
    """Compute the amount of interest due in the next payment.

    Arguments:
        balance (float): The balance of the mortgage.
        annual_interest_rate (float): The annual interest rate
        num_payments_per_year (int): The number of payments per year.

    Returns:
        float: The amount of interest due.

    """
    interest_rate_per_payment = annual_interest_rate / num_payments_per_year
    return balance * interest_rate_per_payment


def remaining_payments(balance, annual_interest_rate, target_payment, num_payments_per_year):
    """Compute the number of payments required to pay off the mortgage.

    Args:
        balance (float): The balance of the mortgage.
        annual_interest_rate (float): The annual interest rate as a decimal.
        target_payment (float): The amount the user wants to pay per payment.
        num_payments_per_year (int): The number of payments per year.

    Returns:
        int: The number of payments required.

    """
    counter = 0
    while balance > 0:
        interest_due_amount = interest_due(balance, annual_interest_rate, num_payments_per_year)
        balance -= (target_payment - interest_due_amount)
        counter += 1
    return counter


def main(total_amount, annual_interest_rate, years=30, num_payments_per_year=12, target_payment=None):
    """Perform fixed-rate mortgage calculations.

    Args:
        total_amount (float): The total amount of the mortgage (principal).
        annual_interest_rate (float): The annual interest rate as a decimal.
        years (int, optional): The term of the mortgage in years (default: 30).
        num_payments_per_year (int, optional): The number of payments per year (default: 12).
        target_payment (float or None, optional): The amount the user wants to pay per payment (default: None).

    """
    min_payment = get_min_payment(total_amount, annual_interest_rate, years, num_payments_per_year)
    print(f"Minimum payment: {min_payment}")

    if target_payment is None:
        target_payment = min_payment

    if target_payment < min_payment:
        print("Your target payment is less than the minimum payment for this mortgage")
    else:
        total_payments = remaining_payments(total_amount, annual_interest_rate, target_payment, num_payments_per_year)
        print(f"If you make payments of ${target_payment}, you will pay off the mortgage in {total_payments} payments.")


def parse_args(arglist):
    """Parse and validate command-line arguments.

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)

    Raises:
        ValueError: encountered an invalid argument.
    """
    parser = ArgumentParser()
    parser.add_argument("total_amount", type=float, help="The total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float, help="The annual interest rate, as a decimal between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30, help="The term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_payments_per_year", type=int, default=12,
                        help="The number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float, help="The amount you want to pay per payment (default: the minimum payment)")
    args = parser.parse_args(arglist)

    if args.total_amount < 0:
        raise ValueError("Mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("Annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("Years must be positive")
    if args.num_payments_per_year < 0:
        raise ValueError("Number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("Target payment must be positive")

    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
