# p2019
# 본인의 과제명 작성

학과 | 학번 | 성명
---- | ---- | ---- 
정보컴퓨터공학과 |201524495 |안준수


## 프로젝트 개요
전체 프로젝트를 수행하는 흐름도를 표나 그림으로 작성(본문스타일)  
공공데이터포털(data.go.kr)에 있는 오픈 api를 이용해 xml 파일 및 csv 파일로 변형 시켜 
입구/출구에 대한 통행량, 차종에 대한 통행량을 그래프로 표현한다.

## 사용한 공공데이터 
[데이터보기](http://data.ex.co.kr/exopenapi/trafficapi/trafficIc?serviceKey=sFogfIyQvOkImGDglyDSE5KbjRXkU1QNWFzOg8Zb5Dzx0tIjWfiOUOU7qmzMf%2BUDg978J07nsNabd5aA56D8aQ%3D%3D&type=xml&exDivCode=00&unitCode=140&numOfRows=999)

## 소스
* [xml 파싱](https://github.com/201524495/p2019/blob/master/HIGHWAYXML.py)
* [csv 변환](https://github.com/201524495/p2019/blob/master/HIGHWAY3api.py)
* [그래프](https://github.com/201524495/p2019/blob/master/HIGHGra.py)

* 코드 삽입
#api이용해서 xml 불러오기 & 저장하기
~~~python
import urllib.request #pip install requests
import csv
import pandas as pd


def XML() :
    unitCode = input("영업소 코드를 입력하세요")
    inOuttype = input("입(0)/출(1) 구분")
    tmType = input("자료 구분(1시간(1)/15분(2))")
    tcsType = input("TCS(1)/Hi-Pass(2) 구분")
    exDivCode = input("도로공사(00)/민자(01,02,08,11,18) 구분")
    carType = input("1종소형(1)/2종중형(2)/3.4.5종대형(3,4,5)/6종소형(6)")
    numOfRows = input("한 페이지당 출력 건수")
    pageNo = input('출력 페이지 번호')
    key = 'sFogfIyQvOkImGDglyDSE5KbjRXkU1QNWFzOg8Zb5Dzx0tIjWfiOUOU7qmzMf%2BUDg978J07nsNabd5aA56D8aQ%3D%3D'
    url = 'http://data.ex.co.kr/exopenapi/trafficapi/trafficIc?serviceKey='+key+\
    '&type=xml&exDivCode='+exDivCode+'&unitCode='+unitCode+'&inOutType='+inOuttype+\
    '&tmType='+tmType+'&tcsType='+tcsType+'&carType='+carType+\
    '&numOfRows='+numOfRows+'&pageNo='+pageNo+''

    data = urllib.request.urlopen(url).read()
    f = open("sample1.xml","wb")
    f.write(data)
    f.close()


if __name__ == '__main__':
    XML()
#api이용해서 xml 불러오기 & 저장하기
~~~

* 코드 삽입
# xml파일 읽어서 csv 파일로 저장
~~~
import xml.etree.ElementTree as etree
import sys
import csv

def READ():
    sys.stdout = open('CSVCSV.csv','w')
    tree = etree.parse('sample1.xml')
    root = tree.getroot()
    print(
        '입출구' + ',' + '업소명' + ',' + '업소코드' + ',' + '차종' + ',' + '교통량' + ',' + 'TCS/hi-pass' + ',' + '집계시간'+','+'결과메세지')
    for a in root.findall('trafficIc'):
        if a.findtext('carType') == '1':
            s = '1종 소형'
        elif a.findtext('carType') == '2':
            s = '2종 중형'
        elif a.findtext('carType') == '3':
            s = '3종 대형'
        elif a.findtext('carType') == '4':
            s = '4종 대형'
        elif a.findtext('carType') == '5':
            s = '5종 대형'
        elif a.findtext('carType') == '6':
            s = '6종 소형'

        print(a.findtext('inoutName'), ',', a.findtext('unitName'), ',', a.findtext('unitCode'), ',', s, ',',
              a.findtext('trafficAmout'), ',', a.findtext('tcsName'), ',', a.findtext('tmName'), ',',
              a.findtext('message'))


if __name__ == "__main__":
    READ()
# xml파일 읽어서 csv 파일로 저장
~~~


* 코드 삽입
그래프 
~~~
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
def GRAPHY():
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
if __name__ == "__main__":
    GRAPHY()
~~~
