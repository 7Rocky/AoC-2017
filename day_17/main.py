def add_number(numbers, cur, steps):
    n = len(numbers)
    pos = (cur + steps) % n

    return numbers[:pos] + [n] + numbers[pos:], pos + 1


def main():
    steps = 328
    numbers = [0]
    pos = 0

    for _ in range(2017):
        numbers, pos = add_number(numbers, pos, steps)

    print(f'Value after 2017 (1): { numbers[numbers.index(2017) + 1] }')

    for n in range(2017, 50_000_000):
        pos = (pos + steps) % (n + 1) + 1

        if pos == 1:
            number_after_0 = n + 1

    print(f'Value after 0 (2): { number_after_0 }')


if __name__ == '__main__':
    main()
