# -*- coding: utf-8 -*-
__author__ = 'alex'

import pandas as pd

df = pd.read_csv("./data/HR.csv")
type(df['satisfaction_level'])
type(df.mean())
df.mean()
df.median()
df.quantile(0.25)
print(df.head(10))
