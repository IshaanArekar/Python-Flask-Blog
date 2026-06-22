from flask import Flask , render_template, url_for, flash, redirect
from dotenv import load_dotenv
import os
from forms import RegistrationForm, LogInForm

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')




posts = [
    {
        'author' : 'Ishaan Arekar',
        'title' : 'Blog post 1',
        'content' : 'Blog post 1 content',
        'date_posted' : '21st April, 2026'

    },
    {

        'author' : 'test',
        'title' : 'Blog post 2',
        'content' : 'Blog post 2 content',
        'date_posted' : '21st April, 2023'

    }
    ]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form = form , title = 'Register')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True, port= 5001)
