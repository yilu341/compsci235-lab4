from flask import  Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/user/<name>')
def show_name(name):
    return f'{name}, Welcome to lab 4'


@app.route('/results/<mark>')
def mark(mark):
    if int(mark) >= 90:
        return "You have got a grade of: A+)"
    elif int(mark) >= 80:
        return "You have got a grade of: A+)"
    elif int(mark) >= 60:
        return "You have got a grade of: B)"
    else:
        return  "You failed the exam."

if __name__ == '__main__':
    app.run(debug=True, port=8000)