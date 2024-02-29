from tkinter import *
from db import Database
from tkinter import messagebox
from api import API

class NLPApp:

    def __init__(self):

        # create db object
        self.dbo = Database()
        self.apio = API()

        self.root = Tk()
        self.root.title('NLP Application')
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('350x600')
        self.root.configure(bg='#2b4370')
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root,text='NLP App', bg='#2b4370',fg='white')
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

        login_btn = Button(self.root,text='Login',width=30,height=2, command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member?', bg='#2b4370',fg='white')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Register Now', bg='#2b4370', command=self.register_gui)
        redirect_btn.pack(pady=(10, 10))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#2b4370',fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name', bg='#2b4370',fg='white')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=35)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text='Enter Email', bg='#2b4370',fg='white')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=35)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text='Enter Password', bg='#2b4370',fg='white')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=35, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='Register', width=30, height=2, command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?', bg='#2b4370',fg='white')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Now', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def perform_registration(self):
        # fetch data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success','Registration successful. You can login now')
        else:
            messagebox.showerror('Error','Email already exists')

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('success','Login successful')
            self.home_gui()
        else:
            messagebox.showerror('error','Incorrect email/password')

    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#2b4370',fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4, command=self.ner_gui)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4, command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#2b4370',fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#2b4370', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text', bg='#2b4370', fg='white')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='', bg='#2b4370', fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        go_back_btn = Button(self.root, text='Go Back', command=self.home_gui)
        go_back_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''
        for sentiment_category, score in result['sentiment'].items():
            txt += f"{sentiment_category} -> {str(score)}\n"

        print(txt)
        self.sentiment_result['text'] = txt
    
    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#2b4370',fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition', bg='#2b4370', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text', bg='#2b4370', fg='white')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text='Analyze NER', command=self.do_ner)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='#2b4370', fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 16))

        go_back_btn = Button(self.root, text='Go Back', command=self.home_gui)
        go_back_btn.pack(pady=(10, 10))

    def do_ner(self):

        text = self.ner_input.get()
        result = self.apio.ner(text)

        txt = ''
        count = 1
        for i in result['entities']:
            txt += f'{str(count)}\n'
            count += 1
            for ner_category,name in i.items():
                txt += f"{ner_category} -> {str(name)}\n"

        print(txt)
        self.ner_result['text'] = txt

    def emotion_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='#2b4370',fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Analysis', bg='#2b4370', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text', bg='#2b4370', fg='white')
        label1.pack(pady=(10, 10))

        self.emo_input = Entry(self.root, width=50)
        self.emo_input.pack(pady=(5, 10), ipady=4)

        emo_btn = Button(self.root, text='Analyze Emotion', command=self.do_emo)
        emo_btn.pack(pady=(10, 10))

        self.emo_result = Label(self.root, text='', bg='#2b4370', fg='white')
        self.emo_result.pack(pady=(10, 10))
        self.emo_result.configure(font=('verdana', 16))

        go_back_btn = Button(self.root, text='Go Back', command=self.home_gui)
        go_back_btn.pack(pady=(10, 10))

    def do_emo(self):

        text = self.emo_input.get()
        result = self.apio.emotion_prediction(text)

        txt = ''
        for emotion_category, score in result['emotion'].items():
            txt += f"{emotion_category} -> {str(score)}\n"

        print(txt)
        self.emo_result['text'] = txt

    def clear(self):
        # clear the existing gui
        for i in self.root.pack_slaves():
            i.destroy()

nlp = NLPApp()