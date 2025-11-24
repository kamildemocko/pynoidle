from idler import Idler
from icon import Icon


START_TIME_AFTER_SEC = 10
IN_BETWEEN_DELAY = 3


def main():
    idler = Idler(START_TIME_AFTER_SEC, IN_BETWEEN_DELAY)
    icon = Icon(idler.start_wiggling, idler.stop_wiggling)

    icon.run()


if __name__ == "__main__":
    main()
