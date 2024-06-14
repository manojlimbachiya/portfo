from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText


app = Flask(__name__)

port = 587
smtp_server = "smtp.gmail.com"
login = "myapp@gmail.com"
password = "********"  
my_email = "myapp@gmail.com"

@app.route("/")
def main():
    return render_template('./index.html')

@app.route("/home")
def home():
    return render_template('./index.html')

@app.route("/net")
def net():
    return render_template('./net-details.html')

@app.route("/sql")
def sql():
    return render_template('./sql-details.html')

@app.route("/devops")
def devops():
    return render_template('./devops-details.html')

@app.route("/python")
def python():
    return render_template('./python-details.html')

@app.route("/angular")
def angular():
    return render_template('./angular-details.html')

@app.route("/contact_submit",methods=['POST','GET'])
def contact_submit():
    if request.method == 'POST':
        data = request.form.to_dict();
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        emailmessage = MIMEText(message, "plain")
        emailmessage["Subject"] = subject + '-' + name
        emailmessage["From"] = email
        emailmessage["To"] = my_email
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()  # Secure the connection
            server.login(login, password)
            server.sendmail(email, my_email, emailmessage.as_string())

        return render_template('./index.html')