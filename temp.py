# -*- coding: utf-8 -*-
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_excel("mobile_app_user_dataset.xlsx")
##print data.head()
#
##print type(data)
#
x = data["Q1_1_TEXT"]
##print x
#
count = x.groupby(x).count()
#print count
#
count1 = count[1:(len(count)-1)]
#print count1
#
#count2 = count[:-1]
#print count2

print count1.index
print count1.values

sns.set(style="white", context="talk")

sns.barplot(count1.index,count1.values)


sns.despine(bottom=True)


#rs = np.random.RandomState(7)
#
#
## Set up the matplotlib figure
#f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8,6), sharex=True)
#
## Generate some sequential data
#x = np.array(list("ABCDEFGHI"))
#y1 = np.arange(1, 10)
#sns.barplot(x, y1, palette="BuGn_d", ax=ax1)
#ax1.set_ylabel("Sequential")
#
## Center the data to make it diverging
#y2 = y1 - 5
#sns.barplot(x, y2, palette="RdBu_r", ax=ax2)
#ax2.set_ylabel("Diverging")
#
## Randomly reorder the data to make it qualitative
#y3 = rs.choice(y1, 9, replace=False)
#sns.barplot(x, y3, palette="Set3", ax=ax3)
#ax3.set_ylabel("Qualitative")
#
## Finalize the plot
#sns.despine(bottom=True)
#plt.setp(f.axes, yticks=[])
#plt.tight_layout(h_pad=3)



#help(sns)
#help(sns.set())
#str(sns.set())
#sns.set()


