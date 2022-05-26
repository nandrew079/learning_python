import utils


def f_main(args):
    for param in args[1:]:
        print(*utils.currency_rates(param), sep=', ')


if __name__ == '__main__':
    import sys

exit(f_main(sys.argv))
