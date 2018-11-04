# -*- coding: utf-8 -*-
# -*- python 3 -*-
# -*- hongzhong Lu -*-


# Import packages
import re
import numpy as np
import pandas as pd
import os    ##for directory
import sys
import pprint


def splitAndCombine(gene, rxn, sep0, moveDuplicate=False):
    ## one rxn has several genes, this function was used to splite the genes
    ## used for the dataframe data

    gene = gene.fillna('NA')  # fill the NaN with 'NA'
    gene0 = gene.tolist()
    rxn0 = rxn.tolist()
    s1 = list()
    s2 = list()
    for i in range(len(gene0)):
        s1 = s1 + [rxn0[i]] * len(gene0[i].split(sep0))
        s2 = s2 + gene0[i].split(sep0)
    df0 = pd.DataFrame({'V1': s1,
                        'V2': s2}
                       )
    if moveDuplicate == True:
        df00 = df0.drop_duplicates()
    else:
        df00 = df0
    return df00



def getCompartment(rxn):
    """
    This function is used to obtain the compartment information from reaction of yeastGEM
    :param rxn:  example acetyl-CoA[m] + L-glutamate[m]  -> coenzyme A[m] + H+[m] + N-acetyl-L-glutamate[m]'
    :return:
    """
    cp1 = ['[c]','[ce]','[e]','[er]','[erm]','[g]','[gm]','[lp]','[m]','[mm]','[n]','[p]','[v]','[vm]']
    cp2 = ['cytoplasm','cell envelope','extracellular','endoplasmic reticulum','endoplasmic reticulum membrane','Golgi','Golgi membrane','lipid particle',
             'mitochondrion','mitochondrial membrane','nucleus','peroxisome','vacuole','vacuolar membrane']


    cp = [None]*len(cp1)
    for i in range(len(cp1)):
       if cp1[i] in rxn:
         cp[i] = cp2[i]
       else:
          cp[i] = None
    cp1 = [x for i,x in enumerate(cp) if x is not None]
    cp0 = ';'.join(str(e) for e in cp1)
    return cp0



def getCommonCompartment(c1,c2, sep0=";"):
    '''this function could get the common part between string c1 and c2
    for example, c1="a;b", c2="a;c" '''
    if c1 is None:
        c10 = 'NONE'
    else:
        c10 = c1.split(sep0)
        c10 = [x.strip() for x in c10]
    if c2 is None:
        c20 = 'NONE'
    else:
        c20 = c2.split(sep0)
        c20 = [x.strip() for x in c20]
    c3 = list(set(c10).intersection(c20))
    c4 = sep0.join(str(e) for e in c3)
    return c4

def getRXNgeneMapping(rxn0, gpr0):
    '''this function is used to split the GPR;
    input, for example rxn0=['r1','g2']
    gpr0=['a or c','a and b']
    output, each rxn related with each gene'''
    s1 = rxn0
    s2 = gpr0
    s2 = s2.str.replace('and','@')
    s2 = s2.str.replace('or','@')
    s2 = s2.str.replace('\\( ','')
    s2 = s2.str.replace('\\(\\( ','')
    s2 = s2.str.replace('\\(', '')
    s2 = s2.str.replace('\\(\\(', '')
    s2 = s2.str.replace(' \\)','')
    s2 = s2.str.replace(' \\)\\) ','')
    s2 = s2.str.replace('\\)', '')
    s2 = s2.str.replace('\\)\\) ', '')
    s3 = splitAndCombine(s2,s1,sep0="@")
    s3['V2'] = s3['V2'].str.strip()
    s3.columns = ['rxnID', 'gene']
    return s3

def getRXNmetaboliteMapping(rxn0, met0):
    '''this function is used to split the equation of metabolites; used to produce the dataframe format of GEM using
    cobrapy
    input, for example rxn0=['r1','g2']
    gpr0=['a => c','a => b']
    output, each rxn related with each gene'''
    met_annotation = pd.read_excel('../result/met_yeastGEM.xlsx')
    s1 = rxn0
    s2 = met0
    s3 = splitAndCombine(s2,s1,sep0=" ")
    s3['V2'] = s3['V2'].str.strip()
    s3.columns = ['rxnID', 'met']
    s3['met_name'] = singleMapping(met_annotation['description'],met_annotation['m_name'],s3['met'])
    for i, x in s3.iterrows():
        if s3['met_name'][i] is None:
            s3['met_name'][i] = s3['met'][i]
        else:
            s3['met_name'][i] = s3['met_name'][i]
    return s3


def correctSomeWrongFormat(model0):
  """
  This function is used to correct some wrong format when read yeastGEM model from cobratoolbox
  """
  # Correct metabolite ids:
  for met in model0.metabolites:
    met.id = met.id.replace('__91__', '_')
    met.id = met.id.replace('__93__', '')

  # Correct gene ids:
  for gene in model0.genes:
    gene.id = gene.id.replace('__45__', '-')
  return model0


def produceMetaboliteList(model0):
  #produce the dataframe for the metabolites from yeastGEM
  met_list =[None]*len(model0.metabolites)
  met_dataframe = pd.DataFrame({'m_name':met_list,
                              'description':met_list,
                              'formula':met_list})

  for i, met in enumerate(model0.metabolites):
      print(i)
      met_dataframe['m_name'][i] = met.id
      met_dataframe['description'][i] = met.name
      met_dataframe['formula'][i] = met.formula
  #s2 = met_dataframe['m_name'].str.split('_', expand=True)
  #met_dataframe['description'] = met_dataframe['description'].str.replace('\s\[', '@')
  #s3 = met_dataframe['description'].str.split('@', expand=True)
  #met_dataframe['description'] = s3.iloc[:, 0] + '[' + s2.iloc[:, 2] + ']'
  return met_dataframe

def produceRxnList(model0):
  #produce the dataframe for the rxn from yeastGEM
  reaction_list =[None]*len(model0.reactions)
  gem_dataframe = pd.DataFrame({'name':reaction_list,
                              'equation':reaction_list,
                              'GPR':reaction_list,
                              'rxnID':reaction_list,
                              'formula':reaction_list
                              })

  for i, reaction in enumerate(model0.reactions):
      print(i)
      gem_dataframe['name'][i] = reaction.name
      gem_dataframe['equation'][i] = reaction.reaction
      gem_dataframe['GPR'][i] = reaction.gene_reaction_rule
      gem_dataframe['rxnID'][i] = reaction.id
  gem_dataframe['ID'] = ['R'+ str(i) for i in range(0, len(model0.reactions))]
  gem_dataframe['GPR'] = gem_dataframe['GPR'].str.replace('__45__', '-')
  #replace the metabolite name in gem_dataframe
  s0 = getRXNmetaboliteMapping(gem_dataframe['rxnID'], gem_dataframe['equation'])
  gem_dataframe['formula'] = multiMapping(s0['met_name'],s0['rxnID'],gem_dataframe['rxnID'],removeDuplicates=False)
  gem_dataframe['formula'] = gem_dataframe['formula'].str.replace(";", " ")
  return gem_dataframe


def getSimilarTarget(rxn_yeast0,rxn_newGPR0,ss):
    from fuzzywuzzy import fuzz
    from fuzzywuzzy import process
    rxn_yeast1 = np.array(rxn_yeast0)  # np.ndarray()
    rxn_yeast2 = rxn_yeast1.tolist()
    rxn_yeast3 = pd.Series((v[0] for v in rxn_yeast2))
    rxn_newGPR1 = np.array(rxn_newGPR0)  # np.ndarray()
    rxn_newGPR2 = rxn_newGPR1.tolist()
    rxn_newGPR3 = pd.Series((v[0] for v in rxn_newGPR2))
    similarTarget = [None] * ss
    for i in range(ss):
        similarTarget[i] = process.extract(rxn_newGPR3[i], rxn_yeast3, limit=2)

    return similarTarget

def singleMapping (description, item1, item2, dataframe=True):
    """get the single description of from item1 for item2 based on mapping"""
    #description = w
    #item1 = v
    #item2 = testData
    # used for the list data
    if dataframe:
        description = description.tolist()
        item1 = item1.tolist()
        item2 = item2.tolist()
    else:
        pass
    index = [None]*len(item2)
    result = [None]*len(item2)
    tt = [None]*len(item2)
    for i in range(len(item2)):
        if item2[i] in item1:
            index[i] = item1.index(item2[i])
            result[i] = description[index[i]]
        else:
            index[i] = None
            result[i] = None
    return result

def multiMapping (description, item1, item2, dataframe=True, sep=";", removeDuplicates=True):
    """get multiple description of from item1 for item2 based on mapping"""
    #description = w
    #item1 = v
    #item2 = testData
    #used for the list data
    if dataframe:
        description = description.tolist()
        item1 = item1.tolist()
        item2 = item2.tolist()
    else:
        pass
    result = [None]*len(item2)
    for i in range(len(item2)):
        if item2[i] in item1:
            index0 = [description[index] for index in range(len(item1)) if item1[index] == item2[i]]
            if removeDuplicates:
                index1 = pd.unique(index0).tolist()
            else:
                index1 = index0
            result[i] = sep.join(str(e) for e in index1) #string cat
        else:
            result[i] = None
    return result


def updateOneColumn(df1, df2, key0, value0):
    """
    using dataframe df2 to update the df1

    :param df1:
    :param df2:
    :param key0: the common column name, a string, used for the mapping
    :param value0: the column in df2 used to update the df1
    :return:
    example
    df10 = pd.DataFrame({'A': ['a', 'b', 'c'],
                 'B': ['x', 'y', 'z']})

    df20 = pd.DataFrame({'A':['c','b'],
                       'B': ['e', 'd']})
    updateOneColumn(df10,df20,key0='A',value0='B')
    """
    df10 = df1.copy()
    df11 = df1.copy()
    df10[value0] = multiMapping(df2[value0], df2[key0], df10[key0])
    for i, x in df10.iterrows():
        print(x[value0])
        if x[value0] is None:
            df11[value0][i] = df11[value0][i]
        else:
            df11[value0][i] = df10[value0][i]
    return df11[value0]



def saveExcel(infile, outfile):
    writer = pd.ExcelWriter(outfile)
    infile.to_excel(writer,'Sheet1')
    writer.save()


def findRemoveRxnBasedOnGene(rxnRemovedGene, rxnAllGene):
    '''this function is used to remove rxn based on the removed gene list
    if the all genes in a reaction were in the removed gene list, then this reaction was removed'''
    #x0 = gem_dataframe['removed_gene'].tolist()
    #y0 = gem_dataframe['all_gene'].tolist()
    x0=rxnRemovedGene.tolist()
    y0=rxnAllGene.tolist()
    removed_rxn = list()
    for x,y in zip(x0,y0):
        if x is None:
            removed_rxn.append('NO')
        else:
            if len(x) ==len(y):
                removed_rxn.append('YES')
            else:
                removed_rxn.append('NO')
    return removed_rxn



def RemoveDuplicated(s1):
    """
    example:
    s1=['a // a', 'b // a', None, 'non']

    """
    s2=list()
    for x in s1:
        print(x)
        if x =='non':
            s2.append('')
        elif x is None:
            s2.append('')
        else:
            if "//" in x:
                s0= x.split(' // ')
                s0 = [x.strip() for x in s0]
                s01= list(set(s0))
                if len(s01)==1:
                    s2.append(s01[0])
                else:
                    s2.append(' // '.join(s01))
            else:
                s2.append(x)
    return s2




def exchange(s1, subystem):
    """
    this function is used to define the exchange reaction
    s1=['a --> b','a <=> c', 'H+ [extracellular] + L-citrulline [extracellular] <=> H+ [cytoplasm] L-citrulline [cytoplasm]', ' a--> ']
    subsystem = ['a','a','b','']

    """
    for i, x in enumerate(s1):
        if ' --> ' in x:
            x0 = x.split(' --> ')
            if len(x0[1]) >=1:
                #subystem.append('General')  # exchange
                subystem[i] = subystem[i]
            else:
                subystem[i] ='Exchange reaction' #exchange
                print(subystem[i])
        if ' <=> ' in x:
            x0 = x.split(' <=> ')
            if len(x0[1]) >=1:
                #subystem.append('General')  # exchange
                subystem[i] = subystem[i]
            else:
                subystem[i] ='Exchange reaction' #exchange
                print(subystem[i])
        else:
            subystem[i] = subystem[i]
    return subystem


#SLIME rxn
def SLIME(rxnName, subsystem):
    """
    if the rxnName contains the SLIME, classify the reaction into SLIME reaction
    """
    for i,x in enumerate(rxnName):
        if 'SLIME' in x:
            subsystem[i] = 'SLIME reaction'
            print(subsystem[i])
        else:
            subsystem[i] = subsystem[i]
    return subsystem



def transport(s1, subsysem):
    """
    this function is used to define the transport reaction
    #example
     s1 =['UMP [extracellular] <=> UMP [cytoplasm]', 'H+ [extracellular] + phosphoenolpyruvate [extracellular] <=> H+ [cytoplasm] + phosphoenolpyruvate [cytoplasm]']
     subsysem = ['a','b']

    :param s1:
    :param subsysem:
    :return:
    """

    for i, x0 in enumerate(s1):
        x1 = re.findall(r"\[([A-Za-z0-9_\s]+)\]", x0)
        x2 = re.sub(r"\[([A-Za-z0-9_\s]+)\]", '', x0)
        if "<=>" in x2:
            x3 = x2.split("<=>")
        elif "<->" in x2: #bigg database format
            x3 = x2.split("<=>")
        else:
            x3 = x2.split("-->")
        x3 = [x.strip() for x in x3]
        x1=pd.unique(x1).tolist() #remove the duplicated
        if '+' in x3[0]:
            x30=x3[0].split('+')
        else:
            x30=x3[0]
        x30=[x.strip() for x in x30]
        if '+' in x3[1]:
            x31 = x3[1].split('+')
        else:
            x31=x3[1]
        x31 = [x.strip() for x in x31]

        if set(x30) == set(x31):
            subsysem[i] ='Transport' + '['+', '.join(x1)+']'
            print(subsysem[i])
        else:
            subsysem[i] = subsysem[i]

    return subsysem


def nz(value):

    '''
    Convert None to string else return value.
    '''

    if value == None:
        return 'none'
    return value