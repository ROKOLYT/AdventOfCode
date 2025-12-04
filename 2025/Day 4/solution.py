from typing import List

with open('papers.txt', 'r') as f:
    data = f.read()
    
def findSolution(data: str) -> int | str:
    lines = data.splitlines()
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    answer = 0
    res = []
    
    for row in range(rows):
        line = []
        for col in range(cols):
            if isValid(row, col, lines):
                line.append('.')
                answer += 1
            else:
                line.append(lines[row][col])
                
        res.append(''.join(line))
        
    result_str = '\n'.join(res)
    return answer, result_str

def findSolutionNew(data: str) -> int:
    answer = 0
    while findSolution(data)[0] != 0:
        count, data = findSolution(data)
        answer += count
    return answer
            
def isValid(row: int, col: int, data: List[str]) -> bool:
    adjescent = 0
    
    if data[row][col] != '@':
        return False
    
    for rowk in range(3):
        for colk in range(3):
            row_index = row - 1 + rowk
            col_index = col - 1 + colk
            
            if not (0 <= row_index < len(data) and 0 <= col_index < len(data[0])):
                continue
            
            if data[row_index][col_index] == '@':
                adjescent += 1
    
    if adjescent < 5:
        return True
    return False

def testFindSolution():
    data = r"""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
    
    assert findSolution(data)[0] == 13
    
if __name__ == '__main__':
    testFindSolution()
    answer = findSolutionNew(data)
    print(answer)
            
            
            
            
    