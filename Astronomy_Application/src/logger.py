# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:48:25 2020

@author: sample
"""

import logging.config
import config
import platform


# ログ設定ファイルからログ設定を読み込み
logging.config.fileConfig(config.config_log)
app_logger = logging.getLogger()


def init():
    app_logger.info('logging Init')


def logging_environment():
    # 開発環境
    app_logger.info("Python Version:%s", platform.python_version())
    app_logger.info("Compiler:%s", platform.python_compiler())
    app_logger.info("Build:%s", platform.python_build())

    # オペレーティングシステム/ハードウェア情報
    app_logger.info("OS:%s", platform.platform())
    app_logger.info("uname:%s", platform.uname())
    app_logger.info("system:%s", platform.system())
    app_logger.info("node:%s", platform.node())
    app_logger.info("release:%s", platform.release())
    app_logger.info("version:%s", platform.version())
    app_logger.info("machine:%s", platform.machine())
    app_logger.info("architecture:%s", platform.architecture())
    app_logger.info("/bin/ls:%s", platform.architecture('/bin/ls'))
