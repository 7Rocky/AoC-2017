import re


def remove_ignored(groups):
    return re.sub(r'!.', '', groups)


def remove_garbage(groups):
    new_groups = ''
    is_garbage = False
    count = 0

    for char in groups:
        if is_garbage:
            count += 1

        if char == '<':
            is_garbage = True
        elif char == '>':
            is_garbage = False
            count -= 1

        if not is_garbage:
            new_groups += char

    return new_groups, count


def score(groups):
    depth, count = 0, 0

    for char in groups:
        if char == '{':
            depth += 1
            count += depth
        elif char == '}':
            depth -= 1

    return count


def main():
    f = open('input.txt')

    groups = ''

    for line in f:
        groups = line.strip()

    f.close()

    groups = remove_ignored(groups)
    groups, count_garbage = remove_garbage(groups)

    print(f'Total score (1): { score(groups) }')
    print(f'Max value held during the process (2): { count_garbage }')


if __name__ == '__main__':
    main()
