def verify_position(pos, grid):
    if pos.real == -1:
        pos += 1

        for i in range(len(grid)):
            grid[i].insert(0, '.')
    elif pos.imag == -1:
        pos += 1j
        grid.insert(0, ['.'] * len(grid[0]))
    elif pos.real == len(grid[0]):
        for i in range(len(grid)):
            grid[i].append('.')
    elif pos.imag == len(grid):
        grid.append(['.'] * len(grid[0]))

    return pos


def burst_1(grid, virus):
    global infected_nodes

    pos = virus['position']

    if grid[int(pos.imag)][int(pos.real)] == '#':
        virus['direction'] *= 1j
        grid[int(pos.imag)][int(pos.real)] = '.'
    else:
        virus['direction'] *= -1j
        grid[int(pos.imag)][int(pos.real)] = '#'
        infected_nodes += 1

    virus['position'] = verify_position(pos + virus['direction'], grid)


def burst_2(grid, virus):
    global infected_nodes

    pos = virus['position']
    node = grid[int(pos.imag)][int(pos.real)]

    if node == '.':
        virus['direction'] *= -1j
        grid[int(pos.imag)][int(pos.real)] = 'W'
    elif node == 'W':
        grid[int(pos.imag)][int(pos.real)] = '#'
        infected_nodes += 1
    elif node == '#':
        virus['direction'] *= 1j
        grid[int(pos.imag)][int(pos.real)] = 'F'
    elif node == 'F':
        virus['direction'] *= -1
        grid[int(pos.imag)][int(pos.real)] = '.'

    virus['position'] = verify_position(pos + virus['direction'], grid)


infected_nodes = 0


def get_infected_nodes(grid, bursts, level):
    global infected_nodes

    infected_nodes = 0

    virus = {
        'direction': -1j,
        'position': len(grid) // 2 * (1 + 1j)
    }

    if level == 1:
        for _ in range(bursts):
            burst_1(grid, virus)
    elif level == 2:
        for _ in range(bursts):
            burst_2(grid, virus)

    return infected_nodes


def main():
    grid_1, grid_2 = [], []

    with open('input.txt') as f:
        for line in f:
            grid_1.append([c for c in line.strip()])
            grid_2.append([c for c in line.strip()])

    infected_nodes = get_infected_nodes(grid_1, 10000, 1)

    print(f'Infected nodes (1): { infected_nodes }')

    infected_nodes = get_infected_nodes(grid_2, 10000000, 2)

    print(f'Infected nodes (2): { infected_nodes }')


if __name__ == '__main__':
    main()
