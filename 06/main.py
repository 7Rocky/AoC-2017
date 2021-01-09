def debug_banks(banks):
    steps = 0
    debugged = []

    while debugged.count(banks) < 2:
        steps += 1
        blocks = max(banks)
        cand_index = banks.index(blocks)
        banks[cand_index] = 0

        while blocks != 0:
            cand_index += 1
            blocks -= 1
            banks[cand_index % len(banks)] += 1

        debugged.append(banks.copy())

    cycles = steps - (debugged.index(banks) + 1)

    return steps, cycles


def main():
    f = open('input.txt')

    banks = []

    for line in f:
        banks = line.strip().split('\t')

    banks = [int(b) for b in banks]

    f.close()

    count, cycles = debug_banks(banks.copy())

    print(f'Redistribution cycles (1): { count }')
    print(f'Cycles of the infinite loop (2): { cycles }')


if __name__ == '__main__':
    main()
