
from trial import *

s=h()

def showone(one):
    for item in s:
        name=item['name'].lower()
        if name==one.lower():
            k=item
            print(k)
    return k