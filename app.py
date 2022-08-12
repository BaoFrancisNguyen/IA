from tkinter import *
import webbrowser


class MyApp:

    def __init__(self):
        self.window = Tk()
        self.window.title("My Application")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        #self.window.iconbitmap("/home/francis/Github/IA/logo.ico")
        self.window.config(background='#41B77F')

        # initialization des composants
        self.frame = Frame(self.window, bg='#41B77F')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)

    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create_field_input()
        self.create_generate_button()
        
    def create_field_input(self):
        donnee_1_text = Label(text = "donnée1 * ",)
        donnee_2_text = Label(text = "donnée2 * ",)
        iteration = Label(text = "Itérations")
        donnee_1_text.place(x=15, y=70)
        donnee_2_text.place(x=15, y=140)
        iteration.place(x=15, y=220)
        donnee_1_text = IntVar()
        donnee_2_text = IntVar()
        iteration = IntVar()
        donnee_1_text_entree = Entry(textvariable=donnee_1_text)
        donnee_2_text_entree = Entry(textvariable=donnee_2_text)
        iteration_entree = Entry(textvariable=iteration)
        donnee_1_text_entree.place(x=15, y=100)
        donnee_2_text_entree.place(x=15, y=180)
        iteration_entree.place(x=15, y=240)


    def create_title(self):
        label_title = Label(self.frame, text="PALANTIR", font=("Courrier", 40), bg='#41B77F',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, text="AI", font=("Courrier", 25), bg='#41B77F',
                               fg='white')
        label_subtitle.pack()

    def create_generate_button(self):
        yt_button = Button(self.frame, text="GENERATE", font=("Courrier", 25), bg='white', fg='#41B77F',
                           command=self.open_channel)
        yt_button.pack(pady=25, fill=X)

    def open_channel(self):
        webbrowser.open_new("http://youtube.com/gravenilvectuto")
        
        



# afficher
app = MyApp()
app.window.mainloop()
