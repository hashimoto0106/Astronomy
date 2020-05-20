# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:53:21 2020

@author: sample
"""

import configparser


INI_FILE = '../parameter/config.ini'

inifile = configparser.ConfigParser()
inifile.read(INI_FILE, 'UTF-8')

# パラメータ取得
# [config]
config_log = inifile.get('config', 'log')

# [syslog]
syslog_facility = inifile.get('syslog', 'facility')
syslog_option = inifile.get('syslog', 'option')

# [database]
database = inifile.get('database', 'database')

# [line]
line_notify_api = inifile.get('line', 'notify_api')
line_notify_token = inifile.get('line', 'notify_token')

# [observation]
observation_target = inifile.get('observation', 'target')
observation_start_time = inifile.get('observation', 'start_time')
observation_time_hr = inifile.getfloat('observation', 'time_hr')
observation_interval_hr = inifile.getfloat('observation', 'interval_hr')
observation_location_latitude = inifile.get('observation', 'location_latitude')
observation_location_longitude = inifile.get('observation', 'location_longitude')
observation_target_ra = inifile.get('observation', 'target_ra')
observation_target_dec = inifile.get('observation', 'target_dec')


def init():
    print()


def logging_paramter():
    import logger
    logger.app_logger.debug("config_log:%s", config_log)
    logger.app_logger.debug("syslog_facility:%s", syslog_facility)
    logger.app_logger.debug("syslog_option:%s", syslog_option)
    logger.app_logger.debug("database:%s", database)
    logger.app_logger.debug("line_notify_api:%s", line_notify_api)
    logger.app_logger.debug("line_notify_token:%s", line_notify_token)
    logger.app_logger.debug("observation_target:%s", observation_target)
    logger.app_logger.debug("observation_start_time:%s", observation_start_time)
    logger.app_logger.debug("observation_time_hr:%s", observation_time_hr)
    logger.app_logger.debug("observation_interval_hr:%s", observation_interval_hr)
    logger.app_logger.debug("observation_location_latitude:%s", observation_location_latitude)
    logger.app_logger.debug("observation_location_longitude:%s", observation_location_longitude)
    logger.app_logger.debug("observation_target_ra:%s", observation_target_ra)
    logger.app_logger.debug("observation_target_dec:%s", observation_target_dec)
