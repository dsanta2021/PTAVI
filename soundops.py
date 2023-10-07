from mysound import Sound
from operator import add
from itertools import zip_longest


def soundadd(s1: Sound, s2: Sound) -> Sound:
    s3 = Sound(max(s1.duration, s2.duration))

    if len(s1.buffer) == len(s2.buffer):
        s3.buffer = list(map(add, s1.buffer, s2.buffer))
    else:
        s3.buffer = list(sum(x) for x in zip_longest(s1.buffer,
                                                     s2.buffer, fillvalue=0))

    return s3
