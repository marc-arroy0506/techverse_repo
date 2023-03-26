from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_pressed')
def button_pressed():
    return render_template('form.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    downspeed = request.form['download']
    upspeed = request.form['upload']


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
