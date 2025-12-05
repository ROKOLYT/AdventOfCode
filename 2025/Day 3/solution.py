import json
from typing import List

with open('sequence.json', 'r') as file:
    sequences = json.load(file)
    
def findSolution(sequences: List[str], n: int) -> int:
    answer = 0
    
    for sequence in sequences:
        answer += findBiggestJoltageNew(sequence, n)
    
    return answer
    
    
def findBiggestJoltage(s: str) -> int:
    splits = splitString(s)
    
    first_digit = max(splits[:-1])
    index = splits.index(first_digit)
    second_digit = max(splits[index + 1:])
    
    return int(str(first_digit) + str(second_digit))

def findBiggestJoltageNew(s: str, n: int) -> int:
    splits = splitString(s)
    digits: List[int] = []
    prevIndex = -1
    
    for i in range(1, n + 1, 1):
        lastIndex = i - n
        
        if lastIndex != 0:
            digits.append(max(splits[(prevIndex + 1):(lastIndex)]))
        else:
            digits.append(max(splits[(prevIndex + 1):]))
            
        prevIndex = splits.index(digits[-1], prevIndex + 1)
        
    number = ''.join(str(digit) for digit in digits)
    return int(number)  

def testFindBiggestJoltageNew():
    assert findBiggestJoltageNew("123456789", 3) == 789
    assert findBiggestJoltageNew("987654321", 2) == 98
    assert findBiggestJoltageNew("543216789", 4) == 6789
    
    
def splitString(s: str) -> List[int]:
    return [int(s[i:i+1]) for i in range(len(s))]

if __name__ == '__main__':
    testFindBiggestJoltageNew()
    answer = findSolution(sequences, 12)
    print(answer)