"""
@Python Interpreter: /opt/homebrew/bin/python3.11
@Coding            : UTF-8
@Time              : 2023/07/11 23:48
@Author            : ruyan
@Software          : PyCharm
@Python Project    : WZBC-Python
@File              : T4.py
"""


import pandas as pd
import matplotlib.pyplot as plt


def analyze_huxing():
    data = pd.read_csv('替换户型列中房间为室后链家北京租房数据.csv')

    huxing_counts = data['户型'].value_counts()
    print(huxing_counts)

    huxing_counts = huxing_counts[:11].sort_index().reset_index()

    huxing_counts.columns = ['户型', '数量']
    print(huxing_counts)
    huxing_counts.to_csv('户型数量分析.csv')

    plt.rcParams['font.sans-serif'] = ['Songti SC']

    plt.figure(dpi=600)
    huxing_counts.plot(kind='barh')
    plt.title('户型数量分析')
    plt.xlabel('数量')
    plt.ylabel('户型')
    plt.xticks([0, 500, 1000, 1500, 2000, 2500])
    plt.show()


def main():
    analyze_huxing()


if __name__ == '__main__':
    main()
