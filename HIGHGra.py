# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import csv
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font',family=font_name)
import numpy as np


def GRAPHY():
#pip install pandas, pip install matplotlib
    df = pd.read_csv('CSVCSV.csv',engine='python')

    plt.subplot(211)
    plt.scatter(df['차종'],df['입출구'],df['교통량'])
    plt.ylabel("교통량")

    plt.subplot(212)
    plt.scatter(df['입출구'],df['교통량'])
    plt.ylabel("교통량")

    plt.show()
    print(df)
if __name__ == "__main__":
    GRAPHY()
