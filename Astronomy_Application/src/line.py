# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:08:35 2020

@author: sample
"""

import requests
import config


headers = {'Authorization': 'Bearer ' + config.line_notify_token}  # 発行したトークン


def send_message(mesg):
    payload = {'message': mesg}
    line_notify = requests.post(config.line_notify_api, data=payload, headers=headers)


def send_image(mesg, file):
    payload = {'message': mesg}
    files = {"imageFile": open(file, "rb")}
    line_notify = requests.post(config.line_notify_api, data=payload, headers=headers, files=files)


def send(mesg, file):
    payload = {'message': mesg}
    files = {"imageFile": open(file, "rb")}
    line_notify = requests.post(config.line_notify_api, data=payload, headers=headers, files=files)
