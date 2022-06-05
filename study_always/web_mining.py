# import libraries
import urllib.request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd

def getAnnotationYMDB(metabolite):
    url0 = 'http://www.ymdb.ca/compounds/'
    url = url0 + metabolite
    try:
        response = urllib.request.urlopen(url)
    except HTTPError as e:
        return  None
    try:
        html = response.read()
        soup0 = BeautifulSoup(html,"lxml")
    #print(soup0.prettify())
        header = soup0.find_all('td')
    #print(header)
    #len(header)
        ss = [None] * (len(header))
        for i in range(len(header)):
            ss[i] = soup0.find_all('td')[i].get_text()

    ## obtain the index information of each ID
        chebi_index = ss.index("CHEBI ID") + 1
        HMDB_index = ss.index("HMDB ID") + 1
        Pubchem_index = ss.index("Pubchem Compound ID") + 1
        kegg_index = ss.index("Kegg ID") + 1

    ## creat dict
        results = {}
        results['chebi'] = ss[chebi_index]
        results['hmdb'] = ss[HMDB_index]
        results['pubchem'] = ss[Pubchem_index]
        results['kegg'] = ss[kegg_index]

        return(results)
    except AttributeError as e:
        return None


getAnnotationYMDB("YMDB02322")


# get the id information for each 30 metabolites
metaboliteYMDB = pd.read_excel('ymdb_allMetabolite_yeast.xlsx')
metaboliteYMDB['chebiID_old'] = metaboliteYMDB['chebiID_old'].str.replace(':','_')
metabolite_noID = metaboliteYMDB[metaboliteYMDB['chebiID_old'].isnull()]


# batch process2
ss = len(metaboliteYMDB.iloc[1855:2023,0])
CHEBI = [None] * ss
HMDB =[None] * ss
PUBCHEM =[None] * ss
KEGG =[None] * ss

metList = metaboliteYMDB.iloc[1855:2023,0].tolist()
for i,x in enumerate(metList):
    print(i)
    result = getAnnotationYMDB(x)
    CHEBI[i] = result['chebi']
    HMDB[i] = result['hmdb']
    PUBCHEM[i] = result['pubchem']
    KEGG[i] = result['kegg']


#change the data into dataframe format
YMDB ={}
YMDB['ymdbID'] = metList
YMDB['CHEBI'] = CHEBI
YMDB['HMDB'] = HMDB
YMDB['PUBCHEM'] = PUBCHEM
YMDB['KEGG'] = KEGG
YMDB0 = pd.DataFrame(YMDB)

writer = pd.ExcelWriter('ymdbAnnotation3.xlsx')
YMDB0.to_excel(writer,'Sheet1')
writer.save()




## example 1
import re

#待分析字符串
html_doc = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
<p class="title aq">
    <b>
        The Dormouse's story
    </b>
</p>

<p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
    and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.
</p>

<p class="story">...</p>
"""


# html字符串创建BeautifulSoup对象
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

#输出第一个 title 标签
print (soup.title)

#输出第一个 title 标签的标签名称
print (soup.title.name)

#输出第一个 title 标签的包含内容
print (soup.title.string)

#输出第一个 title 标签的父标签的标签名称
print (soup.title.parent.name)

#输出第一个  p 标签
print (soup.p)

#输出第一个  p 标签的 class 属性内容
print (soup.p['class'])

#输出第一个  a 标签的  href 属性内容
print (soup.a['href'])
'''
soup的属性可以被添加,删除或修改. 再说一次, soup的属性操作方法与字典一样
'''
#修改第一个 a 标签的href属性为 http://www.baidu.com/
soup.a['href'] = 'http://www.baidu.com/'

#给第一个 a 标签添加 name 属性
soup.a['name'] = u'百度'

#删除第一个 a 标签的 class 属性为
del soup.a['class']

##输出第一个  p 标签的所有子节点
print (soup.p.contents)

#输出第一个  a 标签
print (soup.a)

#输出所有的  a 标签，以列表形式显示
print (soup.find_all('a'))

#输出第一个 id 属性等于  link3 的  a 标签
print (soup.find(id="link3"))

#获取所有文字内容
print(soup.get_text())

#输出第一个  a 标签的所有属性信息
print (soup.a.attrs)


for link in soup.find_all('a'):
    #获取 link 的  href 属性内容
    print(link.get('href'))

#对soup.p的子节点进行循环输出
for child in soup.p.children:
    print(child)

#正则匹配，名字中带有b的标签
for tag in soup.find_all(re.compile("b")):
    print(tag.name)





####example 2
url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'

page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

print(soup.prettify())

soup.find_all('p')

soup.find_all('p')[2].get_text()



snp_122 = pd.read_excel('122_strain.xls')


####example3
# import libraries
import urllib2
from bs4 import BeautifulSoup
# specify the url
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'
# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(quote_page)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'name'}