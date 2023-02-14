from flask import Flask, request, redirect, render_template, session, flash, url_for, abort
from network import Network
from wrist import wrist as w
import  webbrowser
import string, random


# Function to generate strings
def def_key(size=50, chars=string.ascii_uppercase+string.digits+string.punctuation+string.ascii_lowercase):
  return ''.join(random.choice(chars) for _ in range(size))

app = Flask(__name__)
app.secret_key = def_key(size=200)

# Configuration index page
@app.route("/")
def index():
  try:
    app.logger.info("Load page success!")
    return render_template("index.html")
  except NameError as e:
    app.logger.error(e)
    abort(404)

@app.route("/css/index.css")
def index_css():
  return render_template("css/index.css")

@app.route("/js/index.js")
def index_js():
  return render_template("js/index.js")

# Configuretion network page
@app.route("/network")
def network():
  try:
    app.logger.info("Load page success! [data: ", session['ips'], ']')
    return render_template("network.html", ips=session['ips'])
  except NameError as e:
    app.logger.error(e)
    abort(404)

@app.route("/css/network.css")
def network_css():
  return render_template("css/network.css")

@app.route("/js/network.js")
def network_js():
  return render_template("js/network.js")

# Configuration port scann page
@app.route('/network/port_scann/')
def port_scann():
  try:
    app.logger.info("Send data with success! [data:{}]".format(session['ips']))
    return render_template('port_scann.html', data=session['data'])
  except NameError as e:
    app.logger.error(e)
    abort(500)

# thumbnail
@app.route("/favicon.ico")
def favincon():
  return render_template("favicon.ico")

# Configuretion scanner
@app.route("/scann/<ips>")
def scann(ips):
  get_ip = ips
  ip = Network(get_ip)
  if ip.check_ip():
    ip.set_networking()
    session['ips'] = ip.networks
    return redirect(url_for('network'))
  else:
    flash('ERROR: IP pattern incorrect')
    return redirect(url_for('index')) 

@app.route("/port_scann", methods=["POST"])
def port_scaning():
  if request.method == 'POST':
    ip = request.form.get('ip')
    ports  = request.form.get('ports')
    if ports:
      if ports == "all_ports":
        data = w(ip=ip, port=[], all=True)
        data.scann()
        session["data"] = data.data
      else:
        ports = list(map(int, ports.split(',')))
        data = w(ip=ip, port=ports, all=False)
        data.scann()
        session["data"] = {"ip":ip, "ports":data.data}
        pass
    webbrowser.open('http://127.0.0.1:5000/network/port_scann')
    return redirect(url_for('static', filename='js/network.js'))
  else:
    return redirect(url_for('network'))

# Error handling
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html', error=e), 404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html', error=e), 500

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
