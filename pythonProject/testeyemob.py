import win32com.client as win32
import time
import os

print("Olá, está aplicação tem como objetivo enviar emails automaticamente.")
print(' ')
time.sleep(5)
def enviar_email():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    destinatario = input("Digite o email do destinatario:")
    mail.to = destinatario

    mail.Subject = 'FEEDBACK GLPI'

    chamado = input("Digite a mensagem:")
    chamado = chamado.replace("\n", "<br>" '\n')

    mail.htmlbody = chamado

    enviar_email = input("Deseja realmente enviar este email? sim(s) ou não(n):")
    if enviar_email.lower() == 's':
        mail.Send()
        print("Email enviado!")
    else:
        print("Email não enviado!")


while True:
    enviar_email()
    enviar_novo = input("Deseja enviar outro email? sim(s) ou não(n):")
    if enviar_novo.lower() != 's':
        print("Encerrando o programa.")
        break
        os.system('clear') or None
    time.sleep(3)