import argparse
import sys

def init_common_parser(description=''):
    """Prepare a base argparse argument parser so that flags are consistent across different shell command tools.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('file', metavar="FILE", nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                        help='The CSV file to operate on. If omitted, will accept input on STDIN.')
    parser.add_argument('-d', '--delimiter', dest='delimiter', default=',',
                        help='Delimiting character of the input CSV file. Defaults to comma.')
    parser.add_argument('-t', '--tabs', dest='tabs', action='store_true',
                        help='Specifies that the input CSV file is delimited with tabs. Overrides "-d".')
    parser.add_argument('-q', '--quotechar', dest='quotechar', default='"',
                        help='Character used to quote strings in the input CSV file. Defaults to double-quote.')
    parser.add_argument('-e', '--encoding', dest='encoding', default='utf-8',
                        help='NOT YET IMPLEMENTED. Reserving flag for unicode-aware future.')

    return parser                    