from tkinter import *

class NLPApp:

    def __init__(self):
        self.root = Tk()
        self.root.title('NLP Application')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#2b4370')
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):

        heading = Label(self.root,text='NLPApp', bg='#2b4370',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text='Enter Email', bg='#2b4370',fg='white')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=35)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text='Enter Password', bg='#2b4370',fg='white')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=35,show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn = Button(self.root,text='Login',width=30,height=2)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member?', bg='#2b4370',fg='white')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now')
        redirect_btn.pack(pady=(10, 10))

    def clear(self):
        # clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()

nlp = NLPApp()