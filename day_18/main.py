class Program:
    def __init__(self, program_id):
        self.registers = {'p': program_id}
        self.count = 0
        self.sounds = []
        self.pc = 0

    def extract(self, instruction):
        number = None

        if instruction.count(' ') > 1:
            instruction, reg, number = instruction.split(' ')

            try:
                number = int(number)
            except ValueError:
                number = self.registers[number]
        else:
            instruction, reg = instruction.split(' ')

        if not self.registers.get(reg):
            self.registers[reg] = 0

        return instruction, reg, number

    def process(self, instructions, program=None):
        sound = 0

        while self.pc < len(instructions):
            instruction, reg, number = self.extract(instructions[self.pc])

            if program:
                end = self.co_process(instruction, reg, number, program)

                if end:
                    return
            else:
                sound = self.process_alone(sound, instruction, reg, number)

                if self.count > 0:
                    return sound

            self.pc += 1

    def do_instruction(self, instruction, reg, number):
        if instruction == 'set':
            self.registers[reg] = number
        elif instruction == 'add':
            self.registers[reg] += number
        elif instruction == 'mul':
            self.registers[reg] *= number
        elif instruction == 'mod':
            self.registers[reg] %= number
        elif instruction == 'jgz':
            try:
                self.pc += number - 1 if int(reg) > 0 else 0
            except ValueError:
                self.pc += number - 1 if self.registers[reg] > 0 else 0

    def process_alone(self, sound, instruction, reg, number):
        if instruction == 'snd':
            sound = self.registers[reg]
        elif instruction == 'rcv' and self.registers[reg] != 0:
            self.count += 1
        else:
            self.do_instruction(instruction, reg, number)

        return sound

    def co_process(self, instruction, reg, number, program):
        if instruction == 'snd':
            program.sounds.append(self.registers[reg])
            self.count += 1
        elif instruction == 'rcv':
            if len(self.sounds) == 0:
                return True
            self.registers[reg] = self.sounds.pop(0)
        else:
            self.do_instruction(instruction, reg, number)


def main():
    f = open('input.txt')

    instructions = [line.strip() for line in f]

    f.close()

    sound = Program(0).process(instructions)

    print(f'First frequency received (1): { sound }')

    programs = [Program(0), Program(1)]

    i = 0

    while True:
        programs[i % 2].process(instructions, programs[(i + 1) % 2])
        i += 1

        if len(programs[i % 2].sounds) == 0:
            break

    print(
        f'Number of sent frequencies by Program 1 (2): { programs[1].count }')


if __name__ == '__main__':
    main()
