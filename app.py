from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USER")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
mail.init_app(app)

@app.route("/", methods=["GET", "POST"])
def home():
    form = ContactForm()
    
    # if method is POST
    if request.method == "POST":
        if form.validate() == False:
            flash("All fields are required.")
            return render_template("index.html", form=form, scroll=True)
        else:   
            msg = Message("Portfolio", sender="coxjosh.tr@gmail.com", recipients=["joshcox2@hotmail.com"])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            flash("Email successfully sent.")
            return render_template("index.html", form=form, scroll=True, success=True)
    # if method is GET
    elif request.method == "GET":
        return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
    