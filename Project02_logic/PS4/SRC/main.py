import os
from pl_resolution import *


def main():
    for input_file in os.listdir('input'):
        input_path = os.path.join('input', input_file)

        output_path = os.path.join('output', 'output' + input_file[5:])

        knowledge_base, alpha = read_input(input_path)

        pl_resolution(knowledge_base, alpha, output_path)


if __name__ == '__main__':
    main()
