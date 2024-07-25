import argparse
import secrets
import string
import subprocess
import sys


def generate_password(length, fraction_symbols=0.15, fraction_digits=0.25):
    alphabet = string.ascii_letters
    digits = string.digits
    symbols = r"!?_-.,:$@%&*[]"

    digits_fraction1 = fraction_digits / 3
    digits_fraction2 = fraction_digits - digits_fraction1

    num_digits1 = int(round(length * digits_fraction1, 0))
    num_digits2 = int(round(length * digits_fraction2, 0))

    symbols_fraction1 = fraction_symbols / 3
    symbols_fraction2 = fraction_symbols - symbols_fraction1

    num_symbols1 = int(round(length * symbols_fraction1, 0))
    num_symbols2 = int(round(length * symbols_fraction2, 0))

    letters1 = "".join(secrets.choice(alphabet) for i in range(int(length / 2)))
    letters_leftover = length - num_digits1 - num_digits2 - num_symbols1 - num_symbols2 - len(letters1)
    letters2 = "".join(secrets.choice(alphabet) for i in range(int(letters_leftover)))

    digits1 = "".join(secrets.choice(digits) for i in range(num_symbols1))
    digits2 = "".join(secrets.choice(digits) for i in range(num_symbols2))

    symbols1 = "".join(secrets.choice(symbols) for i in range(num_digits1))
    symbols2 = "".join(secrets.choice(symbols) for i in range(num_digits2))

    return letters1 + digits1 + symbols1 + letters2 + digits2 + symbols2


def main():
    parser = argparse.ArgumentParser(description="Password generator")
    parser.add_argument("-n", "--number", type=int, default=1, help="Number of passwords to generate")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password(s)")

    args = parser.parse_args()

    for i in range(args.number):
        password = generate_password(args.length)
        print(password)  


if __name__ == "__main__":
    main()
