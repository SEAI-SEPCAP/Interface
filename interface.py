import tkinter as tk
from PIL import ImageTk,Image
from threading import Timer

class interface(tk.Tk):
    
    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self,*args,**kwargs)
        self.title("SEPCAP")
        self.geometry("800x480")
        self.attributes("-zoomed", True)
        self.overrideredirect(1)
        container = tk.Frame(self,width = 800, height = 480)
        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        self.frames = {}

        lg = Image.open("/home/pi/Desktop/Interface/logo.png")
        lg = lg.resize((70,70),Image.ANTIALIAS)
        logo= ImageTk.PhotoImage(lg, Image.ANTIALIAS)
        
        pageId = (iniPage,menuSep,menuCont,separacao1,separacao2,separacao3,contagem1,contagem2,calib1,calib2)

        pageName = ("","MENU INICIAL","MENU INICIAL","SEPARAÇÃO","SEPARAÇÃO","SEPARAÇÃO","CONTAGEM","CONTAGEM","CALIBRAÇÃO","CALIBRAÇÃO")


        for F,pName in zip(pageId,pageName):
            frame = F(container,self)
            frame.config(cursor='none')
            if (F!=iniPage):
                canvas = tk.Canvas(frame, width=300, height=80,bg="black",highlightthickness=3)
                canvas.place(x=-5,y=30)
                logoTop = tk.Label(frame, image=logo, bg='black')
                logoTop.image = logo
                logoTop.place(x=5,y=35)
                w = tk.Label(frame, text=pName,font=("Paytone One", 20),fg='white',bg='black').place(x=75,y=48)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            

        self.showFrame(iniPage)
        self.update()

    def showFrame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()
        

    def update(self):
        global nCaps
        total = 0
        for i in range(0,8,1):
                n = int(nCaps[i].get())+1
                nCaps[i].set(str(n)) 
                total = total + n
        nCaps[8].set(total)
        if (n<=30):
                self.after(2000,self.update)


class iniPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")
        lg = Image.open("/home/pi/Desktop/Interface/logo.png")
        logo= ImageTk.PhotoImage(lg, Image.ANTIALIAS)
        logoIni = tk.Label(self, image=logo, bg='black')
        logoIni.image = logo
        logoIni.place(x=120,y=105)
        w = tk.Label(self, text="SEPCAP",font=("Paytone One", 40),fg='white',bg='black').place(x=320,y=180)
        ld = tk.Label(self, text="A INICIALIZAR O SISTEMA...",font=("Paytone One", 15),fg='grey',bg='black').place(x=320,y=245)
        t = Timer(interval=5,function=lambda:controller.showFrame(menuSep))
        t.start()

class menuSep(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")
        buttonMode = tk.Button(self, text = "MODO: SEPARAÇÃO",font=("Paytone One", 25),bd=10,bg='grey',activebackground='grey',fg="black",height=2,width=15,command=lambda:controller.showFrame(menuCont)).place(x=42,y=160)
        buttonCalib = tk.Button(self, text = "CALIBRAR CORES",font=("Paytone One", 25),bd=10,bg='grey',activebackground='grey',fg="black",height=2,width=15,command=lambda:controller.showFrame(calib)).place(x=42,y=312)
        buttonStart = tk.Button(self, text = "INICIAR",font=("Paytone One", 33),bd=10,bg='#00B050',activebackground='#00B050',fg="black",height=4,width=8,command=lambda:controller.showFrame(separacao1)).place(x=462,y=160)
        off = Image.open("/home/pi/Desktop/Interface/off.png")
        off = off.resize((90,90),Image.ANTIALIAS)
        offImg= ImageTk.PhotoImage(off, Image.ANTIALIAS)
        buttonOff = tk.Button(self, image = offImg,command=lambda:controller.destroy())
        buttonOff.image = offImg
        buttonOff.place(x=660,y=30)


class menuCont(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")
        buttonMode = tk.Button(self, text = "MODO: CONTAGEM",font=("Paytone One", 25),bd=10,bg='grey',fg="black",activebackground='grey',height=2,width=15,command=lambda:controller.showFrame(menuSep)).place(x=42,y=160)
        buttonCalib = tk.Button(self, text = "CALIBRAR CORES",font=("Paytone One", 25),bd=10,bg='grey',fg="black",activebackground='grey',height=2,width=15,command=lambda:controller.showFrame(calib)).place(x=42,y=312)
        buttonStart = tk.Button(self, text = "INICIAR",font=("Paytone One", 33),bd=10,bg='#00B050',activebackground='#00B050',fg="black",height=4,width=8,command=lambda:controller.showFrame(contagem1)).place(x=462,y=160)
        off = Image.open("/home/pi/Desktop/Interface/off.png")
        off = off.resize((90,90),Image.ANTIALIAS)
        offImg= ImageTk.PhotoImage(off, Image.ANTIALIAS)
        buttonOff = tk.Button(self, image = offImg,command=lambda:controller.destroy())
        buttonOff.image = offImg
        buttonOff.place(x=660,y=30)


class separacao1(tk.Frame):
   
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")
        l = tk.Label(self, text="Nº DE \nCÁPSULAS:",font=("Paytone One", 22),fg='white',bg='black',justify='left').place(x=40,y=142)
        canvas = tk.Canvas(self, width=140, height=77,bg="black",highlightthickness=3)
        canvas.place(x=225,y=148)
        global nCap
        nCap = tk.StringVar(self)
        nCap.set("")
        w = tk.Label(self, textvar=nCap,font=("Paytone One", 36),fg='#db9d00',bg='black').place(x=247,y=151)
        button3 = tk.Button(self, text = "3",font=("Paytone One", 25),bd=10,bg='grey',activebackground='grey',fg="black",height=1,width=1,command=lambda:self.add(3)).place(x=590,y=150)   
        button6 = tk.Button(self, text = "6",font=("Paytone One", 25),bd=10,bg='grey',activebackground='grey',fg="black",height=1,width=1,command=lambda:self.add(6)).place(x=590,y=250)
        button9 = tk.Button(self, text = "9",font=("Paytone One", 25),bd=10,bg='grey',activebackground='grey',fg="black",height=1,width=1,command=lambda:self.add(9)).place(x=590,y=350)
        button2 = tk.Button(self, text = "2",font=("Paytone One", 25),bd=10,bg='grey',activebackground='grey',fg="black",height=1,width=1,command=lambda:self.add(2)).place(x=500,y=150)
        button5 = tk.Button(self, text = "5",font=("Paytone One", 25),bd=10,bg='grey',activebackground='grey',fg="black",height=1,width=1,command=lambda:self.add(5)).place(x=500,y=250)
        button8 = tk.Button(self, text = "8",font=("Paytone One", 25),bd=10,bg='grey',activebackground='grey',fg="black",height=1,width=1,command=lambda:self.add(8)).place(x=500,y=350)
        button1 = tk.Button(self, text = "1",font=("Paytone One", 25),bd=10,bg='grey',activebackground='grey',fg="black",height=1,width=1,command=lambda:self.add(1)).place(x=410,y=150)
        button4 = tk.Button(self, text = "4",font=("Paytone One", 25),bd=10,bg='grey',activebackground='grey',fg="black",height=1,width=1,command=lambda:self.add(4)).place(x=410,y=250)
        button7 = tk.Button(self, text = "7",font=("Paytone One", 25),bd=10,bg='grey',fg="black",height=1,width=1,command=lambda:self.add(7)).place(x=410,y=350)
        buttonDel = tk.Button(self, text = "<",font=("Paytone One", 26),bd=10,bg='#383838',fg="black",height=3,width=1,command=lambda:self.delete()).place(x=680,y=150)
        button0 = tk.Button(self, text = "0",font=("Paytone One", 25),bd=10,bg='grey',activebackground='grey',fg="black",height=1,width=1,command=lambda:self.add(0)).place(x=680,y=350)
        buttonBack = tk.Button(self, text = "VOLTAR",font=("Paytone One", 20),bd=10,bg='#c20000',activebackground='#c20000',fg="black",height=1,width=6,command=lambda:controller.showFrame(menuSep)).place(x=596,y=40)
        buttonGo = tk.Button(self, text = "AVANÇAR",font=("Paytone One", 25),bd=10,bg='#00B050',activebackground='#00B050',fg="black",height=1,width=12,command=lambda:controller.showFrame(separacao2)).place(x=45,y=350)
    
    def add(self,num):
        global nCap
        n = nCap.get()
        if (len(n)<3):
                nCap.set(str(n)+str(num))
        
    def delete(self):    
        global nCap
        n = nCap.get()
        if (len(n)>0):
                nCap.set(str(n[:-1]))
                
class separacao2(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black") 
        canvas = tk.Canvas(self,bg="black",highlightthickness=0)
        canvas.pack(fill='both',expand=1) 
        canvas.create_rectangle(450,30,805,110,width=3,outline='red')
        l1 = tk.Label(self, text="EM OPERAÇÃO...",font=("Paytone One", 20),fg='red',bg='black').place(x=517,y=48)
        global nCaps
        nCaps = []
        for i in range(0,9,1):
                var = tk.StringVar(self)
                var.set("0")
                nCaps.append(var)
        y = 160
        n=0
        nCaps[8].set(0)
        for x in range(45,750,90):
                canvas.create_oval(x,y,x+70,y+70,width=3,outline='grey')
                l = tk.Label(self, text=n,font=("Paytone One", 28),fg='grey',bg='black').place(x=x+22,y=y+5)
                nc = tk.Label(self, textvar=nCaps[n],font=("Paytone One", 40),width=2,justify='center',fg='white',bg='black').place(x=x,y=y+78)
                n = n+1
        l2 = tk.Label(self, text="TOTAL:",font=("Paytone One", 30),fg='white',bg='black').place(x=45,y=355)
        l3 = tk.Label(self, textvar=nCaps[8],font=("Paytone One", 40),fg='#db9d00',bg='black').place(x=205,y=345)
        buttonGo = tk.Button(self, text = "PARAR",font=("Paytone One", 25),bd=12,bg='red',activebackground='red',fg="black",height=1,width=10,command=lambda:controller.showFrame(separacao3)).place(x=470,y=350)

class separacao3(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black") 
        canvas = tk.Canvas(self,bg="black",highlightthickness=0)
        canvas.pack(fill='both',expand=1) 
        canvas.create_rectangle(450,30,805,110,width=3,outline='#00B050')
        l1 = tk.Label(self, text="OPERAÇÃO CONCLUÍDA",font=("Paytone One", 20),fg='#00B050',bg='black').place(x=465,y=48)
        global nCaps
        y = 160
        n=0
        for x in range(45,750,90):
                canvas.create_oval(x,y,x+70,y+70,width=3,outline='grey')
                l = tk.Label(self, text=n,font=("Paytone One", 28),fg='grey',bg='black').place(x=x+22,y=y+5)
                nc = tk.Label(self, textvar=nCaps[n],font=("Paytone One", 40),width=2,justify='center',fg='white',bg='black').place(x=x,y=y+78)
                n = n+1
        l2 = tk.Label(self, text="TOTAL:",font=("Paytone One", 30),fg='white',bg='black').place(x=45,y=355)
        l3 = tk.Label(self, textvar=nCaps[8],font=("Paytone One", 40),fg='#db9d00',bg='black').place(x=205,y=345)
        buttonGo = tk.Button(self, text = "AVANÇAR",font=("Paytone One", 25),bd=12,bg='#00B050',activebackground='#00B050',fg="black",height=1,width=10,command=lambda:controller.showFrame(menuSep)).place(x=470,y=350)

class contagem1(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black") 
        global nCaps 
        canvas = tk.Canvas(self,bg="black",highlightthickness=0)
        canvas.pack(fill='both',expand=1) 
        canvas.create_rectangle(450,30,805,110,width=3,outline='red')
        l1 = tk.Label(self, text="EM OPERAÇÃO...",font=("Paytone One", 20),fg='red',bg='black').place(x=517,y=48)
        l2 = tk.Label(self, text="Nº DE CÁPSULAS:",font=("Paytone One", 30),fg='white',bg='black').place(x=230,y=155)
        l3 = tk.Label(self, textvar=nCaps[8],font=("Paytone One", 50),width=5,justify='center',fg='#db9d00',bg='black').place(x=280,y=205)
        buttonGo = tk.Button(self, text = "PARAR",font=("Paytone One", 30),bd=12,bg='red',activebackground='red',fg="black",height=1,width=10,command=lambda:controller.showFrame(contagem2)).place(x=233,y=340)
        
        
class contagem2(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")  
        global nCaps
        canvas = tk.Canvas(self,bg="black",highlightthickness=0)
        canvas.pack(fill='both',expand=1) 
        canvas.create_rectangle(450,30,805,110,width=3,outline='#00B050')
        l1 = tk.Label(self, text="OPERAÇÃO CONCLUÍDA",font=("Paytone One", 20),fg='#00B050',bg='black').place(x=465,y=48)
        l2 = tk.Label(self, text="Nº DE CÁPSULAS:",font=("Paytone One", 30),fg='white',bg='black').place(x=230,y=155)
        l3 = tk.Label(self, textvar=nCaps[8],font=("Paytone One", 50),width=5,justify='center',fg='#db9d00',bg='black').place(x=280,y=205)
        buttonGo = tk.Button(self, text = "AVANÇAR",font=("Paytone One", 30),bd=12,bg='#00B050',activebackground='#00B050',fg="black",height=1,width=10,command=lambda:controller.showFrame(menuSep)).place(x=233,y=340)

class calib1(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="black")   
        l1 = tk.Label(self, text="Instruções:",font=("Paytone One", 22),fg='white',bg='black').place(x=50,y=140)
        l1 = tk.Label(self, text="Posicione a cápsula no alinhamento da câmara",font=("Paytone One", 18),fg='grey',bg='black').place(x=70,y=185)
        lg = Image.open("/home/pi/Desktop/Interface/sep.png")
        lg = lg.resize((325,200),Image.ANTIALIAS)
        logo= ImageTk.PhotoImage(lg, Image.ANTIALIAS)
        logoTop = tk.Label(self, image=logo, bg='black')
        logoTop.image = logo
        logoTop.place(x=100,y=240)
        buttonBack = tk.Button(self, text = "VOLTAR",font=("Paytone One", 20),bd=10,bg='grey',activebackground='grey',fg="black",height=1,width=7,command=lambda:controller.showFrame(menuSep)).place(x=570,y=40)
        buttonBack = tk.Button(self, text = "SEGUINTE",font=("Paytone One", 20),bd=10,bg='#00B050',activebackground='#00B050',fg="black",height=1,width=7,command=lambda:controller.showFrame(menuSep)).place(x=570,y=370)

app = interface()
app.mainloop()


