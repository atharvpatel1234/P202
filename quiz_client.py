import socket
from threading import Thread
from tkinter import *

nickname=input("Choose Your Nickname : ")
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip_address= '127.0.0.1'
port= 8001

client.connect((ip_address, port))

print("Connected with the server...")

class GUI:
    def __init__(self):
        self.Window=Tk()
        self.Window.withdraw()

        self.login=Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,height=False)
        self.login.configure(width=400,height=400)


        self.loginlabel=Label(self.login,text='Please Login To Continue',fg='black',bg='white',font=("Calibri",15),justify="center")
        self.loginlabel.place(x=75,y=40)


        self.Namelabel=Label(self.login,text='Name : ',fg='black',font=("Calibri",15),justify="center")
        self.Namelabel.place(x=50,y=120)


        self.name=Entry(self.login,text='',fg='black',font=("Calibri",12),justify="center",bd=5)
        self.name.place(x=180,y=120)
        self.name.focus()


        self.button=Button(self.login,text='CONTINUE',fg='black',bg='grey',font=("Helvetica bold",15),justify="center",command=lambda:self.goAhead(self.name.get()))
        self.button.place(x=120,y=200)

        self.Window.mainloop()

    def goAhead(self,name):
        self.login.destroy()
        self.name=name
        rcv=Thread(target=self.receive)
        rcv.start()


    def receive(self):
        while True:
            try:
                message=client.recv(2048).decode('utf-8')
                if message == "NICKNAME":
                    client.send(nickname.encode('utf-8'))
                else:
                    pass   
            except:
                print("An Error Occurred")
                client.close()
                break

def write():
     while True:
        message = '{}: {} '.format(nickname, input(''))
        client.send(message.encode('utf-8'))
        
v=GUI() 

#receive_thread = Thread(target=receive)
#receive_thread.start()
#write_thread = Thread(target=write)
#write_thread.start()
