# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:47:37 2020

@author: sample
"""

import argparse


# パーサーを作る
parser = argparse.ArgumentParser(
            prog='argparseTest.py',  # プログラム名
            usage='Demonstration of argparser',  # プログラムの利用方法
            description='description',  # 引数のヘルプの前に表示
            epilog='end',  # 引数のヘルプの後で表示
            add_help=True,  # -h/–help オプションの追加
            )

# コマンドライン引数
parser = argparse.ArgumentParser()
parser.add_argument("-mode", "--mode", default="CLI", help="action mode:CLI(default) or SERVER")
parser.add_argument("-ip", "--ip", default="127.0.0.1", help="IP or hostname(default localhost)")
parser.add_argument("-port", "--port", default="514", help="port number(default 514)")
parser.add_argument("-protocol", "--protocol", default="UDP", help="TCP or UDP(default)")
parser.add_argument("-count", "--count", default="1", help="send count(default 1)")
parser.add_argument("-message", "--message", default="syslog message!!", help="syslog message")

# 引数を解析する
args = parser.parse_args()

# 引数表示
#print(args.mode)
#print(args.ip)
#print(args.port)
#print(args.protocol)
#print(args.count)
#print(args.message)
