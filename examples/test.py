"""mapping"""
import os ##for directory
import sys
import pprint
# set the directory
sys.path.append(r"/Users/luho/Documents/GitHub")


# define a function
def add (a,b):
    
    s = a**2 + b**2

    return s


os.getcwd()
pprint.pprint(sys.path)
w = [1,2,3,4,5,6]
v =['z','a','b','a','b','e']
testData = ['a','b','g']


#import mainFunction as MF
import pandas as pd
from hongPy import mainFunction as MF

"""mapping"""
tt = MF.singleMapping(w, v, testData, dataframe=False)
mm = MF.multiMapping(w, v, testData, dataframe=False)


"""split and combine"""
s1 = ['a&b','c']
s2 = ['r1','r2']

ss = pd.DataFrame({'ss1':s1, 'ss2':s2})
nn = MF.splitAndCombine(ss['ss1'], ss['ss2'], sep0="&")

"""autoUpdate"""
df1 = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                    'B': ['A', 'B', 'C'] * 4,
                    'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2}
                   )

df2 = df1.iloc[[1,2]]
df2['C'] = ['good','good']


df1['C'] = MF.AutoUpdate(df2['C'], df2['A'], df1['C'], df1['A'])


##import the module from the code file
from hongPy.primitive import line
from hongPy.primitive import fill
line.hello()
fill.add(x=5,y=6)

# here we add 'from . import newprint' in the __init__.py
# thus we can directly use the followed code
from hongPy import formats
formats.newprint.testfun(x='hongzhong')
formats.newprint.mergeString(x='hello', y='hongzhong!')

from hongPy import primitive
primitive.fill.add(x=5, y=6)




