# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     send_email
   Description :
   Author :       cat
   date：          2018/1/24
-------------------------------------------------
   Change Activity:
                   2018/1/24:
-------------------------------------------------
# pythoncat.cheng@gometech.com.cn
"""


def send_email(subject, content_text):
    import smtplib
    from email.header import Header
    from email.mime.text import MIMEText

    sendObj = smtplib.SMTP('mail.gometech.com.cn', 25)
    sendObj.set_debuglevel(1)  # 打印debug日志
    print(sendObj)  # ok 了
    # 2. 跟服务器建立连接
    sendObj.ehlo()
    # 3. 实现加密的必须的步骤
    # sendObj.starttls()

    username = r'pythoncat.cheng@gometech.com.cn'
    password = r'Abcd1234ABC'

    msg = MIMEText(content_text, 'plain', 'utf-8')
    # msg['From'] = _format_addr('我是发件人 <%s>' % from_addr)
    msg['To'] = ",".join([r'pythoncat.cheng@gometech.com.cn', r'xin.ni@gometech.com.cn'])
    msg['Cc'] = ",".join([r'xing.liu@gometech.com.cn'])
    msg['Subject'] = Header(subject, 'utf-8').encode()

    login_result = sendObj.login(username, password)

    send_result = sendObj.sendmail(username, [r'pythoncat.cheng@gometech.com.cn', r'xin.ni@gometech.com.cn'] + [
        r'xing.liu@gometech.com.cn'],
                                   msg.as_string())
    quit_result = sendObj.quit()
    print(login_result, send_result, quit_result)


if __name__ == "__main__":
    content = r"""GMOS2.X 01月24日 每日版本已经上传服务器：
请大家拷贝到本地刷机，不要直接用下面共享路径下刷机

开发分支版本：
user:\\192.168.59.62\release\dailybuild\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop\2018-01-24-04-04-34_user
userdebug：\\192.168.59.62\release\dailybuild\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop\2018-01-24-04-10-53_userdebug

登录方法：\\192.168.59.62   用户名：build 密码：build


南京服务器地址：
user: \\192.168.63.218\share\dailybuild\SH-ReleaseVersion\tk6757_66_n1\GM12B_7.1_mtk6757cd_develop\2018-01-24-04-04-34_user"""

    send_email("测试自动发送邮件", content)
