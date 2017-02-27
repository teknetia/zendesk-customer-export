import sys, getopt, argparse

# What arguyments do I want to get from the command line?
#    - -f Full export (ignore history)
#    - -d Delta (check existing file and fetch only new)
#    - -s [int] Start from X page
#    - -e [int] End at Y page
#    - -i [str] Input file
#    - -o [str] Output file

parser = argparse.ArgumentParser(description='Fetch customer information from Zendesk')
parser.add_argument('-f', '--full', help="Export all customer records from Zendesk")
parser.add_argument('-d', '--delta', help="Export only new customer records compared to provided input file")
parser.add_argument('-s', '--start', help="Start export from a specific Zendesk page number", type=int)
parser.add_argument('-e', '--end', help="End export at a specific Zendesk page number", type=int)
parser.add_argument('-i', '--input', help="Input file (required for -d)")
parser.add_argument('-o', '--output', help="Output file to store the customer export")
args = parser.parse_args()



print 'You have provided', len(sys.argv), 'arguments'
print 'Those argumenmts are', str(sys.argv)





# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

# args = parser.parse_args()
# print(args.accumulate(args.integers))