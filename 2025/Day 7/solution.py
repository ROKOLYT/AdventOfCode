with open('input.txt', 'r') as f:
    data = f.read()
    
def findSolution(data: str) -> int:
    lines = data.splitlines()
    beams = [False for _ in range(len(lines[0]))]
    beams[lines[0].index('S')] = True
    res = 0
    
    for line in lines[1:]:
        for i, char in enumerate(line):
            if char != '^':
                continue
            
            if beams[i]:
                beams[i - 1] = True
                beams[i + 1] = True
                beams[i] = False
                res += 1
                
    return res

def findSolutionNew(lines: list[str], x: int, y: int, state: dict[tuple[int, int], int] | None = None) -> int:
    if state is None:
        state = {}
    
    key = (x, y)
    if key in state:
        return state[key]
    
    if y >= len(lines):
        return 1
    
    if x < 0 or x >= len(lines[y]):
        return 0
    
    if lines[y][x] == '^':
        left = findSolutionNew(lines, x - 1, y + 1, state)
        right = findSolutionNew(lines, x + 1, y + 1, state)
        result = left + right
    else:
        result = findSolutionNew(lines, x, y + 1, state)
    
    state[key] = result
    return result
            

if __name__ == '__main__':
    state: dict[str, int] = {}
    lines = data.splitlines()
    answer = findSolutionNew(lines, lines[0].index('S'), 0)
    print(answer)
    answer = findSolution(data)
    print(answer)
            