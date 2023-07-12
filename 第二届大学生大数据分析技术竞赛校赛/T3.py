"""
@Python Interpreter: /opt/homebrew/bin/python3.11
@Coding            : UTF-8
@Time              : 2023/07/11 23:36
@Author            : ruyan
@Software          : PyCharm
@Python Project    : WZBC-Python
@File              : T3.py
"""


import pandas as pd


def count_by_region():
    data = pd.read_csv('替换户型列中房间为室后链家北京租房数据.csv')

    region_counts = data['区域'].value_counts().sort_index().reset_index()

    region_counts.columns = ['区域', '数量']

    region_counts.to_csv('房源数量、位置分布分析.csv')

    print(region_counts)


def main():
    count_by_region()


if __name__ == '__main__':
    main()
