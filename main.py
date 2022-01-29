from flask import Flask, render_template
app = Flask('app')

@app.route('/log_in')
def login():
  return render_template("log_in.html")
  
@app.route('/')
def reservation():
  return render_template("reservation.html")

app.run(host='0.0.0.0', port=8080)