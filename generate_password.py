import argparse
import random
import secrets
import string
import subprocess


def generate_password(length):
    alphabet = string.ascii_letters + "æøåÆØÅ" + string.digits + "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Password generator')
    parser.add_argument('-n', '--number', type=int, default=1, help='Number of passwords to generate')
    parser.add_argument('-l', '--length', type=int, default=15, help='Length of the passwords')
    parser.add_argument('-c', '--clipboard', action='store_false', default=True, help='Switch to not copy first password to clipboard')
    args = parser.parse_args()

    for i in range(args.number):
        password = generate_password(args.length)
        print(password)
        if i == 0 and args.clipboard:
            subprocess.run(f'echo -n "{password}" | clip.exe', shell=True, check=True)

if __name__ == "__main__":
    main()