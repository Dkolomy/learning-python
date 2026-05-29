from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--output', '-o', required=True, help='output the result to a file')
parser.add_argument('--text', '-t', required=True, help='this is a text string insert into the output file')

args = parser.parse_args()

# print(args.output)
with open(args.output, 'w') as f:
  f.write(args.text+'\n')

print(f"Output written to {args.output}")