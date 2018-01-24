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


def send_email(subject, content_text, to_address_list, cc_address_list):
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
    msg['To'] = ",".join(to_address_list)
    msg['Cc'] = ",".join(cc_address_list)
    msg['Subject'] = Header(subject, 'utf-8').encode()

    login_result = sendObj.login(username, password)
    # 4. 发送邮件
    send_result = sendObj.sendmail(username, to_address_list + cc_address_list,
                                   msg.as_string())
    # 5. 发送完成，退出
    quit_result = sendObj.quit()
    print(login_result, send_result, quit_result)


if __name__ == "__main__":
    is12e = True
    debug = True
    to_address_lists = [r'pythoncat.cheng@gometech.com.cn',
                        r'xing.liu@gometech.com.cn',
                        r'yun.tang@gometech.com.cn',
                        r'kun.wang@gometech.com.cn',
                        r'yuqi.jiang@gometech.com.cn',
                        r'ruiming.yao@gometech.com.cn',
                        r'kaifeng.wang@gometech.com.cn',
                        r'fei.zhao@gometech.com.cn',
                        r'jie.jiang@gometech.com.cn',
                        r'qiang.li@gometech.com.cn',
                        r'xueliang.chen@gometech.com.cn',
                        r'wenjiang.yang@gometech.com.cn',
                        r'lei.wang1@gometech.com.cn',
                        ]
    cc_address_lists = [r'iuv.swt@gometech.com.cn',
                        r'nina.wu@gometech.com.cn',
                        r'yupeng.zhang@gometech.com.cn',
                        r'iuv.swnj@gometech.com.cn',
                        r'iuv.sw-support@gometech.com.cn',
                        r'iuv.sw@gometech.com.cn',
                        ]
    subject = r"回复: GM12E每日版本" if is12e else r"回复: GMOS2.X[GM12B_7.1_mtk6757cd_develop]每日版本"

    if debug:
        to_address_lists = [r'pythoncat.cheng@gometech.com.cn',
                            r'xin.ni@gometech.com.cn',
                            # r'xing.liu@gometech.com.cn',
                            r'jiaren.li@gometech.com.cn'
                            ]
        cc_address_lists = [
            r'shengfu.huang@gometech.com.cn',
            r'wei.quan@gometech.com.cn'
        ]
        subject = "测试邮件，请勿回复..."+subject
    # todo: 准备工作完成，开始发邮件吧
    from dailyEmail import daily_email_info

    content = daily_email_info.send_info(is12e)

    # print(subject, content, to_address_lists, cc_address_lists)
    send_email(subject, content, to_address_lists, cc_address_lists)
