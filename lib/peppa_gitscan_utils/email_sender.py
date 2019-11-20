# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from itsdangerous import URLSafeTimedSerializer
import settings


def create_confirmation_token(email):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    return serializer.dumps(email, salt=settings.SECURITY_PASSWORD_SALT)


def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    try:
        email = serializer.loads(
            token,
            salt=settings.SECURITY_PASSWORD_SALT,
            max_age=expiration
        )
    except:
        return False
    return email


def mail_sender(subject, template):
    receivers = settings.MAIL_RECEIVER
    mail_host = settings.MAIL_SERVER
    mail_user = settings.MAIL_USERNAME
    mail_pass = settings.MAIL_PASSWORD
    subject = subject

    msg = MIMEText(template, 'html', 'utf-8')
    msg['subject'] = Header(subject, 'utf-8')
    msg['from'] = 'Sky ja<%s>' % settings.MAIL_DEFAULT_SENDER
    msg['To'] = ';'.join(map(lambda x: '<' + x + '>', receivers))

    s = smtplib.SMTP(timeout=5)
    s.connect(mail_host, 587)
    s.starttls()
    s.login(mail_user, mail_pass)
    s.sendmail(mail_user, receivers, msg.as_string())  # 发送邮件
    s.close()

