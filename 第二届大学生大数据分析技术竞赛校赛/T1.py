"""
@Python Interpreter: /opt/homebrew/bin/python3.11
@Coding            : UTF-8
@Time              : 2023/07/11 23:13
@Author            : ruyan
@Software          : PyCharm
@Python Project    : WZBC-Python
@File              : T1.py
"""


import pandas as pd


def process_data():
    data = pd.read_csv('链家北京租房数据.csv', encoding='GBK')

    data_without_duplicates = data.drop_duplicates()

    print(data_without_duplicates)

    data_without_duplicates.to_csv('删除重复数据后链家北京租房数据.csv', index=False)


def main():
    process_data()


if __name__ == '__main__':
    main()
