import json
import itertools

with open('formatted_input.json', 'r') as f:
    data = json.load(f)

def findSolution(data: list[dict[str, list[int] | list[list[int]]]]) -> int:
    result = 0
    
    for entry in data:
        lights: list[int] = entry['lights']  # type: ignore
        buttons: list[list[int]] = entry['buttons'] # type: ignore
        
        result += findMinPresses(lights, buttons)
    
    return result
        
def findMinPresses(lights: list[int], buttons: list[list[int]]) -> int:
    lights_state = [0 for _ in range(len(lights))]
    n = 1
    
    while lights_state != lights:
        for combination in itertools.product(buttons, repeat=n):
            lights_state = [0 for _ in range(len(lights))]
            
            for button in combination:
                for switch in button:
                    lights_state[switch] = (lights_state[switch] + 1) % 2
                    
            if lights_state == lights:
                return n
        
        n += 1
    return n

if __name__ == '__main__':
    answer = findSolution(data)
    print(answer)
            
    