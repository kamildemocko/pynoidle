from idler import Idler
from icon import Icon


IN_BETWEEN_DELAY = 60


def main():
    idler = Idler(IN_BETWEEN_DELAY)
    icon = Icon(idler.start, idler.stop)

    print("pynoidle is running...")

    icon.run()


if __name__ == "__main__":
    main()
