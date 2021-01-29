from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "<head><title>IllyaBot</title></head><h1>Estado: Online!</h1><a href='https://pastebin.com/e6ShLfj1'>Comandos</a>"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()