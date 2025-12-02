import json
from tracemalloc import start
from typing import List

with open('dialseq.json', 'r') as file:
    dialseq_data = json.load(file)

def decodeSequence(dialseq: List[str]) -> int:
    dial = 50
    answer = 0
    
    for action in dialseq:
        direction = action[0]
        turns = int(action[1:])
        
        if direction == 'R':
            dial += turns
        else:
            dial -= turns
        
        dial %= 100
        if dial == 0:
            answer += 1
    
    return answer

def decodeSequenceSecure(dialseq: List[str]) -> int:
    dial = 50
    answer = 0
    
    for action in dialseq:
        direction = action[0]
        turns = int(action[1:])
        
        if direction == 'R':
            first_hit = 100 - dial
            
            if turns >= first_hit:
                answer += 1 + (turns - first_hit) // 100
            
            dial = (dial + turns) % 100
        else:
            first_hit = dial
            
            if first_hit == 0:
                first_hit = 100
                
            if turns >= first_hit:
                answer += 1 + (turns - first_hit) // 100
            
            dial = (dial - turns) % 100
    
    return answer

def testDecodeSequence():
    sequence = ['R50', 'L100', 'R50', 'L50', 'L500', 'R10', 'L20']
    assert decodeSequence(sequence) == 4
    
def testDecodeSequenceSecure():
    sequence = ['R50', 'L100', 'R50', 'L50', 'L500', 'R10', 'L20']
    assert decodeSequenceSecure(sequence) == 9

if __name__ == '__main__':
    testDecodeSequence()
    testDecodeSequenceSecure()
    
    answer = decodeSequence(dialseq_data)
    print(answer)
    
    secure_answer = decodeSequenceSecure(dialseq_data)
    print(secure_answer)
    