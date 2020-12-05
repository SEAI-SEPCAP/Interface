import tkinter as tk
from PIL import ImageTk,Image
from threading import Timer

class interface(tk.Tk):
    
    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self,*args,**kwargs)
        
        self.geometry("800x480")
        container = tk.Frame(self,width = 800, height = 480)
        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames = {}

        lg = Image.open("logo.png")
        lg = lg.resize((70,70),Image.ANTIALIAS)
        logo= ImageTk.PhotoImage(lg, Image.ANTIALIAS)
        
        pageId = (iniPage,menuCalib,menuCont,separacao,contagem,calib)

        pageName = ("","MENU INICIAL","MENU INICIAL","SEPARAÇÃO","CONTAGEM","CALIBRAÇÃO")


        for F,pName in zip(pageId,pageName):
            frame = F(container,self)
            if (F!=iniPage):
                canvas = tk.Canvas(frame, width=300, height=80,bg="black")
                canvas.place(x=30,y=-5)
                logoTop = tk.Label(frame, image=logo, bg='black')
                logoTop.image = logo
                logoTop.place(x=35,y=2)
                w = tk.Label(frame, text=pName,font=("Segoe UI Black", 20),fg='white',bg='black').place(x=100,y=15)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            

        self.showFrame(iniPage)

    def showFrame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()


class iniPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")
        lg = Image.open("logo.png")
        logo= ImageTk.PhotoImage(lg, Image.ANTIALIAS)
        logoIni = tk.Label(self, image=logo, bg='black')
        logoIni.image = logo
        logoIni.place(x=120,y=115)
        w = tk.Label(self, text="SEPCAP",font=("Segoe UI Black", 40),fg='white',bg='black').place(x=320,y=190)
        ld = tk.Label(self, text="A INICIALIZAR O SISTEMA...",font=("Verdana", 15),fg='grey',bg='black').place(x=320,y=255)
        t = Timer(interval=5,function=lambda:controller.showFrame(menuCalib))
        t.start()

class menuCalib(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")
        buttonMode = tk.Button(self, text = "MODO: SEPARAÇÃO",font=("Segoe UI Black", 20),bd=10,bg='grey',fg="black",height=2,width=22,command=lambda:controller.showFrame(menuCont)).place(x=40,y=170)
        buttonCalib = tk.Button(self, text = "CALIBRAR CORES",font=("Segoe UI Black", 20),bd=10,bg='grey',fg="black",height=2,width=22,command=lambda:controller.showFrame(calib)).place(x=40,y=316)
        buttonStart = tk.Button(self, text = "INICIAR",font=("Segoe UI Black", 29),bd=10,bg='#00B050',fg="black",height=4,width=11,command=lambda:controller.showFrame(separacao)).place(x=470,y=170)
        off = Image.open("off.png")
        off = off.resize((90,90),Image.ANTIALIAS)
        offImg= ImageTk.PhotoImage(off, Image.ANTIALIAS)
        buttonOff = tk.Button(self, image = offImg)
        buttonOff.image = offImg
        buttonOff.place(x=660,y=30)


class menuCont(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")
        buttonMode = tk.Button(self, text = "MODO: CONTAGEM",font=("Segoe UI Black", 20),bd=10,bg='grey',fg="black",height=2,width=22,command=lambda:controller.showFrame(menuCalib)).place(x=40,y=170)
        buttonCalib = tk.Button(self, text = "CALIBRAR CORES",font=("Segoe UI Black", 20),bd=10,bg='grey',fg="black",height=2,width=22,command=lambda:controller.showFrame(calib)).place(x=40,y=316)
        buttonStart = tk.Button(self, text = "INICIAR",font=("Segoe UI Black", 29),bd=10,bg='#00B050',fg="black",height=4,width=11,command=lambda:controller.showFrame(contagem)).place(x=470,y=170)
        off = Image.open("off.png")
        off = off.resize((90,90),Image.ANTIALIAS)
        offImg= ImageTk.PhotoImage(off, Image.ANTIALIAS)
        buttonOff = tk.Button(self, image = offImg)
        buttonOff.image = offImg
        buttonOff.place(x=660,y=30)      


class separacao(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")   


class contagem(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")  


class calib(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")  

app = interface()

app.mainloop()