# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:18:02 2020

@author:sample
"""

import os
import time
import config
import logger
import database
# import rsyslog
# import syslog
import help
import line
import astronomy_graph
from tqdm import tqdm
from datetime import datetime


if __name__ == "__main__":

    logger.app_logger.info('Application Start')
    # rsyslog.open()
    # rsyslog.logging(syslog.LOG_ALERT, 'Processing started')
    now = datetime.now()
    start_time = time.time()
    os.system('cls')  # コンソールクリア
    # database.create_table()  # テーブル生成
    logger.logging_environment()  # 実行環境ログ
    config.logging_paramter()  # Parameter読み込み

    astronomy_graph.init()

    # line.send_message("Application End")
    # rsyslog.close()
    proc_time = (time.time()-start_time)
    database.insert(now, proc_time)  # データベース追加
    logger.app_logger.info('Application End(%.6lf[sec])', proc_time)
