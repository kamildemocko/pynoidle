from argparse import ArgumentParser
from dataclasses import dataclass


@dataclass(frozen=True)
class Args:
    delay: int
    start: bool


def parse_args() -> Args:
    args_parser = ArgumentParser(description="utility to prevent idle by pressing F13 button")
    args_parser.add_argument("--delay", "-d", type=int, help="delay between presses", default=60, dest="delay")
    args_parser.add_argument("--no-start", "-s", action="store_false", help="start the pressing at start-up", dest="start")
    args_parser.set_defaults(start=True)
    args = args_parser.parse_args()

    return Args(delay=args.delay, start=args.start)
