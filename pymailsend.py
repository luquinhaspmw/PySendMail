import os
import smtplib as sm
import pandas as pd
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from loading import load
from excel import getDados
from time import sleep
from termcolor import colored

load_dotenv()

def load_template(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def send_emails(reme,dest,passwd,name,subject,date,time,address,phone,company_email,company_name,company_website,fileImage):
    email_host = reme
    passwd_host = passwd
    email_cliente = dest
    
    assunto = subject

    mensagem = load_template('template.html')

    mensagem = mensagem.replace('{{name}}', name)
    mensagem = mensagem.replace('{{date}}', date)
    mensagem = mensagem.replace('{{time}}', time)
    mensagem = mensagem.replace('{{address}}', address)
    mensagem = mensagem.replace('{{company_phone}}', phone)
    mensagem = mensagem.replace('{{company_email}}', company_email)
    mensagem = mensagem.replace('{{company_name}}', company_name)
    mensagem = mensagem.replace('{{company_website}}', company_website)
    
    msg = MIMEMultipart()
    msg['From'] = email_host
    msg['To'] = email_cliente
    msg['Subject'] = assunto

    #Abrindo imagem e adicionando no html
    with open(fileImage, 'rb') as f:
      img_data = f.read()
      image = MIMEImage(img_data)
      image.add_header('Content-ID', '<arte>')
      image.add_header('Content-Disposition','inline',name='arte.png',filename=f'{fileImage}')
      image.add_header('Content-Type', 'image/jpg; name=arte.png')
      msg.attach(image)
      msg.attach(MIMEText(mensagem, 'html'))
	 
    try:
        server = sm.SMTP(os.environ["SMTP_SERVER"], os.environ["SMTP_PORT"])
        server.starttls()
        server.login(email_host, passwd_host)
        texto = msg.as_string()
        server.sendmail(email_host, email_cliente, texto)
        server.quit()
        return True
    except Exception as err:
        print(f"Erro ao enviar email :(\n{str(err)}")
        return False
 
user = os.environ["GMAIL_USER"]
user_pass = os.environ['GMAIL_PASS_APP']

def getPlanilha():    
    arquivo = str(input("Nome da planilha: "))
    dados = getDados(arquivo)
    while type(dados) != pd.core.frame.DataFrame:
      arquivo = str(input("Nome da planilha: "))
      dados = getDados(arquivo)
    
    return dados
   
   
tabela = getPlanilha()
emails = tabela["Email"]
nomes = tabela["Nome"]

cont = 0
load()
sleep(2)
print()
subject = str(input("Assunto: "))


date = '20/11'
time = '15:30'
address = 'Avenida JK'
phone = '639920123456'
company_email = 'emailficticio@gmail.com'
company_name = 'Empresa Ficticia'
company_website = 'empresafictica.com'
arte =  'arte.png'

print()

while cont < len(emails):
    print(f"Enviando email para : {emails[cont]}")
    if send_emails(user,emails[cont],user_pass,nomes[cont],subject,date,time,address,phone,company_email,company_name,company_website,arte):
      print(colored("Sucesso ao enviar email!","green"))
      print("----------------")
    else:
      print("Erro ao enviar email!\n\n")
    cont+=1
