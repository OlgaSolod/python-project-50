import argparse
import json

from gendiff import generate_diff

def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    f1 = json.load(open(first_file))
    f2 = json.load(open(second_file))
    diff = generate_diff(f1, f2)
    print(diff)


if __name__ == '__main__':
    main()

    
