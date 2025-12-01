from icon import Icon
from idler import Idler
from arguments import parse_args


def main():
    args = parse_args()
    idler = Idler(args.delay)
    icon = Icon(idler.start, idler.stop)

    print("pynoidle is running...")

    icon.run(start=args.start)

    print("pynoidle is exitting...")


if __name__ == "__main__":
    main()
