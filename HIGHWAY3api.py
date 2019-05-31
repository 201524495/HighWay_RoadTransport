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

