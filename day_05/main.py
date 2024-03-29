def escape_maze(maze, level):
    steps, i = 0, 0

    while 0 <= i < len(maze):
        steps += 1
        offset = maze[i]
        maze[i] += 1

        if level == 2 and offset >= 3:
            maze[i] -= 2

        i += offset

    return steps


def main():
    maze = []

    with open('input.txt') as f:
        for line in f:
            maze.append(int(line.strip()))

    for level in [1, 2]:
        steps = escape_maze(maze.copy(), level)
        print(f'Steps to escape the maze ({ level }): { steps }')


if __name__ == '__main__':
    main()
