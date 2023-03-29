from flask import Flask, render_template, request
import configparser
import os

new_dir_path = 'C:\\Users\\mcarr\\Documents'

os.chdir(new_dir_path)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_pressed')
def button_pressed():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    config = configparser.ConfigParser()
    downspeed = request.form['download']
    upspeed = request.form['upload']

    a = downspeed
    b = upspeed
    myOutput = open('config.ini', 'w')
    myOutput.write("Configuration Download: " + str(a) + " Mbps" + '\n')
    myOutput.write("Configuration Upload: " + str(b) + " Mbps" + '\n')
    myOutput.close()
    # Write the config object to a file
    # Do something with the form data
    # For example, send an email
    return 'Setting submitted successfully!'

@app.route('/date_range')
def date_range():
    return render_template('dateRange.html')

@app.route('/signal_strength')
def signal_strength():
    return render_template('signal_strength.html')

@app.route('/targetRouter')
def targetRouter():
    return render_template('target_router.html')

@app.route('/user_Account')
def user_Account():
    return render_template('user_account.html')


if __name__ == '__main__':
  app.run(debug=True)
