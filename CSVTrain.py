# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 11:08:43 2021

@author: Ares
"""

import numpy as np 

import pandas as pd 

from matplotlib import pyplot as plt


train_df = pd.read_csv("titanic.csv")

print(train_df)

#print(len(train_df))
#print(train_df.describe())

fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10, 4))
women = train_df[train_df['Sex']=='female']
men = train_df[train_df['Sex']=='male']

#print(women)

richwomen = women[women['Fare']>70]

poorwomen = women[women['Fare']<70]

#print(richwomen.mean())

print(len(richwomen))

#print(poorwomen.mean())

def survivalcomparison(df1,df2):
    df1mean=df1.mean()
    df2mean=df2.mean()
    dfdelta = df1mean['Survived']-df2mean['Survived']
    print("there is a difference of "+str(dfdelta)+" between the two averages")
    return dfdelta

def avgsurvivalcomparison(df1,df2,df1name,df2name):
    df1mean=df1.mean()
    df2mean=df2.mean()
    dfdelta = df1mean['Survived']-df2mean['Survived']
    print( str(df1name)+" has a higher avg survival rate of "+str(dfdelta)+" compared to "+str(df2name))
    return dfdelta


#survivalcomparison(richwomen,poorwomen)

avgsurvivalcomparison(richwomen,poorwomen,'rich women','poor women')

#print(train_df['Sex']=='female')

