import re


def set_regs(regs, m):
    reg, op, num_op = m.group(1), m.group(2), int(m.group(3))
    reg_cond, cond, num_cond = m.group(4), m.group(5), int(m.group(6))

    if op == 'dec':
        num_op *= -1

    if regs.get(reg) == None:
        regs[reg] = 0

    if regs.get(reg_cond) == None:
        regs[reg_cond] = 0

    if (cond == '==' and regs[reg_cond] == num_cond) \
            or (cond == '!=' and regs[reg_cond] != num_cond) \
            or (cond == '<=' and regs[reg_cond] <= num_cond) \
            or (cond == '>=' and regs[reg_cond] >= num_cond) \
            or (cond == '<' and regs[reg_cond] < num_cond) \
            or (cond == '>' and regs[reg_cond] > num_cond):

        regs[reg] += num_op


def main():
    regs = {}
    max_value = 0

    with open('input.txt') as f:
        for line in f:
            if m := re.match(
                r"(\w+) (inc|dec) (-?\d+) if (\w+) (==|!=|<=|>=|<|>) (-?\d+)",
                line
            ):
                set_regs(regs, m)

            if max_value < max(regs.values()):
                max_value = max(regs.values())

    print(f'Max value after the process (1): { max(regs.values()) }')
    print(f'Max value held during the process (2): { max_value }')


if __name__ == '__main__':
    main()
