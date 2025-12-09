from argparse import ArgumentParser
from dataclasses import dataclass


@dataclass(frozen=True)
class Args:
    key: str
    delay: int
    start: bool


def parse_args() -> Args:
    args_parser = ArgumentParser(description="utility to prevent idle by pressing a keyboard button")
    args_parser.add_argument("-k", "--key", type=str, help="key to press, default is key 'F13'", dest="key")
    args_parser.add_argument("-d", "--delay", type=int, help="delay between presses", default=60, dest="delay")
    args_parser.add_argument("-s", "--no-start", action="store_false", help="start the pressing at start-up", dest="start")

    args_parser.set_defaults(key="F13", start=True)

    try:
        args = args_parser.parse_args()
    except SystemExit as see:
        if see.code != 0:
            args_parser.print_usage()
        raise

    return Args(key=args.key, delay=args.delay, start=args.start)
