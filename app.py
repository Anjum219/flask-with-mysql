from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml

# configure DB
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        # fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
