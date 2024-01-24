from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# E-Mail Config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'matheus.correa2k20@gmail.com'
app.config['MAIL_PASSWORD'] = 'mgiz scwn cpuq ftrm'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/cv')
def cv():
    return render_template('cv.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        send_email(name, email, message)

        return redirect(url_for('confirmation'))
    return render_template('contact.html')

def send_email(name, email, message):
    msg = Message(
        subject='Novo Contato',
        recipients=['matheuscorrea.2023@outlook.com'],
        sender='matheus.correa2k20@gmail.com'
    )
    msg.body = f'Nome: {name}\nEmail: {email}\nMessage: {message}'

    mail.send(msg)

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)
