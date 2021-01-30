from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "<head><title>IllyaBot</title></head><img src='https://littlecloudcuriosity.files.wordpress.com/2014/07/fate-kaleid-liner-prisma-illya-2wei-episode-2-21.jpg' style='height:50vh; max-width:50%; object-fit: contain;'><h1>Estado: Online</h1><a href='https://pastebin.com/e6ShLfj1'>Comandos</a><br><a href='https://discord.com/api/oauth2/authorize?client_id=803354223538208869&permissions=8&scope=bot'>Añadir a tu servidor</a>"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()