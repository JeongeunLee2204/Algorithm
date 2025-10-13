#20251013
#3447 버그왕

import sys

for line in sys.stdin: #input 대신 사용
    line = line.rstrip('\n')
    while 'BUG' in line:
        line = line.replace('BUG', '')
    print(line)
