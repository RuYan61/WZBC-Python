"""
@Python Interpreter: /opt/homebrew/bin/python3.11
@Coding            : UTF-8
@Time              : 2023/07/11 23:31
@Author            : Y1560
@Software          : PyCharm
@Python Project    : WZBC-Python
@File              : T2.py
"""


import pandas as pd

def replace_huxing():
    data = pd.read_csv('删除重复数据后链家北京租房数据.csv')

    data['户型'] = data['户型'].str.replace('房间', '室')

    print(data)

    data.to_csv('替换户型列中房间为室后链家北京租房数据.csv', index=False)


def main():
    replace_huxing()


if __name__ == '__main__':
    main()
