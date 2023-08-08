import argparse
from .submodule.sub import submodule1
def main(arg):
    submodule1(arg)
    print(f'Argument received: {arg}')

def cli():
    parser = argparse.ArgumentParser(description='My CLI tool')
    parser.add_argument('arg', type=str, help='An argument to print')
    args = parser.parse_args()
    main(args.arg)

if __name__ == '__main__':
    cli()
