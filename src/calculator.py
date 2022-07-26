import math
import argparse

parser = argparse.ArgumentParser(description="Calculator")
parser.add_argument("--type", type=str, choices=["annuity", "diff"], help="Choose between two options ")
parser.add_argument("--principal", type=int, help="Enter loan principal here")
parser.add_argument("--payment", type=int, help="Enter your monthly payment")
parser.add_argument("--periods", type=int, help="Enter period for your credit")
parser.add_argument("--interest", type=float, help="Your interest ")
args = parser.parse_args()


def difference(principal: int, interest: float, periods: int) -> None:
    overpayment = 0
    nomynal_interest = interest / 12 / 100
    for i in range(0, periods):
        monthly_payment = principal / periods + nomynal_interest * (principal - principal * i / periods)
        print(f"Month {i + 1}: payment is {math.ceil(monthly_payment)}")
        overpayment += math.ceil(monthly_payment)
    print(f"Overpayment = {math.ceil(overpayment - principal)}")


def annuity_without_payment(principal: int, periods: int, interest: float) -> None:
    nomynal_interest = interest / 12 / 100
    monthly_payment = principal * (nomynal_interest * pow(1 + nomynal_interest, periods)) / (
            pow(1 + nomynal_interest, periods) - 1)
    monthly_payment = math.ceil(monthly_payment)
    print(f"Your monthly payment = {monthly_payment}!")
    overpayment = monthly_payment * periods - principal
    print(f"Overpayment = {math.ceil(overpayment)}")


def annuity_without_principal(payment: int, periods: int, interest: float) -> None:
    nomynal_interest = interest / 12 / 100
    loan_principal = payment / (
            nomynal_interest * pow(1 + nomynal_interest, periods) / (pow(1 + nomynal_interest, periods) - 1))
    print(f"Your loan principal = {math.floor(loan_principal)}:")
    overpayment = payment * periods - loan_principal
    print(f"Overpayment = {math.ceil(overpayment)}")


def annuity_without_periods(principal: int, payment: int, interest: float) -> None:
    nomynal_interest = interest / 12 / 100
    monthly_payment = payment
    payment = math.log(payment / (payment - nomynal_interest * principal), 1 + nomynal_interest)
    print(payment)
    years = math.floor(math.ceil(payment) / 12)
    months = math.ceil(payment) % 12
    if years == 0 and months == 1:
        print(f"It will take {months} month to repay the loan")
    elif months == 0 and years > 1:
        print(f"It will take {years} years to repay the loan")
    elif months == 0 and years == 1:
        print(f"It will take {years} year to repay the loan")
    elif years == 0 and months > 1:
        print(f"It will take {months} months to repay the loan")
    elif years == 1 and months == 1:
        print(f"It will take {years} year {months} month to repay the loan")
    elif years > 1 and months > 1:
        print(f"It will take {years} years {months} months to repay the loan")
    overpayment = math.ceil(payment) * monthly_payment - principal
    print("Overpayment = {0}".format(math.ceil(overpayment)))


def start():
    if args.type is None:
        print("Incorrect parameters")
    elif args.principal is not None and args.principal < 0:
        print("Incorrect parameters")
    elif args.interest is not None and args.interest < 0:
        print("Incorrect parameters")
    elif args.periods is not None and args.periods < 0:
        print("Incorrect parameters")
    elif args.type is not None and args.interest is None:
        print("Incorrect parameters")

    if args.type == "diff":
        if args.payment is not None:
            print("Incorrect parameters")
        elif args.periods is None:
            print("Incorrect parameters")
        elif args.interest is None:
            print("Incorrect parameters")
        else:
            difference(args.principal, args.interest, args.periods)
    elif args.type == "annuity":
        if args.payment is None:
            annuity_without_payment(args.principal, args.periods, args.interest)
        elif args.payment is not None and args.principal is None:
            annuity_without_principal(args.payment, args.periods, args.interest)
        elif args.periods is None and args.interest is not None:
            annuity_without_periods(args.principal, args.payment, args.interest)
        else:
            print("Incorrect parameters")


