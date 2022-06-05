# import libraries
import tabula
import study_numpy as np
import pandas as pd


# first job
# extract metabolite concentration data
df1 = tabula.read_pdf("Metabolite concentrations_Part6.pdf")
df2 = tabula.read_pdf("Metabolite concentrations_Part7.pdf")

# convert PDF into CSV
tabula.convert_into("Metabolite concentrations_Part6.pdf", "output1.tsv", output_format="tsv")
tabula.convert_into("Metabolite concentrations_Part7.pdf", "output2.tsv", output_format="tsv")


# extract flux data
df3 = tabula.read_pdf("Metabolite concentrations_Part2.pdf")
df4 = tabula.read_pdf("Metabolite concentrations_Part3.pdf")

# convert PDF into CSV
tabula.convert_into("Metabolite concentrations_Part2.pdf", "flux1.tsv", output_format="tsv")
tabula.convert_into("Metabolite concentrations_Part3.pdf", "flux2.tsv", output_format="tsv")


# extract the reaction information
df5 = tabula.read_pdf("Metabolite concentrations_Part8.pdf")
df6 = tabula.read_pdf("Metabolite concentrations_Part9.pdf")

# convert PDF into CSV
tabula.convert_into("Metabolite concentrations_Part8.pdf", "rxn_inf1.tsv", output_format="tsv")
# convert PDF into CSV
tabula.convert_into("Metabolite concentrations_Part9.pdf", "rxn_inf2.tsv", output_format="tsv")


# some other changes
rxn_inf = pd.read_excel('rxn_inf1.xlsx')
flux_inf = pd.read_excel('flux1_vip.xlsx')
general_direction = ['net','xch', 'for','rev']
newColumn = flux_inf['Reaction'].tolist()
newColumn0 = []
newColumn1 = []
for i in newColumn:
    if 'net' in i:
        newColumn0.append('net')
        j = i.replace('net','')
        newColumn1.append(j)
    elif 'xch' in i:
        newColumn0.append('xch')
        j = i.replace('xch', '')
        newColumn1.append(j)
    elif 'for' in i:
        newColumn0.append('for')
        j = i.replace('for', '')
        newColumn1.append(j)
    else:
        newColumn0.append('rev')
        j = i.replace('rev', '')
        newColumn1.append(j)


flux_inf['Direction'] = newColumn0
flux_inf['Reaction'] = newColumn1


writer = pd.ExcelWriter('flux_inf_correct.xlsx')
flux_inf.to_excel(writer,'Sheet1')
writer.save()


#second job
# "Deciphering the underlying metabolomic and lipidomic patterns linked to thermal acclimation in Saccharomyces cerevisiae"
#  convert PDF into CSV
tabula.convert_into("pr7b00921_si_001_Part7.pdf", "output1.tsv", output_format="tsv")
tabula.convert_into("pr7b00921_si_001_Part8.pdf", "output2.tsv", output_format="tsv")
tabula.convert_into("pr7b00921_si_001_Part9.pdf", "output3.tsv", output_format="tsv")
tabula.convert_into("pr7b00921_si_001_Part10.pdf", "output4.tsv", output_format="tsv")
tabula.convert_into("pr7b00921_si_001_Part11.pdf", "output5.tsv", output_format="tsv")
tabula.convert_into("pr7b00921_si_001_Part12.pdf", "output6.tsv", output_format="tsv")
tabula.convert_into("pr7b00921_si_001_Part13.pdf", "output7.tsv", output_format="tsv")