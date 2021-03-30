from flask import render_template, url_for, request, redirect, session, flash
from app import app

# class higor:
#     def __init__(self):
#         self.id = 1
#         self.remetente = 'fulano@email.com'
#         self.destinatários=['fulano1@email','fulano21@email']
#         self.horário = '12:30'
#         self.assunto= 'Asunto asunto'
#         self.corpo = 'vamos caminhar no bosque em quanto seu lobo nao vem'

@app.route('/')
def index():
    return render_template('tela1.html')

@app.route('/tela2')
def tela2():
    nomes = [1,2,3]
    return render_template('tela2.html',nomes=nomes)

@app.route('/tela3')
def tela3():
    return render_template('tela3.html')