# -*- coding: utf-8 -*-
# -*- python 3 -*-
# -*- hongzhong Lu -*-
import os
import sys
import pprint
os.getcwd()
sys.path.append(r"/Users/luho/Documents/GitHub")
pprint.pprint(sys.path)
from graphics.primitive import line
from graphics.primitive import fill
line.hello()
fill.add(x=5,y=6)
