dial_sequence = r""""""

import json
with open('dialseq.json', 'w') as f:
    json.dump(dial_sequence.strip().split('\n'), f)