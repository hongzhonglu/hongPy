# -*- coding: utf-8 -*-
# -*- python 3 -*-
# -*- hongzhong Lu -*-
def testfun(x):
    print(x+'!')

def mergeString(x,y):
    print(x+y)

# Only export 'testfun' and 'mergeString'
__all__ = ['testfun', 'mergeString']