def is_below(program, programs):
    for p in programs:
        if program["name"] in p["above"]:
            return False

    return True

def find_program(name, programs):
    for i, p in enumerate(programs):
        if p["name"] == name:
            return p, i
    
    return None

def balance(name, programs):
    program, i = find_program(name, programs)

    if program["total"] != 0:
        return program["total"]

    if len(program["above"]) == 0:
        program["total"] = program["weight"]
        programs[i] = program
        return program["total"]

    total = program["weight"]

    for above in program["above"]:
        total += balance(above, programs)

    program["total"] = total
    programs[i] = program

    return total

def is_balanced(program, programs):
    weights = set()

    for name in program["above"]:
        above, _ = find_program(name, programs)
        weights.add(above["total"])

    return len(weights) < 2

def fix_weight(program, programs):
    weights = [ ]

    for name in program["above"]:
        above, _ = find_program(name, programs)
        weights.append(above["total"])

    bad_weight, good_weight = 0, 0

    for w in set(weights):
        if weights.count(w) == 1:
            bad_weight = w
        else:
            good_weight = w

    for name in program["above"]:
        above, _ = find_program(name, programs)

        if above["total"] == bad_weight:
            return above["weight"] - (bad_weight - good_weight)

def main():
    f = open('./input.txt')

    programs = [ ]

    for line in f:
        name = line.strip().split(' (')[0]
        weight = int(line.strip().split(' (')[1].split(')')[0])
        above = [ ]

        if '->' in line:
            above = line.strip().split('-> ')[1].split(', ')
        
        p = { "name": name, "weight": weight, "above": above, "total": 0 }
        programs.append(p)

    f.close()

    below_program = { }

    for p in programs:
        if is_below(p, programs):
            below_program = p
            break

    print(f'Bottom program name (1): { below_program["name"] }')

    bad_program = { "total": 2 ** 32 - 1 }

    for p in programs:
        balance(p["name"], programs)

    for p in programs:
        if not is_balanced(p, programs) and p["total"] < bad_program["total"]:
            bad_program = p

    fixed_weight = fix_weight(bad_program, programs)

    print(f'Fixed weight (2): { fixed_weight }')

if __name__ == '__main__':
    main()
