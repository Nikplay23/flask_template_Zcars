from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def sakums():
  return render_template("sakums.html")

@app.route('/kontakti')
def kontakti():
  return render_template("kontakti.html")

@app.route('/parasta zona')
def parasta_zona():
  return render_template("parasta_zona.html")

@app.route('/rezervēšana')
def rezervesana():
  return render_template("rezervesana.html")

@app.route('/vip')
def vip():
  return render_template("vip.html")

app.run(host='0.0.0.0', port=8080)