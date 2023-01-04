import smtplib
import sender, config

def createMail(words):

    message = f"Subject: EnglishWords\n\nWords:\n{words}"

    smtpObj = smtplib.SMTP(f'smtp.{sender.mailDomain}.com', config.mailPort)
    smtpObj.starttls()
    smtpObj.login(sender.mailLogin, cred.mailPassword)
    smtpObj.sendmail(sender.mailLogin, cred.emailToSend, message)
    smtpObj.quit()

    print("Mail is sended")