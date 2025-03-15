from tkinter import *

root = Tk()
class Application():
    def __init__(self):
        self.root =root
        self.tela_inicial()
        self.frames()
        self.widgets()
        root.mainloop()
    
    def tela_inicial(self):
        self.root.title("Tela1")
        self.root.configure(background= 'black')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(750,600)
        self.root.minsize(500,400)
    
    def frames(self):
        self.frames_1 = Frame(self.root, bd=4, bg='white', highlightbackground='lightblue', 
                              highlightthickness=3)
        self.frames_1.place(relx = 0.02, rely = 0.01, relwidth=0.96, relheight= 0.48)

        self.frames_2 = Frame(self.root, bd=4, bg='white', highlightbackground='lightblue', 
                              highlightthickness=3)
        self.frames_2.place(relx = 0.02, rely = 0.505, relwidth=0.96, relheight= 0.48)

    def widgets(self):
        #botão limpar
        self.bt_clear = Button(self.frames_1, text='Limpar', bd=3, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_clear.place(relx= 0.01, rely=0.90, relheight=0.1, relwidth=0.08)
        #botao buscar
        self.bt_clear = Button(self.frames_1, text='Buscar', bd=3, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_clear.place(relx= 0.095, rely=0.90, relheight=0.1, relwidth=0.08)
        #botao novo
        self.bt_clear = Button(self.frames_1, text='Novo', bd=3, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_clear.place(relx= 0.18, rely=0.90, relheight=0.1, relwidth=0.08)
        #botao alterar
        self.bt_clear = Button(self.frames_1, text='Alterar', bd=3, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_clear.place(relx= 0.265, rely=0.90, relheight=0.1, relwidth=0.08)
        #botao apagar
        self.bt_clear = Button(self.frames_1, text='Apagar', bd=3, bg='#107db2', fg='white', font=('verdana', 8, 'bold'))
        self.bt_clear.place(relx= 0.35, rely=0.90, relheight=0.1, relwidth=0.08)


        #label codigo
        self.lb_codigo = Label(self.frames_1, text='Codigo')
        self.lb_codigo.place(relx= 0.01, rely=0.015, relheight=0.1, relwidth=0.08)
        
        self.lb_entry = Entry(self.frames_1, highlightthickness=3)
        self.lb_entry.place(relx= 0.01, rely=0.15, relheight=0.1, relwidth=0.08)

        #label nome
        self.lb_codigo = Label(self.frames_1, text='Nome')
        self.lb_codigo.place(relx= 0.01, rely=0.30, relheight=0.1, relwidth=0.08)
        
        self.lb_entry = Entry(self.frames_1, highlightthickness=3)
        self.lb_entry.place(relx= 0.01, rely=0.42, relheight=0.1, relwidth=0.56)

        #label telefone
        self.lb_codigo = Label(self.frames_1, text='Telefone')
        self.lb_codigo.place(relx= 0.18, rely=0.015, relheight=0.1, relwidth=0.08)
        
        self.lb_entry = Entry(self.frames_1, highlightthickness=3)
        self.lb_entry.place(relx= 0.18, rely=0.15, relheight=0.1, relwidth=0.2)

        #label UF  
        self.lb_codigo = Label(self.frames_1, text='Estado')
        self.lb_codigo.place(relx= 0.60, rely=0.015, relheight=0.1, relwidth=0.08)
        
        self.lb_entry = Entry(self.frames_1, highlightthickness=3)
        self.lb_entry.place(relx= 0.60, rely=0.15, relheight=0.1, relwidth=0.2)

        #label cidade  
        self.lb_codigo = Label(self.frames_1, text='Cidade')
        self.lb_codigo.place(relx= 0.60, rely=0.30, relheight=0.1, relwidth=0.08)
        
        self.lb_entry = Entry(self.frames_1, highlightthickness=3)
        self.lb_entry.place(relx= 0.60, rely=0.42, relheight=0.1, relwidth=0.30)



Application()