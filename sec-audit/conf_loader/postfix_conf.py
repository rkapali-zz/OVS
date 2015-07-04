
import pprint


def load_conf (file_path):
    # Load file content to buffer
    with open(file_path, 'rU') as f:
        content = f.read ()
    content = content.replace ("\\\n", "")

    confs = {}
    for line in content.splitlines():
        if len (line) > 0 and line[0] != '#':
            position = line.index ('=')
            confs[line[:position]] = line[position + 1:]
    return confs

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(load_conf('sample_postfix_main.cf'))
    
