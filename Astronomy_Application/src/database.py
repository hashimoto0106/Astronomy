# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:36:30 2020

@author: sample
"""

import sqlite3
import config
import platform

conn = sqlite3.connect(config.database)  # dbファイルを開き、コネクションを取得
cursor = conn.cursor()  # カーソルを取得


def create_table():
    # テーブルが存在する場合は削除
    cursor.execute('DROP TABLE IF EXISTS login')

    # テーブル生成
    cursor.execute('''
        CREATE TABLE login (
            start_time TEXT,
            os TEXT,
            python_version TEXT,
            host TEXT,
            proc_time_sec REAL
        )
    ''')

def insert(start_time, proc_time):
    cursor.execute('INSERT INTO login VALUES (:start_time, :os, :python_version, :host, :proc_time_sec)',
          {'start_time': start_time, 'os': platform.platform(), 'python_version': platform.python_version(), 'host': platform.node(), 'proc_time_sec': proc_time})
    
    conn.commit()  # 変更をコミット（保存)
    conn.close()  # コネクションを閉じる
