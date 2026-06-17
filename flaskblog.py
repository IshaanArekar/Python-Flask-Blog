from flask import Flask , render_template, url_for
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True, port= 5001)
