class Program:
    def __init__(self):
        self.registers = {}
        self.count = 0
        self.pc = 0

    def extract(self, instruction):
        instruction, reg, number = instruction.split(' ')

        try:
            number = int(number)
        except ValueError:
            number = self.registers[number]

        if not self.registers.get(reg):
            self.registers[reg] = 0

        return instruction, reg, number

    def process(self, instructions, program=None):
        while self.pc < len(instructions):
            instruction, reg, number = self.extract(instructions[self.pc])
            self.do_instruction(instruction, reg, number)
            self.pc += 1

    def do_instruction(self, instruction, reg, number):
        if instruction == 'set':
            self.registers[reg] = number
        elif instruction == 'sub':
            self.registers[reg] -= number
        elif instruction == 'mul':
            self.count += 1
            self.registers[reg] *= number
        elif instruction == 'jnz':
            try:
                self.pc += number - 1 if int(reg) != 0 else 0
            except ValueError:
                self.pc += number - 1 if self.registers[reg] != 0 else 0


def is_prime(number):
    if number % 2 == 0:
        return False

    d = 1

    while d ** 2 < number:
        d += 2

        if number % d == 0:
            return False

    return True


def main():
    with open('input.txt') as f:
        instructions = [line.strip() for line in f]

    program = Program()
    program.process(instructions)

    print(f'First frequency received (1): { program.count }')

    first_number = int(instructions[0].split(' ').pop())

    b = 100 * first_number + 100000
    c = b + 17000
    h = 0

    for x in range(b, c + 1, 17):
        if not is_prime(x):
            h += 1

    print(f'Value of register "h" (2): { h }')


if __name__ == '__main__':
    main()
