from flask import Flask, render_template, url_for, redirect, request
import json

# initializing the application object
app = Flask(__name__)

# loading the JSON data file and parsing
with open('data.json', 'r') as f:
    data = json.load(f)


# Home Decorator
@app.route('/home')
def home():
    return render_template('home.html', data=data)


# Login Decorator
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == "williammboco" and request.form['myPassword'] == "python418":
            return redirect(url_for('home'))
        else:
            error = "You have entered invalid credentials. Please try again."
    return render_template('index.html', error=error)


# Add Function
@app.route('/add', methods=['GET', 'POST'])
def add(filename='data.json'):
    if request.method == "POST":
        title = request.form['title']
        date = request.form['date']
        body = request.form['body']

        with open("data.json") as json_file:
            content = json.load(json_file)
            val = content["journal"]
            values = {
                "body": body,
                "date": date,
                "title": title
            }
            val.append(values)

        with open(filename, 'w') as f:
            json.dump(content, f, indent=4, sort_keys=True)

        return render_template('home.html', data=data)
    return render_template('add.html')


# Delete Function
@app.route('/delete')
def delete():
    return render_template('home.html', data=data)
