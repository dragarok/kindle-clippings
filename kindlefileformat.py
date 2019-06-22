import os
import re

with open("/home/light/clippings.txt", "r") as clippings:
    content = clippings.read()

r = re.compile(r'[\d]+:[\d]+:[\d]+[\S]')


hello = [i for i in r.findall(content) if len(i) == 9]

for i in hello:
    content = content.replace(i,i[:-1]+"\n\n" + i[-1])

with open("/home/light/my-clippings.txt", "w") as clipping:
    clipping.write(content)




