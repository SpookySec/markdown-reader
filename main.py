from rich.markdown import Markdown
from rich import print

# parse arguemnts
import argparse
parser = argparse.ArgumentParser(description='Render markdown in the terminal with the python Rich library.')
parser.add_argument('-f', '--file', help='The file to render.', required=True)
args = parser.parse_args()

with open(args.file) as f:
    print(Markdown(f.read()))