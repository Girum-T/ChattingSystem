#Program client2
import socket
import threading
from datetime import *

#Variable de l'heure actuelle
now = datetime.now()
current_time = now.strftime("%H:%M")

#Enregistrement du username de l'utilisateur
username= input('Username?')
addresse = ("127.0.0.1",1234)

#Connection a l'adresse du serveur 
cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cl.connect(addresse)

#Fonction qui recoit tout les messages envoyés par les autres utilisateurs (qui passe par le serveur)
def receive():
    while True:
       msg = cl.recv(1024).decode()
       if msg=="Username":
            cl.send(username.encode())
       else:
            print(msg)


#Fonction qui envoie des messages au serveur, qui sont ensuite transmis aux autres utilisateurs
def envoyer():
    while True:
        message= f''' {username}:
                          {input("")}
                          {current_time}'''
        cl.send(message.encode())
        
#Debut des threads pour que l'utilisateur peut tout le temps envoyé et recevoir des messages.
receive_thread = threading.Thread(target= receive)
receive_thread.start()

envoyer_thread = threading.Thread(target= envoyer)
envoyer_thread.start()