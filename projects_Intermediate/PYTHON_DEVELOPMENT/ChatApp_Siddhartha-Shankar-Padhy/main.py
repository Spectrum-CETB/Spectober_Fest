from tkinter import *
from threading import *
import socket
import threading
import os

BACKGR_COLOR = "#1e3d59"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica"

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

class ChatApp:
    def __init__(self, username):
        self.window = Tk()
        self.setup_main_window()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(ADDR)
        self.username = username

        recv_thread = threading.Thread(target=self.recv_messages)
        recv_thread.start()

    def run(self):
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop(0)

    def setup_main_window(self):
        self.window.title("ChatApp")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=400, height=510, bg=BACKGR_COLOR)

        #head bar
        headbar = Label(self.window, text=username, bg="#201e20", fg=TEXT_COLOR, justify=LEFT, font=(FONT,16,"bold"))
        headbar.place(relx=0.4, rely=0.06, anchor=CENTER, width=300, height=37)

        #participants button
        self.participants_btn = Button(self.window,text="Participants",bg="#d71b3b",fg="white",disabledforeground="white", justify=CENTER, command=self.get_participants)
        self.participants_btn.place(relx=0.88,rely=0.06, anchor=CENTER, width=78, height=37)
    
        #border outline
        outline = Label(self.window, height=18)
        outline.place(relx=0.5, rely=0.5, anchor=CENTER, width=380, height=390)

        #main text field
        self.text_field = Text(self.window, wrap=WORD, bg="#000000", fg=TEXT_COLOR, state=DISABLED)
        self.text_field.place(relx=0.5,rely=0.5, anchor=CENTER, width=370, height=380)

        #user input field
        self.input_field = Entry(self.window,borderwidth=3, relief="sunken", justify=CENTER, font=(FONT, 14), bg="#f5f0e1")
        self.input_field.place(relx=0.42, rely=0.94, anchor=CENTER, height=40, width=312)
        self.input_field.focus()

        #scrollbar
        scrollbar = Scrollbar(self.text_field)
        scrollbar.place(relheight=1,relx=0.974)
        scrollbar.configure(command=self.text_field.yview)
        
        #SEND button
        self.start_btn = Button(self.window,text="SEND",bg="#228B22",fg="white",disabledforeground="white", padx=30, command=self.send_msg)
        self.start_btn.place(relx=0.9,rely=0.94, anchor=CENTER, width=57, height=43)
    
    #sends message to the server and prints the message to senders text field
    def send_msg(self):
        msg = self.input_field.get()
        self.input_field.delete(0,END)
        if msg != "":
            own_msg = "You: "+msg+"\n"
            sending_msg = self.username + ": "+msg

            self.client.send(sending_msg.encode(FORMAT))
            self.text_field.configure(state=NORMAL)
            self.text_field.insert(END,own_msg)
            self.text_field.configure(state=DISABLED)
            self.text_field.see("end")

    #receive messages from the server
    def recv_messages(self):
        while True:
            try:
                msg = self.client.recv(1024).decode(FORMAT)
                #try if the participants list has been received
                try:
                    list_msg = eval(msg)
                    self.view_participants(list_msg)
                    continue
                except:
                    pass

                #send username to the server
                if msg == 'USER':
                    self.client.send(self.username.encode(FORMAT))

                #simple messages received
                else:
                    self.text_field.configure(state=NORMAL)
                    self.text_field.insert(END,msg+"\n")
                    self.text_field.configure(state=DISABLED)
                    self.text_field.see("end")

            except Exception as e:
                print(f"Error while receiving messages: {e}")
                self.client.close()
                break
    
    #send a message asking for participants list
    def get_participants(self):
        self.client.send('$$PARTICIPANTS$$'.encode(FORMAT))

    #open a new window displaying the participants
    def view_participants(self, part_list):
        self.part_window = Toplevel()
        self.part_window.title("Participants")
        self.part_window.configure(width=400, height=510, bg="#353935")

        Label(self.part_window,bg="#36454F",fg="#FFFFFF",text="CONNECTIONS",font=('Arial',16)).place(relx=0.5,rely=0.06,width=300,height=50,anchor=CENTER)

        listbox = Listbox(self.part_window, height = 10, width = 15, bg = "#36454F",fg="#FFFFFF",font=('Arial',16))

        count=0
        for member in part_list:
            listbox.insert(count, member)
            count=count+1

        listbox.place(relx=0.5,rely=0.53,width=300,height=430,anchor=CENTER)

    def on_closing(self):
        os._exit(1)

if __name__=="__main__":
    username = input("Username: ")
    app = ChatApp(username)
    app.run()