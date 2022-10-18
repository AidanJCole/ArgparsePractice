import argparse


parser = argparse.ArgumentParser()
# x and y are positional arguments
# positional arguments can't be referenced with the '--' prefix
parser.add_argument('x', type=int, help='The first value to multiply')
parser.add_argument('y', type=int, help='The second value to multiply')
args = parser.parse_args()

product = args.x * args.y
print('Product:', product)