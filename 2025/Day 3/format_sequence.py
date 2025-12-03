sequence = """
"""

import json
with open('sequence.json', 'w') as f:
    sequence = sequence.splitlines()
    json.dump(sequence, f)