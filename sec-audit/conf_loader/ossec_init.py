__author__ = 'sabin'

import pprint
def load_conf (file_path):
    # Load file content to buffer
    with open(file_path, 'rU') as f:
        content = f.read()
    confs = {}
    for line in content.splitlines():
        if len (line) > 0 and line[0] != '#':
            position = line.index ('=')
            confs[line[:position]] = line[position + 1:]
    return confs
