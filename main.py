from python_files import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Path to the genesis file to run", default="python_files/1_hello_genesis.py")

args = parser.parse_args()

def main(args):
    print("Hello from genesis-tutorial!")


if __name__ == "__main__":
    main(args)
