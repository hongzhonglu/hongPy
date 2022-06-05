# Import packages
import study_numpy as np
import pandas as pd
import os    ##for directory
# set the directory
os.chdir('/Users/luho/PycharmProjects/python learning/venv/project3_practicse')
os.getcwd()



'''find the similar targets'''
## application of python in project
## string comparing using fuzzywuzzy

# set the directory
os.chdir('/Users/luho/PycharmProjects/python learning/venv/project3_practicse')
os.getcwd()



""" simple example"""
fuzz.ratio("this is a test", "this is a test!")
choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
process.extract("zz", choices, limit=2)



## description of function
## get the similar target for rxn_newGPR0 from rxn_yeast0
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


#example
newMet = pd.read_excel('new metabolite for check.xlsx')
newMet0 = newMet[['name_unify']]


gemMet = pd.read_excel('unique metabolite in yeastGEM.xlsx')
gemMet0 = gemMet[['Description_simple']]

ss0 = len(newMet0)
similarTarget0 = getSimilarTarget(gemMet0,newMet0,ss=ss0)

newMet['target from yeastGEM'] = similarTarget0
writer = pd.ExcelWriter('new metabolite for check with target from yeastGEM.xlsx')
newMet.to_excel(writer,'Sheet1')
writer.save()
