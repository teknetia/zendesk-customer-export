import argparse

parser = argparse.ArgumentParser(description='Fetch customer information \
                                 from Zendesk')
parser.add_argument('-d', '--delta', action='store_true',
                    help="Export only new customer records")
parser.add_argument('-s', '--start', type=int, metavar="int",
                    help="Start export from a specific Zendesk page number")
parser.add_argument('-e', '--end', type=int, metavar="int",
                    help="End export at a specific Zendesk page number")
parser.add_argument('-i', '--input', metavar="str",
                    help="Input file (required for -d)")
parser.add_argument('-o', '--output', metavar="str", default="output.csv",
                    help="Output file to store the customer export")
args = parser.parse_args()

print(args)
