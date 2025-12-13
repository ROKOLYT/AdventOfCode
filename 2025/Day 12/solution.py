import json

with open('formatted_input.json', 'r') as f:
    data = json.load(f)
    
def findSolution(data: dict[str, list[str] | list[dict[str, list[int] | int]]]) -> int:
    presents: list[str] = data['presents']  # type: ignore
    grids: list[dict[str, list[int] | int]] = data['grids']  # type: ignore
    
    res = 0
    
    for grid in grids:
        area: int = grid['x'] * grid['y']  # type: ignore
        occupied_area = 0
        
        for i, count in enumerate(grid['indexes']):  # type: ignore
            occupied_area += presents[i].count('#') * count  # type: ignore
        
        if occupied_area <= area:
            res += 1
            
    return res

if __name__ == "__main__":
    answer = findSolution(data)
    print(answer)
            
    
   