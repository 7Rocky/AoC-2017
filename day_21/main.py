import math

from functools import reduce


def unnormalize(pattern):
    return pattern.split('/')


def normalize(image):
    return '/'.join(image)


def count_on(image):
    return reduce(lambda x, y: x + y.count('#'), image, 0)


def flip(image):
    new_image = []

    for row in image:
        new_image.append(row[::-1])

    return new_image


def rotate(image):
    new_image = []

    for i in range(len(image)):
        new_row = []

        for j in range(len(image)):
            new_row.append(image[len(image) - 1 - j][i])

        new_image.append(''.join(new_row))

    return new_image


def transform(image, position):
    if position == 0:
        return image
    if position == 1:
        return flip(image)
    if position == 2:
        return rotate(image)
    if position == 3:
        return flip(rotate(image))
    if position == 4:
        return rotate(rotate(image))
    if position == 5:
        return flip(rotate(rotate(image)))
    if position == 6:
        return rotate(rotate(rotate(image)))
    if position == 7:
        return flip(rotate(rotate(rotate(image))))


def get_subimages(image):
    subimages = []

    if len(image) % 2 == 0:
        for j in range(int(len(image) / 2)):
            for i in range(int(len(image) / 2)):
                subimages.append([image[2 * j][2 * i:2 * (i + 1)],
                                  image[2 * j + 1][2 * i:2 * (i + 1)]])
    elif len(image) % 3 == 0:
        for j in range(int(len(image) / 3)):
            for i in range(int(len(image) / 3)):
                subimages.append([image[3 * j][3 * i:3 * (i + 1)],
                                  image[3 * j + 1][3 * i:3 * (i + 1)],
                                  image[3 * j + 2][3 * i:3 * (i + 1)]])

    return subimages


def join_subimages(subimages):
    image = []
    width = int(math.sqrt(len(subimages)))

    rows = [''] * len(subimages[0])

    for i, subimage in enumerate(subimages):
        for j in range(len(rows)):
            rows[j] += subimage[j]

        if (i + 1) % width == 0:
            for row in rows:
                image.append(row)

            rows = [''] * len(subimages[0])

    return image


def enhance(image, rules):
    subimages = get_subimages(image)
    new_subimages = []

    for subimage in subimages:
        for i in range(8):
            match = rules.get(normalize(transform(subimage, i)))

            if match != None:
                new_subimages.append(unnormalize(match))
                break

    return join_subimages(new_subimages)


def main():
    rules = {}

    with open('input.txt') as f:
        for line in f:
            split = line.strip().split(' => ')
            rules[split[0]] = split[1]

    image = ['.#.', '..#', '###']

    for i in range(18):
        if i == 5:
            print(f'Pixels on after 5 iterations (1): { count_on(image) }')

        image = enhance(image, rules)

    print(f'Pixels on after 18 iterations (2): { count_on(image) }')


if __name__ == '__main__':
    main()
