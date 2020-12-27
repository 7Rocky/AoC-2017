import math

def sum_adjacent(sum_rings, point):
    return sum_rings[point + 1] + sum_rings[point - 1] + \
        sum_rings[point + 1j] + sum_rings[point - 1j] + \
        sum_rings[point + 1 + 1j] + sum_rings[point - 1 + 1j] + \
        sum_rings[point + 1 - 1j] + sum_rings[point - 1 - 1j]

def main():
    puzzle_input = 361527

    rings = [ sum(range(i+1)) for i in range(400) ]

    for i, r in enumerate(rings):
        if r >= math.ceil((puzzle_input - 1) / 8):
            ring = i
            break

    recreate_ring = [ i for i in range(8 * rings[ring-1] + 2, 8 * rings[ring] + 2) ]
    despl = abs((recreate_ring.index(puzzle_input) + 1) % (len(recreate_ring) // 4) - ring)

    print(f'Manhattan distance from input (1): { ring + despl }')

    sum_rings = { }
    span = 5

    for x in range(-span, span + 1):
        for y in range(-span, span + 1):
            sum_rings[x + y * 1j] = 0

    ring = 1
    pivot = 0
    sum_rings[pivot] = 1
    d = 1

    while sum_rings[pivot] < puzzle_input:
        pivot += d
        sum_rings[pivot] = sum_adjacent(sum_rings, pivot)

        if abs(pivot.real) + abs(pivot.imag) == 2 * ring or pivot == ring + (1 - ring) * 1j:
            d *= 1j

            if pivot == ring * (1 - 1j):
                d = 1
                ring += 1

    print(f'First number larger than input (2): { sum_rings[pivot] }')

if __name__ == '__main__':
    main()
