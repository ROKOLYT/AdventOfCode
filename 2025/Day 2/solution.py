import json
from typing import List

with open('formatted_sequence.json', 'r') as f:
    data = json.load(f)
    
def decodeInvalid(data: List[dict[str, int]]) -> int:
    answer = 0
    
    for entry in data:
        start = entry['start']
        end = entry['end']
        
        for i in range(start, end + 1, 1):
            if not isValidNew(str(i)):
                answer += i
        
    return answer
        
def isValid(number: str) -> bool:
    
    if len(number) % 2 != 0:
        return True
    
    half = len(number) // 2
    first_half = number[:half]
    second_half = number[half:]
    
    if first_half == second_half:
        return False
    
    return True

def isValidNew(number: str) -> bool:
    
    for i in range(1, (len(number) // 2) + 1, 1):
        if len(number) % i != 0:
            continue
        
        splits = split_number(number, i)
        if len(set(splits)) == 1:
            return False
        
    return True
        
def split_number(s: str, n: int) -> List[str]:
    return [s[i:i+n] for i in range(0, len(s), n)]

if __name__ == '__main__':
    answer = decodeInvalid(data)
    print(answer)