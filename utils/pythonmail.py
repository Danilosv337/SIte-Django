from dotenv import dotenv_values
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

env = dotenv_values('utils/.env')


class Email:
    def __init__(self):
        self.email_send: str = 'dantryus@gmail.com'
        self.email_destiny: str = 'danilosantos@nett3c.com.br'
        self.password: str = 'nxamqjnocbdgcfdz'

    def send_email(self, assunto: str, referencia1: str, referencia2: str, mensagem: str) -> None:
        msg = MIMEMultipart('alternativo')
        msg['Subject'] = assunto
        msg['From'] = self.email_send
        msg['To'] = self.email_destiny

        html = \
        '''
        <!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email HTML</title>
    <style>
        body{
            background-color: #96b9d9;
            color: rgb(25, 25, 25);
        }
        .block{
            position: absolute;
            top: 50px;
            left: 5%;
            padding: 25px;
            width: 85%;
            border-radius: 10px;
            background-color: white;
        }
        h1{
            text-align: center;
            color: #435373;
        }
        .informacao{
            font-size: 2rem;
            padding-left: 20px;
        }
        p{
            text-align: center;
            margin: 0 auto;
            width: 80%;
        }
    </style>
</head>
<body>
    <div class="block">
    <div class="informacao">
        <h1>Email Do Projeto SiteDjango</h1>
        <ul>
            <li>Nome Do Contato: #referencia_1#</li>
            <li>Email Do contato: #referencia_2#</li>
        </ul>
    </div>
    <div>
        <p>#mensagem#</p>
    </div>
    </div>
    
</body>
</html>
        '''

        html = html.replace("#referencia_2#",referencia1).replace('#referencia_1#',referencia2).replace('#mensagem#',mensagem)

        conteudo = MIMEText(html,'html')
        msg.attach(conteudo)


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.email_send, self.password)
            smtp.send_message(msg)


