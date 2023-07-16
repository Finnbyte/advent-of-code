import re


def retrieve_signal(table, wire: str) -> int | None:
    try:
        return int(wire)
    except ValueError:
        if wire in table:
            return table[wire]
    return None


def process_instruction(table, instruction: str) -> tuple[int | None, str]:
    parts = re.split(" -> | ", instruction)
    target = parts[-1]

    if len(parts) == 2:
        wire = retrieve_signal(table, parts[0])
        return (wire, target)

    if parts[0] == "NOT":
        wire = retrieve_signal(table, parts[1])
        if wire is not None:
            return ((~wire) & 0xFFFF, target)
        else:
            return (None, target)

    operand = parts[1]

    wire1 = retrieve_signal(table, parts[0])
    wire2 = retrieve_signal(table, parts[2])

    if wire1 is not None and wire2 is not None:
        match operand:
            case "AND":
                return (wire1 & wire2, target)
            case "OR":
                return (wire1 | wire2, target)
            case "LSHIFT":
                return (wire1 << wire2, target)
            case "RSHIFT":
                return (wire1 >> wire2, target)

    return (None, target)


wires = {}


def get_instructions():
    with open("input.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def resolve_instructions(instructions):
    failures = []  # List to keep track of wires with missing signals

    for instruction in instructions:
        (val, target) = process_instruction(wires, instruction)

        if val is not None:
            wires[target] = min(int(val), 65535)
        else:
            failures.append(instruction)

    return failures


instructions = get_instructions()
while instructions:
    failures = resolve_instructions(instructions)
    if not failures:
        break
    instructions = failures

print(wires["a"])
