import re

pattern = re.compile(r'^([\d]{4,4})\-.*Friendly.*$')

with open("./results.csv", "r") as f:
    for line in f:
        res= re.match(pattern,line)
        if res:
            print(f'{res.group(1)}\n')

