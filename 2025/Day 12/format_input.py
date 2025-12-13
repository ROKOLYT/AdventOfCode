import json

with open('input.txt', 'r') as f:
    data = f.read()
    
def format_input(data: str) -> dict[str, list[str] | list[dict[str, list[int] | int]]]:
    lines = data.splitlines()
    
    presents: list[str] = []
    present = ""
    grids: list[dict[str, list[int] | int]] = []
    grid: dict[str, list[int] | int] = {}
    formatting_presents = True
    
    for line in lines:
        if 'x' in line:
            formatting_presents = False
            
        if formatting_presents:
            if not line.strip() and present:
                presents.append(present.strip())
                present = ""
                
            elif ':' not in line:
                present += line + '\n'
        
        else:
            splits = line.split(':')
            
            x, y = map(int, splits[0].split('x'))
            
            indexes = list(map(int, splits[1].strip().split()))
            
            grid = {'x': x, 'y': y, 'indexes': indexes}
            grids.append(grid)
            
    return {'presents': presents, 'grids': grids}

if __name__ == "__main__":
    formatted_data = format_input(data)
    with open('formatted_input.json', 'w') as f:
        json.dump(formatted_data, f, indent=4)
        
        
        
            
            
    