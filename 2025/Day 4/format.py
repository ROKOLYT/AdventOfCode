from typing import List
import json

papers = r""""""

def splitString(s: str) -> List[str]:
    return [s[i:i+1] for i in range(len(s))]

def formatInput(input: str) -> List[List[str]]:
    lines = input.strip().split('\n')
    return [splitString(line) for line in lines]

if __name__ == "__main__":
    formatted = formatInput(papers)
    with open('papers.json', 'w') as f:
        json.dump(formatted, f, indent=4)