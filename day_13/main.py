class Scanner:
    def __init__(self, depth, rank):
        self.depth = depth
        self.rank = rank
        self.pos = 0
        self.caught = False

    def set_delay_pos(self, delay):
        mod = 2 * self.rank - 2
        self.pos = (delay + self.depth) % mod

        if self.pos >= self.rank:
            self.pos = mod * (self.pos // mod + 1) - self.pos

        self.caught = self.pos == 0


def get_severity(scanners):
    for scanner in scanners:
        scanner.set_delay_pos(0)

    return sum([s.depth * s.rank * int(s.caught) for s in scanners])


def main():
    f = open('input.txt')

    scanners = []

    for line in f:
        depth, rank = line.strip().split(': ')
        scanners.append(Scanner(int(depth), int(rank)))

    f.close()

    print(f'Severity of the trip (1): { get_severity(scanners) }')

    delay = 0
    caught = True

    while caught:
        caught = False
        delay += 1

        for scanner in scanners:
            scanner.set_delay_pos(delay)

            if scanner.caught:
                caught = True
                break

    print(f'Minimum delay to pass without been caught (2): { delay }')


if __name__ == '__main__':
    main()
