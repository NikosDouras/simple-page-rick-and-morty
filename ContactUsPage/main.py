from flask import Flask, request, render_template
import smtplib

MY_EMAIL = 
RECEIVER = 
MY_PASSWORD = 

def send_email(name, email, message):
    email_message = f"Subject:New Message from {name} \n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, RECEIVER, email_message)

        
    email_message2 = f"Subject:Thank you{name}! \n\nWe received your message and we 'll email you back soon!" \
                     f" Below you 'll find a copy of your message, have a nice day!\n\nMessage:'{message}'"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, email, email_message2)

app = Flask(__name__)


@app.route("/contact")
def a():

    return render_template("main_page.html")

@app.route("/thanks", methods=["POST"])
def b():
    username = request.form["username"]
    email = request.form["email"]
    message = request.form["message"]
    send_email(username, email, message)
    return render_template("thank_you.html")



if __name__=="__main__":
    app.run(debug=True)

