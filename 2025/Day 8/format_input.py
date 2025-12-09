import json

with open('input.txt') as f:
    data = f.read().strip()
    
def format_input(data: str) -> None:
    res = [{'x': int(entry[0]), 'y': int(entry[1]), 'z': int(entry[2])} for entry in (line.split(',') for line in data.splitlines())]
    with open('formatted_input.json', 'w') as f:
        json.dump(res, f, indent=4)
        
if __name__ == "__main__":
    format_input(data)
    