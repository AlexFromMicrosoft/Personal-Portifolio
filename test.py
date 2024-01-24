from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações do Flask-Mail (substitua esses valores pelos seus)
app.config['MAIL_SERVER'] = 'seu_servidor_smtp'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'seu_email'
app.config['MAIL_PASSWORD'] = 'sua_senha'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Inicializa a extensão Flask-Mail
mail = Mail(app)