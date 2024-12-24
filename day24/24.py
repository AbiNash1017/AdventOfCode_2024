import re

init_wires = {}
init_gates = set()
with open('D:/Advent of code/day24/input.txt', 'r') as f:
    pattern1 = r'(\w\w\w): (\d)'
    pattern2 = r'(\w\w\w) (\D+) (\w\w\w) -> (\w\w\w)'
    for line in f.readlines():
        if re.match(pattern1, line.strip()):
            wire, val = re.match(pattern1, line.strip()).groups()
            init_wires[wire] = int(val)
        elif re.match(pattern2, line.strip()):
            wire1, op, wire2, wire3 = re.match(pattern2, line.strip()).groups()
            init_gates.add((wire1, wire2, op, wire3))
            for w in (wire1, wire2, wire3):
                if w not in init_wires:
                    init_wires[w] = None

num_x_bits = sum(w[0] == 'x' for w in init_wires)
num_y_bits = sum(w[0] == 'y' for w in init_wires)
num_z_bits = sum(w[0] == 'z' for w in init_wires)

def get_z(gates, xy=None):
    wire_map = init_wires.copy()
    if xy is not None:
        x, y = xy
        bin_x = bin(x)[2:].zfill(num_x_bits)
        for i, bit in enumerate(reversed(bin_x)):
            wire_map['x'+str(i).zfill(2)] = int(bit)
        bin_y = bin(y)[2:].zfill(num_y_bits)
        for i, bit in enumerate(reversed(bin_y)):
            wire_map['y'+str(i).zfill(2)] = int(bit)
    while any(w[0] == 'z' and wire_map[w] is None for w in wire_map):
        to_remove = []
        for gate in gates:
            wire1, wire2, op, wire3 = gate
            if wire_map[wire3] is not None:
                to_remove.append(gate)
                continue
            if wire_map[wire1] is not None and wire_map[wire2] is not None:
                if op == 'AND':
                    wire_map[wire3] = wire_map[wire1] & wire_map[wire2]
                elif op == 'OR':
                    wire_map[wire3] = wire_map[wire1] | wire_map[wire2]
                elif op == 'XOR':
                    wire_map[wire3] = wire_map[wire1] ^ wire_map[wire2]
                to_remove.append(gate)
        if not to_remove:
            return None
        for gate in to_remove:
            gates.remove(gate)
    z_bits = []
    for w in sorted(wire for wire in wire_map if wire[0] == 'z'):
        z_bits.append(str(wire_map[w]))
    z = ''.join(reversed(z_bits))
    return z

# part 1
z = get_z(init_gates.copy())
print(int('0b' + z, 2))

# part 2
def get_num_mistakes(gates):
    result = 0
    for p in range(45):
        x = 2**p
        z = get_z(gates.copy(), (x, 0))
        if z is None:
            result += 1
        elif int('0b'+z, 2) != x:
            result += 1
    return result

print(get_num_mistakes(init_gates))

def get_swapped_gates(pairs):
    new_gates = init_gates.copy()
    for w1, w2 in pairs:
        for gate1 in new_gates:
            if gate1[3] == w1:
                break
        for gate2 in new_gates:
            if gate2[3] == w2:
                break
        new_gate_1 = (gate1[0], gate1[1], gate1[2], gate2[3])
        new_gate_2 = (gate2[0], gate2[1], gate2[2], gate1[3])
        new_gates.remove(gate1)
        new_gates.remove(gate2)
        new_gates.add(new_gate_1)
        new_gates.add(new_gate_2)
    return new_gates

# w1 = 'z16'
# for w2 in init_wires:
#     if w2 == w1:
#         continue
#     num_mistakes = get_num_mistakes(get_swapped_gates([(w1, w2)]))
#     if num_mistakes < 4:
#         print(w1, w2, num_mistakes)

## The following were found via a mix of inspecting the logic
## and using the above helper methods
pairs = [('z08', 'vvr'), ('rnq', 'bkr'), ('z28', 'tfb'), ('z39', 'mqh')]
print(','.join(sorted(['z08', 'vvr', 'rnq', 'bkr', 'z28', 'tfb', 'z39', 'mqh']))) 
