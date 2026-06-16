from flask import Flask , render_template
app = Flask(__name__)

posts = [
    {
        'author' : 'Ishaan Arekar',
        'title' : 'blog post 1',
        'content' : 'blog post 1 content',
        'date_posted' : '21st April, 2026'

    },
    {

        'author' : 'test',
        'title' : 'blog post 2',
        'content' : 'blog post 2 content',
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
    app.run(debug=True)
