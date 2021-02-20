def handle_turn(tubes, position, direction):
    if (abs(direction.real) == 1 and
            int(position.imag - direction.real) < len(tubes) and
            tubes[int(position.imag - direction.real)][int(position.real)] != ' ') or \
        (abs(direction.imag) == 1 and
            int(position.real - direction.imag) < len(tubes[int(position.imag)]) and
            tubes[int(position.imag)][int(position.real - direction.imag)] == ' '):
        return direction * -1j

    return direction * 1j


def travel_tubes(tubes, position, direction):
    chars = []
    steps = 0

    current = tubes[int(position.imag)][int(position.real)]

    while current != ' ':
        if current not in '-|+':
            chars.append(current)
        elif current == '+':
            direction = handle_turn(tubes, position, direction)

        position += direction
        steps += 1
        current = tubes[int(position.imag)][int(position.real)]

    return ''.join(chars), steps


def main():
    f = open('input.txt')

    tubes = [line for line in f]

    f.close()

    chars, steps = travel_tubes(tubes, tubes[0].index('|'), 1j)

    print(f"Seen letters (1): { ''.join(chars) }")
    print(f'Number of steps needed (2): { steps }')


if __name__ == '__main__':
    main()
