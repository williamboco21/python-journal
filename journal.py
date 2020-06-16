from flask import Flask, render_template, url_for, redirect, request
from datetime import datetime
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

        # Appending the form values
        with open("data.json") as json_file:
            cont = json.load(json_file)

            val = cont["journal"]
            add_id = len(val) + 1
            title = request.form['title']
            date = datetime.now().strftime('%Y-%m-%d')
            body = request.form['body']
            values = {
                "id": add_id,
                "body": body,
                "date": date,
                "title": title
            }
            val.append(values)

            # Writing the contents into the file
            with open(filename, 'w') as f:
                json.dump(cont, f, indent=4, sort_keys=True)
                home = '/home'

            return redirect(home)
    return render_template('add.html')


# Delete Function
@app.route('/delete')
def delete():
    return redirect(url_for('home'))
