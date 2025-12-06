import json

with open('formatted_input.json', 'r') as f:
    data = json.load(f)

with open('input.txt', 'r') as f:
    raw_data: str = f.read()
    
def findSolution(data: list[list[str]]) -> int:
    res = 0
    
    for equation in data:
        numbers = list(map(int, equation[:-1]))
        operation = equation[-1]
        
        res += calculateEquation(numbers, operation)
        
    return res

# Both are obsolete I incorrectly assumed that we check each number regardless of how it was formatted in the input
def findSolutionObsolete(data: list[list[str]]) -> int:
    res = 0
    
    for equation in data:
        numbers = findCorrectNumbersObsolete(equation)
        operation = equation[-1]
        
        res += calculateEquation(numbers, operation)
        
    return res
        
def findCorrectNumbersObsolete(equation: list[str]) -> list[int]:
    original_numbers = equation[:-1]
    longest_original_number = max(map(len, original_numbers))
    numbers: list[int] = []
    
    for _ in range(longest_original_number):
        number = ''
        longest_number = max(map(len, original_numbers))
        
        for i, original_number in enumerate(original_numbers):
            if len(original_number) >= longest_number:
                number += original_number[-1]
                original_numbers[i] = original_number[:-1]

        numbers.append(int(number))
        
    return numbers
        
def calculateEquation(numbers: list[int], operation: str) -> int:
    res = 0
    if operation == '+':
        res = 0
        
        for number in numbers:
            res += number
            
    elif operation == '*':
        res = 1
        
        for number in numbers:
            res *= number
            
    return res

def findCorrectNumbersObsoleteTest():
    data = [['123', '45', '6', '*'], 
            ['328', '64', '98', '+'], 
            ['51', '387', '215', '*'], 
            ['64', '23', '313', '+']]
    
    expected = [[3, 25, 146], [8, 248, 369], [75, 181, 532], [3, 431, 623]]
    
    for entry, answer in zip(data, expected):
        assert findCorrectNumbersObsolete(entry) == answer

def findSolutionCorrect(data: str) -> int:
    lines = data.splitlines()
    numbers: list[str] = []
    operation = ''
    res = 0
    
    for i in range(len(lines[0])):
        number = ''
        empty = True
        
        for line in lines:
            char = line[i]
            
            if char in ['*', '+']:
                operation = char
                empty = False
                
            elif char != ' ':
                number += char
                empty = False
                
        if not empty:        
            numbers.append(number)
        else:
            res += calculateEquation(list(map(int, numbers)), operation)
            numbers = []
    
    return res + calculateEquation(list(map(int, numbers)), operation)       

if __name__ == '__main__':
    findCorrectNumbersObsoleteTest()
    answer = findSolutionCorrect(raw_data)
    print(answer)
        