import re
import sys


PATTERN = r'<tt><b>([a-z_]+\([a-z,_]*\))<\/b><\/tt>\s+((.|\n)+?)<br>'


def find_functions(text):
    for m in re.finditer(PATTERN, text):
        yield (m[1], re.sub('\s+', ' ', m[2].strip()))


def produce_comment(signature, description):
    return '///' + signature + '\n//' + description + '\n\n'


def process_file(fn):
    with open(fn) as f:
        for signature, description in sorted(find_functions(f.read())):
            print(produce_comment(signature, description))


if __name__ == "__main__":
    process_file(sys.argv[1])
