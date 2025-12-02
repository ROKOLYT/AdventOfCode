import json

sequence = r""""""

def format_sequence(seq):
    ranges = seq.strip().split(',')
    formatted_ranges = []
    for r in ranges:
        start, end = map(int, r.split('-'))
        formatted_ranges.append({'start': start, 'end': end})
    return json.dumps(formatted_ranges, indent=2)

if __name__ == "__main__":
    with open('formatted_sequence.json', 'w') as f:
        f.write(format_sequence(sequence))