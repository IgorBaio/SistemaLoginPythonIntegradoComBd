from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#Criar janela#
jan = Tk()
jan.title("Baio Systems - Acess Panel")
jan.geometry("600x300")
jan.configure(background="yellow")
jan.resizable(width=False, height=False)
jan.attributes("-alpha",0.93)
jan.iconbitmap(default="icons/baioSystems_8.ico")

#======================Carregando Imagens======================#
logo = PhotoImage(file="icons/BaioSystems5.png")


#======================Widgets======================#
LeftFrame = Frame(jan, width=150, height=300, bg="#483D8B", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=445, height=300, bg="black", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="#483D8B")
LogoLabel.place(x=30,y=100)

UserLabel = Label(RightFrame, text="UserName:", font=("Century Gothic",20), bg="black", fg="#DAA520")
UserLabel.place(x=30,y=85)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=180, y=97)

PasswordLabel = Label(RightFrame, text="Password:", font=("Century Gothic",20), bg="black", fg="#DAA520")
PasswordLabel.place(x=30,y=125)

PassEntry = ttk.Entry(RightFrame, width=30, show="¿")
PassEntry.place(x=180, y=137)

#======================Botoes======================#
LoginButton = ttk.Button(RightFrame, text="Login", width="22")
LoginButton.place(x=34.2 , y=200)

def Register():
    #======================Removendo Widgets de Login======================#
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    #======================Inserindo Widgets de Registro======================#
    NomeLabel = Label(RightFrame, text="Name:", font=("Centuric Gothic",20), bg="black", fg="#DAA520")
    NomeLabel.place(x=30, y=5)
    
    NomeEntry = ttk.Entry(RightFrame, width=30)
    NomeEntry.place(x=180, y=17)

    EmailLabel = Label(RightFrame, text="E-mail:",font=("Centuric Gothic",20), bg="black", fg="#DAA520")
    EmailLabel.place(x=30,y=45)

    EmailEntry = ttk.Entry(RightFrame,width=30)
    EmailEntry.place(x=180,y=57)

    Register = ttk.Button(RightFrame, text="Register", width="22")
    Register.place(x=223,y=199)

    def BackToLogin():
        #======================Removendo Widgets de Registro======================#
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)

        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)

        Register.place(x=5000)

        Back.place(x=5000)

        #======================Trazendo de volta os Widgets de Login======================#
        LoginButton.place(x=34.2 , y=200)

        RegisterButton.place(x=223,y=199)

    Back = ttk.Button(RightFrame, text="Back", width="22", command=BackToLogin)
    Back.place(x=34.2 , y=200)
    


RegisterButton = ttk.Button(RightFrame, text="Register", width="22", command=Register)
RegisterButton.place(x=223,y=199)



jan.mainloop()
 