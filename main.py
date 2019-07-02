from flask import Flask,request, make_response, redirect, render_template,session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'
todos = ['todo 1', 'todo2', 'todo3']


class LoginForm(FlaskForm):
  username = StringField("Nombre de Usuario", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired()])
  submit = SubmitField("Enviar")

@app.errorhandler(404)
def not_found(err):
  return "error "+str(err)

@app.route('/')
def index():
  user_ip = request.remote_addr
  response = make_response(redirect('/hello'))
  session['user_ip'] =user_ip
  return response


@app.route('/hello', methods=['GET','POST'])
def Hello():

  user_ip = session.get('user_ip')
  context ={
    'user_ip':user_ip,
    'todos': todos,
    'login': LoginForm()
  }
  print(context)
  return render_template('hello.html', **context)



if __name__ == "__main__":
  app.run(debug=True)