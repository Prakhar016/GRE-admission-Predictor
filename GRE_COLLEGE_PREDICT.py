# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 18:35:16 2019

@author: Prakhar
"""


import numpy as np
import pandas as pd
from sklearn.linear_model import LassoCV
df = pd.read_csv("Admission_Predict.csv")
x=df.iloc[:,1:-2].values

y=df[df.columns[-1:]]
ls = LassoCV(cv=5, random_state=0)
ls.fit(x,y)
gre1=x[:,0].mean()
tof1=x[:,1].mean()
un1=x[:,2].mean()
sop1=x[:,3].mean()
lor1=x[:,4].mean()
cgpa1=x[:,5].mean()
def pred(GREScore,TOEFLScore,UniversityRating,SOP ,LOR ,CGPA):
    x=[]
    x.append(GREScore)
    x.append(TOEFLScore)
    x.append(UniversityRating)
    x.append(SOP)
    x.append(LOR)
    x.append(CGPA)
    arr=np.array(x)
    return ls.predict(arr.reshape(1,-1))


print("If No value then enter N")
gre=input("Enter the gre_score:-")
if gre=='N':
    gre=gre1
else:
    gre=float(gre)
toefl=input("Enter the toefl_score:-")
if toefl=='N':
    toefl=tof1
else:
    toefl=float(toefl)
univ=input("Enter the university_score:-")
if univ=='N':
    univ=un1
else:
    univ=float(univ)
sop=input("Enter the sop_score:-")
if sop=='N':
    sop=sop1
else:
    sop=float(sop)
lor=input("Enter the lor_score:-")
if lor=='N':
    lor=lor1
else:
    lor=float(lor)
cgpa=input("Enter the cgpa_score:-")
if cgpa=='N':
    cgpa=cgpa1
else:
    cgpa=float(cgpa)
PREDICT=pred(gre,toefl,univ,sop,lor,cgpa)


if PREDICT>0.95:
    print("admission possble in Top Collages")
elif 0.80<PREDICT<0.95:
    print("maybe admission possible")
elif PREDICT<0.80:
    print("Better luck next time")


