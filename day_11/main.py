steps = {
    'ne': 1+1j,
    'n': 2j,
    'se': 1-1j,
    'sw': -1-1j,
    's': -2j,
    'nw': -1+1j
}


def get_steps(pos):
    num_steps = abs(pos.real)

    if abs(pos.imag) - abs(pos.real) > 0:
        num_steps += (abs(pos.imag) - abs(pos.real)) / 2

    return int(num_steps)


def main():
    with open('input.txt') as f:
        for line in f:
            moves = [m for m in line.strip().split(',')]

    max_num_steps, pos = 0, 0

    for s in [steps[m] for m in moves]:
        pos += s
        num_steps = get_steps(pos)

        if max_num_steps < num_steps:
            max_num_steps = num_steps

    print(f'Number of steps to final position (1): { num_steps }')
    print(f'Number of steps to furthest position (2): { max_num_steps }')


if __name__ == '__main__':
    main()
