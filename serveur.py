#Programme serveur
import socket
import threading
from datetime import *

#date de creation du serveur
today = date.today()

#Creation de socket serveur avec adresse localhost
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",1234))
s.listen()

#Creation des listes des clients et des usernames de chaqu'un
clients=[]
username=[]

#Fonction qui gere tous les nouveaux utilisateurs qui ce connectent ainsi que leur username
def nouv_client():
    while True:
        nouv, addr = s.accept()
        print(f"Connection from {addr} has been estabished")
        
        nouv.send('Username'.encode('ascii'))
        username_nouv = nouv.recv(1024).decode()
        username.append(username_nouv)
        clients.append(nouv)
        
        print(f'Username of the client {addr} is {username_nouv}')
        envoyer(f'{username_nouv} has joined the chat')
        
        thread= threading.Thread(target=receive, args=(nouv,)) 
        thread.start() #debut du thread infini de la fonction pour qu'elle accepte les utilisateurs sans arret

#Fonction envoyer qui fait passer chaques messages envoyés par un utilisateur a tous les autres
def envoyer(message):
    for e in clients:
        e.send(message.encode())

#Fonction receive qui recoit les messages envoyeé par les utilisateurs
def receive(client):
    while True:
        message = client.recv(1024)
        envoyer(message.decode())
        
      
print(f'{today}: Server has been activated')

#Activation 
nouv_client()
        
    


       
        
       
        
       
  