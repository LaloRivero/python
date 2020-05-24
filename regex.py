import re

pattern = re.compile(r'^([\d]{4})-\d{2}-\d{2},(.+),(.+),(\d+),(\d+),.*$')

f = open('results.csv', 'r')

for line in f:
    res = re.match(pattern, line)
    if res:
        total = int(res.group(4)) + int(res.group(5))
        if total >= 10:
            print(f'{res.group(2)} {res.group(4)} VS {res.group(5)} {res.group(3)}.')
            print(f'Total de goles: {total}, Fecha {res.group(1)}\n')
f.close()
