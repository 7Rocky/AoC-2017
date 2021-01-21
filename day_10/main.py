from functools import reduce


def knot_round(numbers, start, length, skip_size):
    end = (start + length) % len(numbers)

    if length < len(numbers):
        if start <= end:
            sub_numbers = numbers[start:end]
            sub_numbers.reverse()
            numbers[start:end] = sub_numbers
        else:
            sub_numbers = numbers[start:] + numbers[:end]
            sub_numbers.reverse()
            numbers[start:] = sub_numbers[:len(numbers)-start]
            numbers[:end] = sub_numbers[len(numbers)-start:]
    else:
        sub_numbers = numbers[start:] + numbers[:start]
        sub_numbers.reverse()
        numbers[start:] = sub_numbers[:len(numbers)-start]
        numbers[:start] = sub_numbers[len(numbers)-start:]

    return numbers, (start + length + skip_size) % len(numbers)


def to_ascii(string):
    return [ord(c) for c in string]


def knot_hash(numbers):
    return reduce(lambda x, y: x ^ y, numbers, 0)


def to_hex(numbers):
    return bytearray(numbers).hex()


STANDARD_SUFFIX_VALUES = [17, 31, 73, 47, 23]


def main():
    f = open('input.txt')

    numbers = [n for n in range(256)]
    lengths_string = ''
    lengths = []

    for line in f:
        lengths_string = line.strip()
        lengths = [int(n) for n in line.split(',')]

    f.close()

    start, skip_size = 0, 0

    for length in lengths:
        numbers, start = knot_round(numbers, start, length, skip_size)
        skip_size += 1

    print(f'Result (1): { numbers[0] * numbers[1] }')

    numbers = [n for n in range(256)]
    rounds = 64
    start, skip_size = 0, 0

    lengths = to_ascii(lengths_string) + STANDARD_SUFFIX_VALUES

    for _ in range(rounds):
        for length in lengths:
            numbers, start = knot_round(numbers, start, length, skip_size)
            skip_size += 1

    xors = [knot_hash(numbers[i * 16:(i + 1) * 16]) for i in range(16)]

    print(f'Knot Hash (2): { to_hex(xors) }')


if __name__ == '__main__':
    main()
