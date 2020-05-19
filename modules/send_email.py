import smtplib


class SendEmail:
    def __init__(self):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("sudhagardon62@gmail.com", "email_password")
        message = "hello"
        s.sendmail("sudhagardon62@gmail.com", "pranav12feb@gmail.com", message)
        s.quit()
