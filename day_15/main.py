generator_a, generator_b = 16807, 48271
mod = 2147483647


def main():
    starting_values = []

    with open('input.txt') as f:
        for line in f:
            starting_values.append(int(line.split(' ').pop()))

    next_a, next_b = starting_values

    judge_count = 0

    for _ in range(40_000_000):
        if next_a & 0xffff == next_b & 0xffff:
            judge_count += 1

        next_a = (next_a * generator_a) % mod
        next_b = (next_b * generator_b) % mod

    print(f"First judge's final count (1): { judge_count }")

    judge_count = 0
    r = 0

    next_a, next_b = starting_values
    used_a, used_b = False, False

    while r < 5_000_000:
        while next_a & 3 or used_a:
            next_a = (next_a * generator_a) % mod
            used_a = False

        while next_b & 7 or used_b:
            next_b = (next_b * generator_b) % mod
            used_b = False

        r += 1
        used_a, used_b = True, True

        if next_a & 0xffff == next_b & 0xffff:
            judge_count += 1

    print(f"Second judge's final count (2): { judge_count }")


if __name__ == '__main__':
    main()
