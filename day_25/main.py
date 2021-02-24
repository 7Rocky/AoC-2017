import re


def run(state, tape, cursor):
    global states

    current_value = tape[cursor]

    tape[cursor] = states[state][current_value]['write']
    cursor += states[state][current_value]['move']
    state = states[state][current_value]['continue']

    if cursor < 0:
        cursor = 0
        tape.insert(0, 0)
    elif cursor == len(tape):
        tape.append(0)

    return state, cursor


states = {}


def main():
    f = open('input.txt')

    lines = [line.strip() for line in f if line != '\n']

    f.close()

    state = re.match(r'Begin in state (\w)\.', lines.pop(0))[1]
    steps = int(re.match(
        r'Perform a diagnostic checksum after (\d+) steps\.', lines.pop(0))[1])

    num_states = sum([int('In state ' in line) for line in lines])

    global states

    for i in range(num_states):
        state_lines = lines[9 * i: 9 * (i + 1)]
        state_name = re.match(r'In state (\w):', state_lines[0])[1]

        states[state_name] = [
            {
                'write': int(re.match(r'- Write the value (0|1)\.', state_lines[2])[1]),
                'move': 1 if re.match(r'- Move one slot to the (left|right)\.',
                                      state_lines[3])[1] == 'right' else -1,
                'continue': re.match(r'- Continue with state (\w)\.', state_lines[4])[1]
            }, {
                'write': int(re.match(r'- Write the value (0|1)\.', state_lines[6])[1]),
                'move': 1 if re.match(r'- Move one slot to the (left|right)\.',
                                      state_lines[7])[1] == 'right' else -1,
                'continue': re.match(r'- Continue with state (\w)\.', state_lines[8])[1]
            }
        ]

    tape = [0]
    cursor = 0

    for _ in range(steps):
        state, cursor = run(state, tape, cursor)

    print(f'Diagnostic checksum (1): { sum(tape) }')


if __name__ == '__main__':
    main()
