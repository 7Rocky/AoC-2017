import re


class Particle:
    def __init__(self, number, position, velocity, acceleration):
        self.number = number
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.destroyed = False

    def move(self):
        for i in range(len(self.acceleration)):
            self.velocity[i] += self.acceleration[i]

        for i in range(len(self.velocity)):
            self.position[i] += self.velocity[i]

    def distance(self):
        x, y, z = self.position
        return abs(x) + abs(y) + abs(z)


def get_positions_count(particles):
    positions_count = {}

    for particle in particles:
        position_str = ''.join(map(str, particle.position))

        if not positions_count.get(position_str):
            positions_count[position_str] = [particle]
        else:
            positions_count[position_str].append(particle)

    return positions_count


def remaining_particles(particles, positions_count):
    for position in positions_count:
        if len(positions_count[position]) > 1:
            for particle in positions_count[position]:
                particle.destroyed = True

    return [particle for particle in particles if not particle.destroyed]


def main():
    particles, colliding_particles = [], []

    with open('input.txt') as f:
        for i, line in enumerate(f):
            m = re.match(
                r'p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>',
                line
            )

            particles.append(Particle(i, [int(m[1]), int(m[2]), int(m[3])], [int(
                m[4]), int(m[5]), int(m[6])], [int(m[7]), int(m[8]), int(m[9])]))
            colliding_particles.append(Particle(i, [int(m[1]), int(m[2]), int(m[3])], [int(
                m[4]), int(m[5]), int(m[6])], [int(m[7]), int(m[8]), int(m[9])]))

    finished = 1000
    min_distance = 2 ** 32 - 1

    while finished != 0:
        for particle in particles:
            particle.move()

        finished -= 1

        for particle in particles:
            distance = particle.distance()

            if min_distance > distance:
                min_distance = distance
                finished += 1
                break

    particles.sort(key=lambda p: p.distance())

    print(f'Closest particle (1): { particles[0].number }')

    remaining = len(colliding_particles)
    finished = 100

    while finished != 0:
        for particle in colliding_particles:
            particle.move()

        positions_count = get_positions_count(colliding_particles)

        colliding_particles = remaining_particles(
            colliding_particles, positions_count)

        if remaining == len(colliding_particles):
            finished -= 1
        else:
            remaining = len(colliding_particles)

    print(f'Remaining particle (2): { remaining }')


if __name__ == '__main__':
    main()
