from collections import defaultdict
count = defaultdict(lambda :0)

with open("level3.dat") as f:
    for line in f:
        for c in line:
            count[c] += 1

for c in count:
    print c, count[c]
