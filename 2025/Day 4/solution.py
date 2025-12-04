from typing import List
import json

with open('papers.txt', 'r') as f:
    data = f.read()
 
with open('papers.json', 'r') as f:
    papers = json.load(f)
    
def findSolution(data: str) -> int:
    lines = data.splitlines()
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    answer = 0
    
    for row in range(rows):
        for col in range(cols):
            if isValid(row, col, lines):
                answer += 1
                
    return answer

def findSolutionNew(data: List[List[str]], answer: int = 0) -> int:
    original_answer = answer
    new_data = []
    
    for i, row in enumerate(data):
        new_line = []
        
        for j, elem in enumerate(row):
            if isValid(i, j, data):
                new_line.append('.')
                answer += 1
            else:
                new_line.append(elem)
        new_data.append(new_line)
    
    if original_answer != answer:
        return findSolutionNew(new_data, answer)
    
    return answer
          
def isValid(row: int, col: int, data: List) -> bool:
    adjascent = 0
    
    if data[row][col] != '@':
        return False
    
    for row_offset in range(3):
        for col_offset in range(3):
            row_index = row - 1 + row_offset
            col_index = col - 1 + col_offset
            
            if not (0 <= row_index < len(data) and 0 <= col_index < len(data[0])):
                continue
            
            if data[row_index][col_index] == '@':
                adjascent += 1
    
    if adjascent < 5:
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
    
    assert findSolution(data) == 13
    
if __name__ == '__main__':
    testFindSolution()
    answer = findSolutionNew(papers)
    print(answer)
            
            
            
            
    