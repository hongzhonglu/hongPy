
############################## how to install python package
# using pycharm
# using conda
# using python -m pip install SomePackage


################################ package install and search
import study_numpy as np
import pandas as pd
import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)

################################### I/O
"""read and save"""
dataset2 = pd.read_excel('dataset2.xlsx')
writer = pd.ExcelWriter('proteinStructure.xlsx')
newResults.to_excel(writer,'Sheet1')
writer.save()

#UserInfo.tsv
user_info=pd.read_csv('../input/UserInfo.tsv',delimiter='\t',encoding='utf-8')
print(list(user_info.columns.values)) #file header
print(user_info.tail(35)) #last N rows

#Location.tsv
location=pd.read_csv('../input/Location.tsv',delimiter='\t',encoding='utf-8')
print(list(location.columns.values)) #file header
print(location.tail(35)) #last N rows

#category.tsv
category=pd.read_csv('../input/Category.tsv',delimiter='\t',encoding='utf-8')
print(list(category.columns.values)) #file header
print(category.tail(5)) #last N rows

#big csv file...
search_info = pd.read_csv('../input/SearchInfo.tsv',delimiter='\t',nrows=20,encoding='utf-8-sig')#skiprows=1000000,
print(list(search_info.columns.values)) #file header
print(search_info[[search_info.columns[0],search_info.columns[1],search_info.columns[2]]])


# sum each column of pandas
df.loc['sum'] = df.apply(lambda x: x.sum()) # sum for each column, the result put in row with name 'sum'


########################################## data structure
import study_numpy as np
import pandas as pd

'''list'''
numbers = [100,34,678]
numbers? # ?check the type ??could show the source code of function


len(numbers)
max(numbers)
x = [4,6,2,1,7,9]
x.sort()


'''list method'''
a = 'is'
b = 'nice'
my_list = ['my', 'list', a, b, a, b]
my_list.index(a)
my_list.count(a)
my_list.append('!')
my_list.remove('!')
del(my_list[0:1])
my_list.reverse()
my_list.extend('!')
my_list.pop(-1)
my_list.insert(0,'!')
my_list.sort()

all([True, 1, { 3 }]) # True
all([True, 1, {}]) # False, {} is falsy
any([True, 1, {}]) # True, True is truthy
all([]) # True, no falsy elements in the list
any([])

#get index of element
['a', 'b'].index('b')
indices = [i for i, x in enumerate(my_list) if x == "whatever"]

#calculate the frequency
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)


def removeDuplicated(items):
    '''
    this function is used to remove the duplicated while keep the order
    :param items: a list
    :return: a list without duplicated value while keep the original order
    example
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    '''
    seen = set()
    for item in items:
        if item not in seen:
        yield item
        seen.add(item)

# usage: list(removeDuplicated(a))
# get the unique element of a list
a = [1, 5, 2, 1, 9, 1, 5, 10]
list(set(a))



'''dict'''
d1 = {'a' : 0., 'b' : 2., 'c' : 2.} #字典
d2 = dict(b=2, c=3) #b, c as the key
d1.values()
d1.items()
d1.keys()


d1 & d2
v1 = d1.items() #return the list
v2 = d2.items()
v1 & v2
v1 - v2
for i in d1.items():
    print(i)


from collections import defaultdict, OrderedDict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)

d= OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
for k, v in d.items(): print(k,v)


'''update d1 using d2'''
d1 = {'one' : pd.Series([1., 2., 3.]), 'two' : pd.Series([1., 2., 3., 4.,5., 6])}
d2 = {'one': pd.Series([2,3,4,5])}
d1.update(d2)


'''construct dict'''
x = [4,6,2,1,7,9]
y =['a','b','c','d']
reaction_status = {r_id: [] for r_id in x} # construct null dict
print(reaction_status)
all_scores = dict(zip(y, x)) # construct specific dict


'''dict to dataframe'''
dd = {'A': pd.Series([2,3,4,5]),
      'B':pd.Series([6,7,8,9])}

df = pd.DataFrame(dd)
df_dict = dict(zip(df.A, df.B))


''''dataframe to dict'''
df = pd.DataFrame([["Women", "Slip on", 7, "Black", "Clarks"], ["Women", "Slip on", 8, "Brown", "Clarcks"], ["Women", "Slip on", 7, "Blue", "Clarks"]], columns= ["Category", "Sub Category", "Size", "Color", "Brand"])
new_dict = {k:list(df[k].unique()) for k in df.columns}
new_dict2 = {k:list(df[k]) for k in df.columns}
df_new = pd.DataFrame(new_dict2)

#Finding Commonalities in Two Dictionaries
a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}
# Find keys in common
a.keys() & b.keys() # { 'x', 'y' }
# Find keys in a that are not in b
a.keys() - b.keys() # { 'z' }
# Find (key,value) pairs in common
a.items() & b.items() # { ('y', 2) }
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}

#Mapping Keys to Multiple Values in a Dictionary
d = {
'a' : [1, 2, 3],
'b' : [4, 5]
}
e = {
'a' : {1, 2, 3},
'b' : {4, 5}
}

from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)



'''set'''
#good for 集合运算
'c' in set('abcd')
set('abc') == set('ab')

s = {'pf','pr'}
type(s)

x = {'foo', 'bar', 'baz', 'foo', 'qux'}
# Boolean
x = set()
bool(x)
x or 1
x and 1
# Don’t forget that set elements must be immutable. For example, a tuple may be included in a set, but a list cannot be contained in a set
x = {42, 'foo', (1, 2, 3), 3.14159}
# Operating on a Set
x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
x1 | x2
x1.union(x2)
x1.intersection(x2)
x1 & x2
x1.difference(x2)
x1-x2


############################################ for looping
""" find the set of girl and boy names with the first same letter"""
girls = ['alice','bernice','clarice']
boys = ['chris','arnold','bob']
letterGirls ={}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])

coef = 10
for i in range(100):
    print(10*range(100)[-i-1])

for idx, boy in enumerate(boys):
    print ('#%d: %s' % (idx, boy))

'''使用列表推导，你就可以让代码简化很多'''
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
even_squares = [x ** 2 for x in nums if x % 2 == 0]

'''循环Loops：在字典中，用键来迭代更加容易'''
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print ('A %s has %d legs' % (animal, legs))
for key in d:
	print(d[key])


'''如果你想要访问键和对应的值，那就使用iteritems (python2.7)方法'''
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print ('A %s has %d legs' % (animal, legs))

'''字典推导Dictionary comprehensions：和列表推导类似，但是允许你方便地构建字典'''
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print (even_num_to_square)


'''循环Loops：在集合中循环的语法和在列表中一样，但是集合是无序的，所以你在访问集合的元素的时候，不能做关于顺序的假设'''
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print ('#%d: %s' % (idx + 1, animal))


'''集合推导Set comprehensions：和字典推导一样，可以很方便地构建集合'''
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print (nums)  # Prints "set([0, 1, 2, 3, 4, 5])"

'''元组是一个值的有序列表（不可改变）。从很多方面来说，元组和列表都很相似。和列表最重要的不同在于，元组可以在字典中用作键，还可以作为集合的元素，而列表不行。例子如下'''
d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
print (d)

'''生成器'''
g = (x * x for x in range(10))
for n in g:
    print(n)





########################################### files 
input_path = 'path_1'
import os
prev_path = os.getcwd()
os.chdir(input_path)
dir_files = os.listdir(input_path)
for i in dir_files:
    #Define EC number and variable name:
    sep_pos   = i.find('_')
    ec_number = i[0:sep_pos]
    var_name  = i[sep_pos+1:len(i)-4]





############################################## function
def recv(maxsize, *, block):
    'Receives a message'
    pass

recv(1024, True) # TypeError
recv(1024, block=True) # Ok


def fibs(num):
    result =[0,1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

fibs(10)

storage ={}

def init(data):
    data['first'] ={}
    data['middle'] ={}
    data['last'] = {}

def lookup(data,label,name):
    return data[label].get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) ==2:
        names.insert(1,'')
    labels = 'first', 'middle','last'
    for label, name in zip(labels,names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


MyNames ={}
init(MyNames)
print(MyNames)

store(MyNames,'Magnus Lie Hetland')

lookup(MyNames,'middle','Lie')

store(MyNames,'Robin Hood')

store(MyNames,'Robin Locksley')

'''递归'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(10)


'''adding check types'''
def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 0
    elif n== 1:
        return 1
    else:
        return n * factorial(n-1)

factorial(10)

# try...except
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()


'''lambda'''
double = lambda x: x*2
print(double(5))

'''map and filter'''
seq =[1,2,3,4,5]
result = list(map(lambda var: var*2, seq))
print(result)
result0 = list(filter(lambda x: x>2, seq))
print(result0)

'''sorted'''
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(students, key=lambda s: s[2])  # 按年龄排序
sorted(students, key=lambda s: s[2], reverse=True)  # 按降序

#This case is especially useful for tracking line numbers in files should you want to use
#a line number in an error message:
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))




########################################class and object
# example
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

b = Pair(1,2)
b.__repr__()
b.__str__()


# example
class Person:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print("Hello, world! I'm %s" %self.name)

foo = Person()
foo.setName('L S') ## self is very important
foo.name
foo.greet()
foo.getName()

# example
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

s = SPAMFilter()
s.init()
s.filter(['SPAM','eggs','SPAM'])

# example
'''构造方法 + super'''
__metaclass__ = type
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaah...')
            self.hungry = False
        else:
            print('No, thanks!')
class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squak!'
    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()
sb.eat()

# example
'''class application'''
class myDict(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

## example
myd = myDict()
myd.add('apples',6)
myd.add('bananas',3)
s1 = ['a','b','c']
s2 = [1,2,3,4]
for i in range(len(s1)):
    myd.add(s1[i],s2[i])




'''setter'''
class Timer:

  def __init__(self, value = 0.0):
    self._time = value
    self._unit = 's'

  # 使用装饰器的时候，需要注意：
  # 1. 装饰器名，函数名需要一直
  # 2. property需要先声明，再写setter，顺序不能倒过来
  @property
  def time(self):
    return str(self._time) + ' ' + self._unit

  @time.setter
  def time(self, value):
    if(value < 0):
      raise ValueError('Time cannot be negetive.')
    self._time = value

t = Timer()
t.time = 1.0
print(t.time)

# example
class Point:
""" point definition"""
print(Point)
blank = Point()
blank
blank.x = 3
blank.y = 4
blank.z = 5
import math
distance = math.sqrt(blank.x**2  + blank.y**2)
distance

class Rectangle:
"""represent rectangle"""

box = Rectangle()
box.width = 100
box.height = 200
box.corner = Point()
box.corner.x = 0
box.corner.y = 0

class Time:
    """Represent the time of day"""
time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def add_time(t1,t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

# example

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return ('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(self, seconds):
        minutes, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(minutes, 60)
        return self

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()

    def __radd__(self,other):
        return self.__add__(other)


start = Time()
start.hour = 9
start.minute = 45
start.second = 00

end = Time()
end.hour = 10
end.minute = 45
end.second = 00

end.is_after(start)

time = Time()
time.print_time()
time = Time(9,45)
print(time)

start = Time(9,45)
duration = Time(1,35)
print(start + duration)
print(start + 1337)
print(1337 + start)

t1 = Time(7,43)
t2 = Time(7,41)
t3 = Time(7,37)
total = sum([t1,t2])

#inherity
class Card:
    """represents a standard playing card"""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    suit_names = ['Clubs','Diamonds','Hearts','Spades']
    rank_names = [None, 'Ace', '2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    def __str__(self):
        return ('%s of %s' %(Card.rank_names[self.rank],
                             Card.suit_names[self.suit]))
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

card1 = Card(2,11)
print(card1)

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    #print
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

deck = Deck()
print(deck)




class DictList(list):
    """A combined dict and list
    This object behaves like a list, but has the O(1) speed
    benefits of a dict when looking up elements by their id.
    """

    def __init__(self, *args):
        """Instantiate a combined dict and list.
        Parameters
        ----------
        args : iterable
            iterable as single argument to create new DictList from

        """
        if len(args) > 2:
            raise TypeError("takes at most 1 argument (%d given)" % len(args))
        super(DictList, self).__init__(self)
        self._dict = {}
        if len(args) == 1:
            other = args[0]
            if isinstance(other, DictList):
                list.extend(self, other)
                self._dict = other._dict.copy()
            else:
                self.extend(other)


ss = DictList()
ss = DictList(['A','B','C'])


def dictlist(*args):
    ss = {}
    if len(args) > 2:
        raise TypeError("takes at most 1 argument (%d given)" % len(args))
    if len(args) == 1:
        other = args[0]
        if isinstance(other, dict):
            ss = list.extend(other)
             = other._dict.copy()
        else:
            self.extend(other)




# an example
class DHT:
   def __init__(self, data={}):
      self.data = data
      self.data['one'] = '1'
      self.data['two'] = '2'
      self.data['three'] = '3'
   def showData(self):
      print(self.data)


DHT().showData()
# Build the class first
dht = DHT({'six':6,'seven':'7'})
# The call whatever method you want (In our case only 1 method available)
dht.showData()






#################################### web technology
import os    ##for directory
print (os.getcwd()) #obtain the present directory
s = os.getcwd()
s
os.chdir('/Users/luho')
os.chdir('/Users/luho/python learning')    

## web
from urllib import request
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc)


text = urllib.request.urlopen("http://www.ymdb.ca/compounds/YMDB00286")
response = text.read()
soup = BeautifulSoup(response)
print(soup)





############################## 正则表达式工具 and strings
a ='foo'
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')


pattern = re.compile(r'\d+')
print (re.split(pattern,'one1two2three3four4'))


'''txt processing'''
TXTtemp = open("fishandsheephistory.txt","r+")
txtbuffer=TXTtemp.read()
#i=0
oldlist=['']
newlist=['']
#for txtchar in txtbuffer:
#   oldlist.append(txtchar)
#   i=i+1
oldlist=list(txtbuffer)
for index in range(len(txtbuffer)):
    if oldlist[index]=="《":
        for j in range(30):
            if oldlist[index+j]=="》":
                newlist.append("》")
                newlist.append("\n")
                j=0
                break
            newlist.append(oldlist[index+j])
print(newlist)
strlist="".join(newlist)
txtnew=open("newtxt.txt","w")
txtnew.write(strlist)
txtnew.close()
TXTtemp.close()

'''python提取关键字所在行的后边几行'''
'''cat 1.txt

a1 =

  (DESCRIPTION =

    (ADDRESS = (PROTOCOL = TCP)(HOST = oracle)(PORT = 1000))

    (CONNECT_DATA =

      (SERVER = aaa)

      (SERVICE_NAME = aaa)

a2 =

  (DESCRIPTION =

    (ADDRESS = (PROTOCOL = TCP)(HOST = bbb-vip)(PORT = 1000))

    (CONNECT_DATA =

      (SERVER = ccc)

      (SERVICE_NAME = bbb)

a3 =

  (DESCRIPTION =

    (ADDRESS = (PROTOCOL = TCP)(HOST = ccc-vip)(PORT = 1000))

    (CONNECT_DATA =

      (SERVER = ccc)

      (SID = ccc)
#!/usr/bin/env python
# -*- coding: utf-8 -*-'''

b = ['a1', 'a2']
with open('1.txt', 'r') as f:
    a = []
    lines = f.readlines()
    print(lines[0])
    for x in lines:
        if x.startswith('a'):
            a.extend([x.strip().split()[0], lines.index(x),])
    for i in b[:-1]:
        if i in a:
            c = a.index(i)
            print (''.join(lines[a[c+1]:a[c+3]]))
    if b[-1] == a[-2]:
        print(''.join(lines[a[int(a.index(b[-1]) + 1)]:])
    else:
        print(''.join(lines[a[int(a.index(b[-1])) + 1]:a[int(a.index(b[-1])) + 3]])



'''string manipulation in pandas'''
val = 'a,b, guido'
pieces = [x.strip() for x in val.split(',')]
'guido' in val
val.index(',')
val.index(':')
val.find(',')
val.find(':')


'''string methods'''
my_string = 'thisStringIsAwesomew '
'm' in my_string
my_string.upper()
my_string.lower()
my_string.count('w')
my_string.replace('e','i')
my_string.strip()


'''An Improved String Formatting Syntax (Guide)'''
name = "Eric"
"Hello, %s." % name  # method1
name = "Eric"
age = 74
"Hello, %s. You are %s." % (name, age)  # method2
"Hello, {}. You are {}.".format(name, age)
'Hello, Eric. You are 74.'
f"Hello, {name}. You are {age}."  # method3



# packages uage
############################## #pandas

'''pd.Series'''
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
ser2[-1]
s  = pd.Series(['aa-123', 'ff-ds-ds', 'zzz-42', 'xx’])
s.str.split("-", 1, expand=True)



'''add new row and new column'''

df=DataFrame(np.arange(16).reshape((4,4)),index=['a','b','c','d'],columns=['one','two','three','four']) 
df.loc['new_raw'] = '3' #add new row
df['new_colum'] = '3' # add new column
df.set_value('a', 'one', 10) #add a single value


'''construct the dataframe'''
df = pd.DataFrame( {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20130101',periods = 6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df.head
df.tail(3)
df.index
df.columns
df.values
df.describe()
df.T
df.sort_index(axis=1, ascending=False)
df.sort_values(by='B')
df['A']
df[0:3]
df.loc[dates[0]]
df
#selection by position
df.iloc[3]
df[df > 0]

df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2[df2['E'].isin(['two','four'])]


df.at[dates[0],'A'] = 0
df.iat[0,1] = 0

df1 = df.reindex(index=datas[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
df1.dropna(how='any')
df1.fillna(value=5)
pd.isna(df1)


s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
df.sub(s, axis='index')


""" dataframe merge"""
frames = [newData,newData1] # newData is dataframe
result = pd.concat(frames)


"""change dataframe into dict"""
d = {0: [50, 45, 0, 0],
     1: [53, 48, 0, 0],
     2: [56, 53, 0, 0],
     3: [54, 49, 0, 0],
     4: [53, 48, 0, 0],
     5: [50, 45, 0, 0]}

pd.DataFrame.from_items(d.items(),
                            orient='index',
                            columns=['A','B','C','D'])


"""combine two column in two dataframe"""
df['c'] = df['a'].str.cat(df['b'], sep=',')


"""filter row"""
df['A'] # choose the column A
df.A # choose the column A
df[df.A > 0]


'''How to get the items of series A not present in series B?'''
ser1 = pd.Series([1, 2, 3, 4, 5,1])
ser2 = pd.Series([4, 5, 6, 7, 8])
# Solution
index = ser1.isin([None])
index
ser1[index]
ser1[ser1.isin(ser2)]
ser1[~ser1.isin(ser2)]


'''How to convert the first character of each element in a series to uppercase?'''
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
# Solution 1
ser.map(lambda x: x.title())

# Solution 2
ser.map(lambda x: x[0].upper() + x[1:])

# Solution 3
pd.Series([i.title() for i in ser])

'''How to calculate the number of characters in each word in a series?'''
# Input
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
# Solution
ser.map(lambda x: len(x))
pd.Series([len(x) for x in ser])

''' How to filter words that contain at least 2 vowels from a series?'''
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
from collections import Counter
mask = ser.map(lambda x: sum([Counter(x.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
ser[mask]


'''How to filter valid emails from a series?'''
# Input
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])

# Solution 1 (as series of strings)
import re
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
emails[mask]

# Solution 2 (as series of list)
emails.str.findall(pattern, flags=re.IGNORECASE)

# Solution 3 (as list)
[x[0] for x in [re.findall(pattern, email) for email in emails] if len(x) > 0]



'''merge two dataframe'''
# Input
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'fruit': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})

result = pd.merge(df1, df2, on='fruit')



'''How to remove rows from a dataframe that are present in another dataframe?'''
#Difficulty Level: L3
#From df1, remove the rows that are present in df2. All three columns must be the same.'''
# Input
df1 = pd.DataFrame({'fruit': ['apple', 'orange', 'banana'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.arange(9)})

df2 = pd.DataFrame({'fruit': ['apple', 'orange', 'pine'] * 2,
                    'weight': ['high', 'medium'] * 3,
                    'price': np.arange(6)})

# Solution
print(df1[~df1.isin(df2).all(1)])





'''.loc and loc '''
import pandas as pd
data = [[1,2,3],[4,5,6]]
index = ['a','d']
columns=['a','b','c']
df = pd.DataFrame(data=data, index=index, columns=columns)
df.loc['a']
df.loc['a':]
df.iloc[0]




'''python里使用iterrows()对dataframe进行遍历'''
import  pandas as pd
import study_numpy as np
# Input
df = pd.DataFrame({'fruit1': np.random.choice(['apple', 'orange', 'banana'], 10),
                    'fruit2': np.random.choice(['apple', 'orange', 'banana'], 10)})
for index,row in df.iterrows():
  print (index)
  print (row)


'''row and column'''
df.drop('Row A', axis =1)
df.drop('column A', axis = 0)


'''apply function for dataFrame'''
df = pd.DataFrame([[4,9],]*3, columns=['A','B'])
df.apply(np.sqrt)
df.apply(np.sum, axis=0) #for each column
df.apply(np.sum, axis=1) #for each row


'''describe'''
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
obj.describe()


'''get_dummies'''
df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],'data1': range(6)})
pd.get_dummies(df['key'])

'''pd.cut'''
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
cats.codes
cats.categories
pd.value_counts(cats)

np.random.seed(12345)
values = np.random.rand(10)
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
pd.get_dummies(pd.cut(values, bins))



'''pandas description'''
s1 =[1,2,3,4]
s2 =[4,5,6,7]
s3 =[7,8,9,10]

dataset1 = pd.DataFrame({'n1':s1,
                         'n2':s2,
                         'n3':s3})
feature = dataset1.loc[:, dataset1.columns != 'n1']
target = dataset1.loc[:,dataset1.columns == 'n1']

dataset1.iloc[:,0:2].columns.values
dataset1.iloc[:,1:3].describe()
dataset1.n1.mean()
dataset1.n1.std()

'''save result'''
outname = '../Dataset/kmERG1_kmNCP1_features.csv'
df.to_csv(outname)


'''pandas loop'''
# it turns out there’s a better way: df.itertuples().
times_r = []
times_t = []
n = 1000
for i in range(250):
    # Iterate using iterrows()
    begin = time.time()
    data = {}
    for row in df[:sz].iterrows():
        row = row[1]
        key = row.firstName[:2]
        if key not in data:
            data[key] = [0]
        data[key][0] = data[key][0] + 1
    end = time.time()
    times_r.append({'begin': now, 'end': end, 'diff': end - begin})

    # Iterate using itertuples()
    begin = time.time()
    data = {}
    for row in df[:sz].itertuples():
        key = row.firstName[:2]
        if key not in data:
            data[key] = [0]
        data[key][0] = data[key][0] + 1
    end = time.time()
    times_t.append({'begin': now, 'end': end, 'diff': end - begin})




########################################### numpy
import study_numpy as np
import pandas as pd

'''arange and linspace'''
np.arange(3,7,2)
b = np.arange(4)
np.linspace(2.0,3.0, num=5)

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr % 2 ==1] = -1

'''Get the positions where elements of a and b match'''
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
a*b #just like R
np.where(a == b)
np.where(a == 2)
a[np.where(a == 2)]


'''get the unique items and the counts'''
np.random.seed(100)
arr_rand = np.random.randint(0, 10, size=10)
uniqs, counts = np.unique(arr_rand, return_counts=True)
summary = pd.DataFrame({'unique_item': uniqs,
                        'counts':counts})

'''get the position'''
# Create an array
import study_numpy as np
arr_rand = np.array([8, 8, 3, 7, 7, 0, 4, 2, 5, 2])
print("Array: ", arr_rand)

# Positions where value > 5
index_gt5 = np.where(arr_rand > 5)
print("Positions where value > 5: ", index_gt5)


'''vectorize – Make a scalar function work on vectors'''
# Define a scalar function
def foo(x):
    if x % 2 == 1:
        return x**2
    else:
        return x/2
# Vectorize foo(). Make it work on vectors.
foo_v = np.vectorize(foo, otypes=[float])

print('x = [10, 11, 12] returns ', foo_v([10, 11, 12]))
print('x = [[10, 11, 12], [1, 2, 3]] returns ', foo_v([[10, 11, 12], [1, 2, 3]]))

'''good function from numpy'''
import study_numpy as np
values = np.array([6,0,0,3,2,5,6])
target = [2,3,7,8,0]
ss = np.in1d(values, target)
values[ss]
ss = np.in1d(values, 6)



x = values
y = [2,3,6]
np.unique(x)
np.intersect1d(x,y)
np.union1d(x, y)
np.setdiff1d(x, y)
np.setxor1d(x, y)


a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# Select row 1
a[1]
array([5, 6, 7, 8])
# Select column 1
a[:,1]
# Select a subregion and change it
a[1:3, 1:3]
np.where(a < 10, a, 10)
np.isnan #only for number



# biopython
import Bio
from Bio.Seq import Seq

'''create a sequence object'''
my_seq = Seq('CATGTAGACTAG')

# bioservices
import bioservices
from bioservices import PDB
s = PDB()
res = s.get_file("1FBV", "pdb")

s = PDB()
s.get_ligands("4HHB")


##itertools

items = ['a', 'b', 'c']
from itertools import permutations

for p in permutations(items):
    print(p)

for p in permutations(items, 2):
    print(p)

##collections
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
items = [1, 2, [3, 4, [5, 6], 7], 8]
# Produces 1 2 3 4 5 6 7 8
for x in flatten(items):
print(x)

# gurobi install
# cd / Library / gurobi810 / mac64 /  # the directory for the gurobi install
# python3 setup.py install


'''
regular expression
'''
import re
s = "12abc345ab"
m = re.match(r"\d+", s)
m.group()
m.span()
m = re.match(r"\d{3,}", s)
m = re.search(r"\d{3,}", s)
ms = re.findall(r"\d+", s)

m = re.match(r"(\d+)(?P<letter>[abc]+)", s)
m.group()

re.findall(r"[a-z]+", "%123Abc%45xyz&")


# split
re.split(r"\W", "abc,123,x")
re.split(r"(\W)", "abc,123,x")
re.sub(r"[a-z]+", "*", "abc,123,x")



# strip
# Whitespace stripping
s = ' hello world \n'
s.strip()
s.lstrip() #left
s.rstrip() #right

# Character stripping
t = '-----hello====='
t.lstrip('-') # remove '-' in the left
t.strip('-=') # remove '-' and '='

# multiple line pattern
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
... multiline comment */
... '''
comment.findall(text1)
comment.findall(text2)
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)

# Specifying a Regular Expression for the Shortest
# Match
str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1)
text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2)
str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)

# search and replace
text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

# Matching and Searching for Text Patterns
text = 'yeah, but no, but yeah, but no, but yeah'
text.startswith('yeah')
text.endswith('no')
text.find('no')


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

# split
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
re.split(r'[;,\s]\s*', line)
line.split(' ')


# f-Strings
age = 25
name = 'Jeremy'
print(f'My name is {name}, and I am {age}')

# run python from a file
exec(open("filename.py").read())


# for NaN in a list
# using NaN is not np.nan to remove it


import json
import pandas as pd
with open('/Users/luho/PycharmProjects/study_always/data/878HGTs.json') as f:
  data = json.load(f)
OG =[]
for x in data:
    print(x["ortholog"])
    OG.append(x["ortholog"])

OG_with_HGT = pd.DataFrame({"OG": OG})
OG_with_HGT.to_csv("/Users/luho/PycharmProjects/study_always/data/OG_with_HGT_cell.csv")




import numpy as np
np.arange(10)
arr = np.arange(10, dtype=float).reshape((2, 5))
arr2 = arr[:, 1:4]
arr2[0, 0] = 33

nums = np.arange(5)
nums * 10



# change string into variable name
eval('ecYeast.reactions.prot_Q0045.flux_expression + ecYeast.reactions.prot_Q0080.flux_expression')