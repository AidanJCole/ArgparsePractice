import argparse

parser = argparse.ArgumentParser()

#strings can be bare when single or in single or double quotes when multiple words are needed.
# parameters for add_argument:
# name, type, required.
parser.add_argument('--name', type=str, required=True)
# optional arguments are as simple as omitting required=True
parser.add_argument('--age', type=int)
args = parser.parse_args()

if args.age:
    print(args.name, 'is', args.age, 'years old.')
else:
    print('Hello,', args.name)