data = """
"""

import json

def parse_data(data):
    lines = data.splitlines()
    d = {'intervals': [], 'ids': []}
    
    for line in lines:
        if '-' in line:
            start, end = map(int, line.split('-'))
            d['intervals'].append((start, end))
        elif line.strip():
            d['ids'].append(int(line))
    
    with open('formatted_data.json', 'w') as f:
        json.dump(d, f, indent=4)
        
if __name__ == "__main__":
    parse_data(data)
