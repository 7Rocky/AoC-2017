def main():
    program_connections = {}

    with open('input.txt') as f:
        for line in f:
            program, connections = line.strip().split(' <-> ')
            program_connections[int(program)] = set(
                [int(p) for p in connections.split(', ')])

    groups = []

    for p in program_connections:
        if sum([int(p in g) for g in groups]):
            continue

        group = set(program_connections[p])
        final_length = 0

        while final_length != len(group):
            final_length = len(group)

            for program, connections in program_connections.items():
                if program in group:
                    group.update(connections)

        if group not in groups:
            groups.append(group)

    print(f'Number of elements of group 0 (1): { len(groups[0]) }')
    print(f'Number of distinct groups (2): { len(groups) }')


if __name__ == '__main__':
    main()
