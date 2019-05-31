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


'''
INOUT = range(0, 1)
pieces = []
with open("sample2.txt", 'rt') as f:
    data = csv.reader(f, delimiter = ' ')
    for d in data:
        pieces.append(d)

x = [INOUT for INOUT, carTYPE, Amount in pieces]

y1 = [Amount for INOUT, carTYPE, Amount in pieces]
y2 = [carTYPE for INOUT, carTYPE, Amount in pieces]

p1 = plt.plot(x,y1,'r^--',label = 'Amount')
p2 = plt.plot(x,y2,'bs-',label = 'carTYPE')

plt.legend()
plt.title("HELP ME")
plt.xlabel('INOUT'),plt.ylabel('AMOUNT')
plt.show'''
#txt파일로 그래프 그리기
#csv 파일로 그래프 그리기
'''a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
df = pd.read_csv('CSVCSV.csv',engine='python')
for row in csv.reader(df):
    a.append(row[0])    #입출구
    b.append(row[1])    #업소명
    c.append(row[2])    #업소코드
    d.append(row[3])    #차종
    e.append(row[4])    #교통량
    f.append(row[5])    #TCS
    g.append(row[6])    #집계시간
    h.append(row[7])    #결과 메세지
plt.plot()

plt.bar(a,e,'r')
plt.bar(d,e,'b')
plt.axis([-1,30,-5,30])

plt.show()     '''


