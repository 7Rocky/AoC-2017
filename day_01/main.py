def solve(captcha, next):
    return sum(int(captcha[i - next])
               for i in range(len(captcha)) if captcha[i - next] == captcha[i])


def main():
    f = open('input.txt')

    captcha = f.readline().strip()

    f.close()

    print(f'Solution to captcha (1): { solve(captcha, 1) }')
    print(f'Solution to captcha (2): { solve(captcha, len(captcha) // 2) }')


if __name__ == '__main__':
    main()
