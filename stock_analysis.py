from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def company_stock(start,end,company_code):
    df = data.DataReader(company_code,"stooq")
    df = df[(df.index >= start) & (df.index <= end)]
    df.index

    date = df.index
    price = df['Close']


    span01 = 5
    span02 = 25
    span03 = 50

    df['sma01'] = price.rolling(window = span01).mean()
    df['sma02'] = price.rolling(window = span02).mean()
    df['sma03'] = price.rolling(window = span03).mean()




    #出来高と折れ線を同時に出力
    plt.figure(figsize=(20,20))
    plt.subplot(2,1,1)

    plt.plot(date,price,label='Close',color='#99b898')
    plt.plot(date,df['sma01'],label = 'sma01',color='#e84a5f')
    plt.plot(date,df['sma02'],label = 'sma02',color='#ff847c')
    plt.plot(date,df['sma03'],label = 'sma03',color='#feceab')
    plt.show()

    plt.subplot(2,1,2)
    plt.bar(date,df['Volume'],label='Volume',color='grey')
    plt.show()

#main
print("これから指定された株価のデータを出力します")
print("株価出力に関する情報をすべて半角で教えてください")
print("=========")
start = str(input("期間の始まりを入力してください(例:2020-09-02):"))
end =  str(input("期間の終わりを入力してください(例:2020-09-02):"))
company_code = str(input("証券コードの4桁に末尾.JPを付けて入力してください(例:xxxx.JP)"))
print("株価データを出力します")
company_stock(start,end,company_code)