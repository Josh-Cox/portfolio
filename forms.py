from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
  name = StringField("Name", validators=[InputRequired()], render_kw={
      "placeholder": "Name"
  })
  email = StringField("Email", validators=[InputRequired(), Email()], render_kw={
      "placeholder": "Email"
  })
  message = TextAreaField("Message", validators=[InputRequired()], render_kw={
      "placeholder": "Message"
  })
  submit = SubmitField("Send") 
