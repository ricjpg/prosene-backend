import os
import smtplib
from email.message import EmailMessage
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))

def send_email(to_email: str, subject: str, template_name: str, template_data: dict, url_reset : str):

    try:
        email_address = os.getenv('email_address')
        email_password = os.getenv('email_password')

        # Cargar la plantilla y renderizarla con datos dinámicos
        template = env.get_template("request_reset.html")
        email_content = template.render(nombre = to_email, reset_url = url_reset)

        # Crear el correo
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email_address
        msg['To'] = to_email
        msg.set_content(email_content, subtype="html")

        # Enviar el correo
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)

        return {"message": "Email successfully sent"}

    except Exception as error:
        print(f"Error sending email: {error}")
        return {"error": "An error occurred while sending the email"}

def welcome_mail(to_email: str, subject: str, template_name: str, template_data: dict, url : str):

    try:
        email_address = os.getenv('email_address')
        email_password = os.getenv('email_password')

        # Cargar la plantilla y renderizarla con datos dinámicos
        template = env.get_template("welcome_page.html")
        email_content = template.render(nombre = to_email, url = url)

        # Crear el correo
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = email_address
        msg['To'] = to_email
        msg.set_content(email_content, subtype="html")

        # Enviar el correo
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)

        return {"message": "Email successfully sent"}

    except Exception as error:
        print(f"Error sending email: {error}")
        return {"error": "An error occurred while sending the email"}
