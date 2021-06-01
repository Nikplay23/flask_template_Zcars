from flask import Flask, render_template
app = Flask('app')


@app.route('/')
def galvena():
  return render_template("galvena.html")

@app.route('/kontakti')
def kontakti():
  return render_template("kontakti.html")

@app.route('/parasta zona')
def parasta_zona():
  return render_template("parasta zona.html")

@app.route('/rezervēšana')
def rezervēšana():
  return render_template("rezervēšana.html")

@app.route('/vip')
def vip():
  return render_template("vip.html")


app.run(host='0.0.0.0', port=8080)