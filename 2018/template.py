def main(part=1, data=None):
    if data is None:
        with open('data/06.txt') as f:
            lines = f.read()
    data = data.splitlines()


if __name__ == '__main__':
    print(main())

