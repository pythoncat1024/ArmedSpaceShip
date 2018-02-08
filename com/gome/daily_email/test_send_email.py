#!/usr/bin/env python
# -*-encoding: utf-8 -*-


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

target = 123


def change():
    global target
    target += 11

    s = 0
    print(s, target)

change()
