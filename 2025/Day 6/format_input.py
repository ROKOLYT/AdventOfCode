import json

with open('input.txt', 'r') as f:
    data = f.read()

def formatInput(data: str) -> list[list[str]]:
    return [line.split() for line in data.splitlines()]

def transposeInput(data: list[list[str]]) -> list[list[str]]:
    return [list(row) for row in zip(*data)]

if __name__ == '__main__':
    formatted_input = formatInput(data)
    transposed_input = transposeInput(formatted_input)
    with open('formatted_input.json', 'w') as f:
        json.dump(transposed_input, f)
