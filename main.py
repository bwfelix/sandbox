import sys

def _main(name):
    print("Hello", name)


if __name__ == '__main__':
    _main(NAME)

_main(sys.ARGV[1])
