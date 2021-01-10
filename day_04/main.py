def is_valid(passphrase, level):
    words = passphrase.split(' ')

    for i in range(len(words)):
        if level == 1 and words.count(words[i]) > 1:
            return False

        if level == 2:
            for j in range(i + 1, len(words)):
                if set(words[i]) == set(words[j]):
                    return False

    return True


def main():
    f = open('input.txt')

    passphrases = []

    for line in f:
        passphrases.append(line.strip())

    f.close()

    count = [0, 0]

    for level in [1, 2]:
        for passphrase in passphrases:
            if is_valid(passphrase, level):
                count[level - 1] += 1

        print(f'Number of valid pashphrases ({ level }): { count[level - 1] }')


if __name__ == '__main__':
    main()
