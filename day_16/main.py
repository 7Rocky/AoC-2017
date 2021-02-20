def move_programs(programs, move):
    if move[0] == 's':
        despl = int(move[1:])
        programs = programs[-despl:] + programs[:-despl]
    elif move[0] == 'x':
        a, b = map(int, move[1:].split('/'))
        programs[a], programs[b] = programs[b], programs[a]
    elif move[0] == 'p':
        a, b = map(programs.index, move[1:].split('/'))
        programs[a], programs[b] = programs[b], programs[a]

    return programs


def main():
    f = open('input.txt')

    programs = [bytes([i + 97]).decode() for i in range(16)]
    initial_programs = programs.copy()

    for line in f:
        moves = line.strip().split(',')

    f.close()

    i = 0

    while i < 1_000_000_000:
        for move in moves:
            programs = move_programs(programs, move)
        if i == 0:
            print(f"Programs order (1): { ''.join(programs) }")

        i += 1

        if programs == initial_programs:
            i = (1_000_000_000 // i) * i

    print(f"Programs order (2): { ''.join(programs) }")


if __name__ == '__main__':
    main()
