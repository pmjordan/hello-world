from flask import Flask
from flask import render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/page')
def test():
    myfilm = {'title': 'Bullet'}
    films = [
        {
            'title': 'John',
            'year': '1994'
        },
        {
            'title': 'Bullet',
            'year': '1994'
        }
    ]
    return render_template('newPage.html', myfilm=myfilm, films=films)
