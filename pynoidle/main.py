from idler import Idler


START_TIME_AFTER_SEC = 10
IN_BETWEEN_DELAY = 3


def main():
    idler = Idler(START_TIME_AFTER_SEC, IN_BETWEEN_DELAY)
    idler.wiggle()


if __name__ == "__main__":
    main()
