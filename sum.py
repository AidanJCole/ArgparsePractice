import argparse

parser = argparse.ArgumentParser()
# multiple arguments can be passed with nargs set to a value, must be exact
# an arbitrary number of 1+ arguments can be given with the string '+'
parser.add_argument('--values', '-v', type=int, nargs='+')
args = parser.parse_args()

sum= sum(args.values)
print('Sum:', sum)
