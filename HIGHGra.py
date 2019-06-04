# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font',family=font_name)
import xml.etree.ElementTree as etree
import HIGHWAY3api
import sys

#pip install pandas, pip install matplotlib
df = pd.read_csv('CSVCSV.csv',engine='python')


plt.subplot(211)
plt.bar(df['차종'],df['교통량'])
plt.xlabel('')
plt.ylabel("교통량")

plt.subplot(212)
plt.bar(df['입출구'],df['교통량'])
plt.xlabel('')
plt.ylabel("교통량")

plt.title('')
plt.show()
print(df)
