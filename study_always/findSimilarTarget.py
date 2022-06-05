# The code is used to find the similar target for one target based on character similarity
# Import packages
import study_numpy as np
import pandas as pd
import os    ##for directory
from fuzzywuzzy import fuzz, process
# set the directory
os.getcwd()

""" simple example"""
fuzz.ratio("this is a test", "this is a test!")
choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
process.extract("zz", choices, limit=2)



## description of function
## get the similar target for rxn_newGPR0 from rxn_yeast0
def getSimilarTarget(rxn_yeast0,rxn_newGPR0,ss):
    from fuzzywuzzy import process
    rxn_yeast1 = np.array(rxn_yeast0)  # np.ndarray()
    rxn_yeast2 = rxn_yeast1.tolist()
    rxn_yeast3 = pd.Series((v[0] for v in rxn_yeast2))
    rxn_newGPR1 = np.array(rxn_newGPR0)  # np.ndarray()
    rxn_newGPR2 = rxn_newGPR1.tolist()
    rxn_newGPR3 = pd.Series((v[0] for v in rxn_newGPR2))
    similarTarget = [None] * ss
    for i in range(ss):
        print(i)
        s0 = process.extract(rxn_newGPR3[i], rxn_yeast3, limit=2)
        s01 = s0[0]
        s02 = s0[1]
        s1 =s01[0]
        s2 =s01[1]
        s3 = s02[0]
        s4 = s02[1]
        s = "&".join[s1, s2,s3,s4]
        similarTarget[i] = s

    return similarTarget



s0 = ('ethanol', 100, 3093), ('ethanol', 100, 3094)

#example
newMet = pd.read_excel('FBA_model_metNames_table.xlsx')
newMet0 = newMet[['model_Fdb_metNames']]


gemMet = pd.read_excel('Foodb_orig_source_name.xlsx')
gemMet0 = gemMet[['orig_source_name']]

ss0 = len(newMet0)
similarTarget0 = getSimilarTarget(gemMet0,newMet0,ss=ss0)


newMet['target from yeastGEM'] = similarTarget0
writer = pd.ExcelWriter('new metabolite for check with target from yeastGEM.xlsx')
newMet.to_excel(writer,'Sheet1')
writer.save()
