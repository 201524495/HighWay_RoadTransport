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