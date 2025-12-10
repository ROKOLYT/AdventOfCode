import json
import re

with open('input.txt', 'r') as f:
    data = f.read()
    
def format_input(data: str) -> list[dict[str, list[int] | list[list[int]]]]:
    lines = data.splitlines()
    
    formatted_data:list[dict[str, list[int] | list[list[int]]]] = []
    
    for line in lines:
        light_indicators_raw:str = re.findall(r'\[(.*?)\]', line)[0]
        light_indicators:list[int] = format_indicator_lights(light_indicators_raw)
        
        buttons_raw:list[str] = re.findall(r'\((.*?)\)', line)
        buttons:list[list[int]] = [[int(x) for x in btn.split(',')] for btn in buttons_raw]
        
        joltage_raw = re.findall(r'\{(.*?)\}', line)[0]
        joltage:list[int] = [int(x) for x in joltage_raw.split(',')]
        
        formatted_data.append({
            'lights': light_indicators,
            'buttons': buttons,
            'joltage': joltage
        })
    return formatted_data
        

def format_indicator_lights(indicator_str: str) -> list[int]:
    lights:list[int] = []
    for c in indicator_str:
        if c == '.':
            lights.append(0)
        elif c == '#':
            lights.append(1)
    
    return lights

if __name__ == "__main__":
    formatted_data = format_input(data)
    with open('formatted_input.json', 'w') as f:
        json.dump(formatted_data, f, indent=4)