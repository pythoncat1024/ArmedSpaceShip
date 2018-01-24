#!/usr/bin/env python
# -*-encoding: utf-8 -*-


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# image包可以发送图片形式的附件
# from email.mime.image import MIMEImage

# 可以查询文件对应的'Content-Type'
# import mimetypes
# mimetypes.guess_type('c:\\users\\adminstrator\\desktop\\ceshi.xls')


asender = 'aa@aa.com'
# 多个收件人用逗号隔开
areceiver = 'bb@bb.com, cc@cc.com'
acc = 'dd@dd.com, eeg@ee.com'
asubject = u'HI'

# 阿里云邮箱的smtp服务器
asmtpserver = 'smtp.mxhichina.com'
ausername = 'aa@aa.com'
apassword = '123456'

# 下面的to\cc\from最好写上，不然只在sendmail中，可以发送成功，但看不到发件人、收件人信息
msgroot = MIMEMultipart('related')
msgroot['Subject'] = asubject
msgroot['to'] = areceiver
msgroot['Cc'] = acc
msgroot['from'] = asender

# MIMEText有三个参数，第一个对应文本内容，第二个对应文本的格式，第三个对应文本编码
thebody = MIMEText(u'Please check the attachment, thanks!', 'plain', 'utf-8')
msgroot.attach(thebody)

# 读取xls文件作为附件，open()要带参数'rb'，使文件变成二进制格式,从而使'base64'编码产生作用，否则附件打开乱码
# att = MIMEText(open('C:\\ceshi.xls', 'rb').read(), 'base64', 'GB2312')
# att['Content-Type'] = 'application/vnd.ms-excel'
# att['Content-Disposition'] = 'attachment; filename ="1.xls"'

# 读取xlsx文件作为附件，open()要带参数'rb'，使文件变成二进制格式,从而使'base64'编码产生作用，否则附件打开乱码
att = MIMEText(open(u'C:\\ceshi.xlsx', 'rb').read(), 'base64', 'utf-8')
att['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
# 下面的filename 等号(=)后面好像不能有空格
attname = 'attachment; filename ="123.xlsx"'
att['Content-Disposition'] = attname

msgroot.attach(att)

asmtp = smtplib.SMTP()
asmtp.connect(asmtpserver)
asmtp.login(ausername, apassword)

# 发送给多人时，收件人应该以列表形式，areceiver.split把上面的字符串转换成列表
# 只要在sendmail中写好发件人、收件人，就可以发送成功
# asmtp.sendmail(asender, areceiver.split(','), msgroot.as_string())

# 发送给多人、同时抄送给多人，发送人和抄送人放在同一个列表中
asmtp.sendmail(asender, areceiver.split(',') + acc.split(','), msgroot.as_string())
asmtp.quit()