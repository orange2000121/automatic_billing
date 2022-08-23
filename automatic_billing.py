from math import gcd
import pygsheets
import requests
import pandas as pd
import csv

def getOrderDetails(start_date : str, end_date : str, store='9330'):
    download_api = 'http://www.posky.net/posky/sales_analysis/orders_list/download_excel'
    with requests.Session() as s:
        download = s.get(f'{download_api}?s={start_date}&e={end_date}&b={store}')

        decoded_content = download.content.decode('ansi')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        df = pd.DataFrame(cr)
        df.to_csv('raw_datas/test.csv', index=False, header=False)
        df = pd.read_csv('raw_datas/test.csv')
        return df
def uploadGoogleSheet(df):
    gc = pygsheets.authorize(service_file='smalltownweb-52cee3cd4431.json')
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1ZMh5FM0ZjT1z5kP1VC1fMQpCrUACCtaB-jvpqjzGK1s/edit#gid=0')
    wks = sh.worksheet_by_title('2022')
    wks.set_dataframe(df, (1,1))
    return True
def createSheet():
    gc = pygsheets.authorize(service_file='smalltownweb-52cee3cd4431.json')
    gc.create('2022')
    return True
if __name__ == '__main__':
    # df = getOrderDetails('2022/8/1', '2022/08/30')
    # uploadGoogleSheet(df)
    # print('done')
    createSheet()