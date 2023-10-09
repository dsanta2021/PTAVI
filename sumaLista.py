from itertools import zip_longest
from operator import add

s1 = [1, 0, 8, 2, 10]
s2 = [3, 8, 1]

if len(s1) == len(s2):
    s3 = list(map(add, s1, s2))
else:
    s3 = list(sum(x) for x in zip_longest(s1, s2, fillvalue=0))

print(s3)