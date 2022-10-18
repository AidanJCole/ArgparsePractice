import argparse

parser = argparse.ArgumentParser()

#strings can be bare when single or in single or double quotes when multiple words are needed.
# paramaters for add_argument:
# name, type, required.
parser.add_argument('--name', type=str, required=True)

args = parser.parse_args()

print('Hello,', args.name)