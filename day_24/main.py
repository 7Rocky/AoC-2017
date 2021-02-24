pins = []
max_strength = 0
longest_bridge = '0'


def next_nodes(node):
    global pins

    next_nodes = []
    connection = node['ports'].split('/')[0 if node.get('reversed') else 1]

    for pin in pins:
        if connection == pin['ports'].split('/')[0]:
            next_nodes.append(pin)
        elif connection == pin['ports'].split('/')[1]:
            next_nodes.append({'ports': pin['ports'], 'reversed': True})

    return next_nodes


def depth_first_search(root, bridge):
    global max_strength
    global longest_bridge

    root['visited'] = True
    bridge += '--' + root['ports']

    for node in next_nodes(root):
        if node['ports'] not in bridge:
            depth_first_search(node, bridge)

    strength = get_strength(bridge)

    max_strength = max([strength, max_strength])
    length = bridge.count('--')
    max_length = longest_bridge.count('--')

    if max_length < length:
        longest_bridge = bridge

    if max_length == length:
        longest_bridge_strength = get_strength(longest_bridge)

        if longest_bridge_strength < strength:
            longest_bridge = bridge


def get_strength(bridge):
    return sum(map(lambda x: sum(map(int, x.split('--'))), bridge.split('/')))


def main():
    f = open('input.txt')

    global pins
    pins = [{'ports': line.strip()} for line in f]

    f.close()

    depth_first_search({'ports': '0/0'}, '0')

    global max_strength
    global longest_bridge

    print(f'Maximum bridge strength (1): { max_strength }')
    print(f'Longest bridge strength (2): { get_strength(longest_bridge) }')


if __name__ == '__main__':
    main()
