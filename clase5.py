#Esta funcion
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def crearbot():
    proyecto=input('nombre del chatbot: ')
    os.mkdir(proyecto)
    os.mkdir(proyecto+'/'+proyecto)
    namechatbot='./'+proyecto+'/'+proyecto+'.yml'
    file=open(namechatbot, "w")

    categoria=input ('Escriba una categoria: ')
    file.write('categoria:' +os.linesep)
    file.write('-'+categoria+os.linesep)

    while True:
        continuar=input('Desea agregar otra: \n 1- Agregar \n 2- Teminal ')
        if continuar =='1':
            pregunta=input('Pregunta')
            respuesta=input('Respuesta')

            file.write('--'+pregunta+os.linesep)  # -- representa el estimulo
            file.write(' -'+respuesta+os.linesep) # - representa la respuesta al estimulo

        if continuar=='2':
            file.close()
            break
        
    namechatbot= './'+proyecto+'/'+proyecto+'.py'
    file=open(namechatbot,"w")
    file.write("from chatterbot import ChatBot\nfrom chatterbot.trainers import ListTrainer\nimport os\nbot=ChatBot('"+proyecto+"')\ntrainer=ListTrainer(bot)\n"+ os.linesep)
    file.write("for files in os.listdir('./"+proyecto+"/'): \n    data=open('./"+proyecto+"/'+files,'r').readlines()\n trainer.train(data)\n    trainer.train(data)\n    trainer.train(data)\n"+ os.linesep)
    file.close()

crearbot()
