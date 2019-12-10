# -*- coding:utf-8 -*-

from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
  command = "/etc/init.d/ssh status"
  ping = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
  (output, err) = ping.communicate()
  test = output.split("\n")
  test = test[2].split(" ")
  message = test[4] + " " + test[5]
  print message
  
  return render_template("index.html",teste = message)

if __name__ == '__main__':
  app.run(debug=True,host="0.0.0.0", port=80)


