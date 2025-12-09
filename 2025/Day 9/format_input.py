import json

with open('input.txt') as f:
    data = f.read()
    
def format_input(data: str) -> list[tuple[int, int]]:
    return [(int(splits[0]), int(splits[1])) 
              for splits in (line.split(',') for line in data.splitlines())]
    
if __name__ == "__main__":
    points = format_input(data)
    with open('formatted_input.json', 'w') as f:
        json.dump(points, f, indent=4)