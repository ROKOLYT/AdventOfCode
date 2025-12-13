import json

with open('input.txt', 'r') as f:
    data = f.read()
    
def format_input(data: str) -> list[dict[str, list[str]]]:
    entries = data.splitlines()
    
    formatted_entries: list[dict[str, list[str]]] = []
    for entry in entries:
        key, values = entry.split(':')
        value_list = values.split()
        
        formatted_entries.append({key: value_list})
        
    return formatted_entries

if __name__ == "__main__":
    formatted_data = format_input(data)
    with open('formatted_input.json', 'w') as f:
        json.dump(formatted_data, f, indent=4)
    