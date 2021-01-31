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


def hex_to_bin(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)


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


def get_adjacent(squares, node):
    adjacent = []
    possible = [(node[0], node[1] - 1), (node[0] - 1, node[1]),
                (node[0] + 1, node[1]), (node[0], node[1] + 1)]

    for n in possible:
        if 0 <= n[0] < 128 and 0 <= n[1] < 128 and squares[n[1]][n[0]] == 1:
            adjacent.append(n)

    return adjacent


positions = {}


def group(squares, x, y, num_group):
    if squares[y][x] == 0:
        return False

    new_group = positions.get((x, y)) == None

    queue = [(x, y)]

    while len(queue):
        node = queue.pop()

        for next in get_adjacent(squares, node):
            if positions.get(next) == None:
                positions[next] = num_group
                queue.append(next)

    return new_group


def main():
    key_string = 'ffayrhll'
    rows = [hex_to_bin(get_knot_hash(f'{ key_string }-{ row }'))
            for row in range(128)]

    squares = [[int(bit) for bit in row] for row in rows]

    used_squares = reduce(lambda x, y: x + y, [sum(row) for row in squares], 0)

    print(f'Used squares (1): { used_squares }')

    num_groups = 0

    for y in range(len(squares)):
        for x in range(len(squares)):
            new_group = group(squares, x, y, num_groups)
            num_groups += 1 if new_group else 0

    print(f'Number of regions (2): { num_groups }')


if __name__ == '__main__':
    main()
