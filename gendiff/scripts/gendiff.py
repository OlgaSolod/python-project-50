import argparse
from gendiff.comparator import generate_diff
from gendiff.stylish import formatter


def main():
    parser = argparse.ArgumentParser(
        prog = 'gendiff',
        description = 'Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output: stylish', default='stylish.py')
    args = parser.parse_args()
    print(formatter(generate_diff(args.first_file, args.second_file)))


if __name__ == '__main__':
    main()
