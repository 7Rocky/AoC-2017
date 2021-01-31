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


def round(lengths, numbers, start, skip_size):
    for length in lengths:
        numbers, start = knot_round(numbers, start, length, skip_size)
        skip_size += 1

    return start, skip_size


def to_ascii(string):
    return [ord(c) for c in string]


def knot_hash(numbers):
    return reduce(lambda x, y: x ^ y, numbers, 0)


def to_hex(numbers):
    return bytearray(numbers).hex()


def get_knot_hash(lengths_string):
    numbers = [n for n in range(256)]
    rounds = 64
    start, skip_size = 0, 0

    lengths = to_ascii(lengths_string) + STANDARD_SUFFIX_VALUES

    for _ in range(rounds):
        start, skip_size = round(lengths, numbers, start, skip_size)

    xors = [knot_hash(numbers[i * 16:(i + 1) * 16]) for i in range(16)]

    return to_hex(xors)


STANDARD_SUFFIX_VALUES = [17, 31, 73, 47, 23]


def main():
    f = open('input.txt')

    numbers = [n for n in range(256)]
    lengths = []

    for line in f:
        lengths_string = line.strip()
        lengths = [int(n) for n in line.split(',')]

    f.close()

    round(lengths, numbers, 0, 0)

    print(f'Result (1): { numbers[0] * numbers[1] }')

    print(f'Knot Hash (2): { get_knot_hash(lengths_string) }')


if __name__ == '__main__':
    main()
