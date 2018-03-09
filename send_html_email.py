# -*- coding: utf-8 -*-

def send_email(subject, content_text, html_path, to_address_list, cc_address_list):
            import smtplib
            from email.header import Header
            from email.mime.text import MIMEText
            from email.utils import formataddr
            send_obj = smtplib.SMTP('mail.gometech.com.cn', 25) 
            if DEBUG and SHOW_LOG:
                        send_obj.set_debuglevel(1)  # 打印debug日志
                                print(send_obj)  # ok 了
                            # 2. 跟服务器建立连接
                            send_obj.ehlo()
        # 3. 实现加密的必须的步骤
        # send_obj.starttls()

        username = r'pythoncat.cheng@gometech.com.cn'
            password = r'Abcd1234ABC'
                # ---- 发送 html 格式的邮件----
                f = open(html_path, 'r', 'utf-8')
                    mail_body = f.read()
        f.close()
        pre__format = '<pre style="font-size:medium">{}</pre>'.format(content_text)
            msg = MIMEText(content_text + mail_body, 'html', 'utf-8')
                msg['From'] = formataddr(["Jenkins Daemon", r'pythoncat.cheng@gometech.com.cn'])  # 设置发件人昵称
                    msg['To'] = ",".join(to_address_list)
                        msg['Cc'] = ",".join(cc_address_list)
                            msg['Subject'] = Header(subject, 'utf-8').encode()

                                login_result = send_obj.login(username, password)
        # 4. 发送邮件
        send_result = send_obj.sendmail(username,
                                                    to_address_list + cc_address_list,
                                                                                        msg.as_string())
        # 5. 发送完成，退出
        quit_result = send_obj.quit()
        if DEBUG and SHOW_LOG:
                print(login_result, send_result, quit_result)

