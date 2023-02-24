from dotenv import dotenv_values
import smtplib
from email.message import EmailMessage

env = dotenv_values('utils/.env')


class Email:
    def __init__(self):
        self.email_send: str = 'dantryus@gmail.com'
        self.email_destiny: str = 'danilosantos@nett3c.com.br'
        self.password: str = 'nxamqjnocbdgcfdz'

    def send_email(self, assunto: str, mensagem: str) -> None:
        msg = EmailMessage()
        msg['Subject'] = assunto
        msg['From'] = self.email_send
        msg['To'] = self.email_destiny
        msg.set_content(mensagem)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.email_send, self.password)
            smtp.send_message(msg)


if __name__ == '__main__':
    email = Email()
    email.send_email('teste', 'testando')
