from tkinter import*
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time 

root = Tk()
root.title = ("Reloj mundial") 
root.geometry("1500x1500")
mapa = ImageTk.PhotoImage(Image.open("download.jpg"))
mapa1 = ImageTk.PhotoImage(Image.open("india.jpg"))
mapa2 = ImageTk.PhotoImage(Image.open("cancun.jpg"))
mapa3 = ImageTk.PhotoImage(Image.open("japon.jpg"))
#mapa3_sub= mapa3.subsample(2)

#------------India------------
India_label = Label (root, text="India")
India_label.place(relx=0.2,rely=0.04, ancho= CENTER)

India_clock = Label(root)
India_clock["image"]=mapa1
India_clock.place(relx=0.2,rely=0.30, ancho= CENTER)

India_time = Label(root)
India_time.place(relx=0.2,rely=0.50, ancho= CENTER)

#-----------mexico-----------

mexico_label = Label (root, text="Mexico")
mexico_label.place(relx=0.7,rely=0.04, ancho= CENTER)

mexico_clock = Label(root)
mexico_clock["image"]=mapa
mexico_clock.place(relx=0.7,rely=0.30, ancho= CENTER)

mexico_time = Label(root)
mexico_time.place(relx=0.7,rely=0.50, ancho= CENTER)

#-----------cancun----------

cancun_label = Label (root, text="cancun")
cancun_label.place(relx=0.2,rely=0.66, ancho= CENTER)

cancun_clock = Label(root)
cancun_clock["image"]= mapa2
cancun_clock.place(relx=0.2,rely=0.78, ancho= CENTER)

cancun_time = Label(root)
cancun_time.place(relx=0.2,rely=0.90, ancho= CENTER)

#----------japon----------------

japon_label = Label (root, text="japon")
japon_label.place(relx=0.7,rely=0.66, ancho= CENTER)

japon_clock = Label(root)
japon_clock["image"]= mapa3
japon_clock.place(relx=0.7,rely=0.78, ancho= CENTER)

japon_time = Label(root)
japon_time.place(relx=0.7,rely=0.94, ancho= CENTER)


class India(): 
    def times(self): 
        home=pytz.timezone('Asia/Kolkata') 
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S") 
        India_time["text"]="Time :"+ current_time 
        India_time.after(200,self.times)
        
class Mex(): 
    def times(self): 
        home=pytz.timezone('Mexico/General') 
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S") 
        mexico_time["text"]="Time :"+ current_time 
        mexico_time.after(200,self.times)
        
class cancun(): 
    def times(self): 
        home=pytz.timezone('America/Cancun') 
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S") 
        cancun_time["text"]="Time :"+ current_time 
        cancun_time.after(200,self.times)
        
class japon(): 
    def times(self): 
        home=pytz.timezone('Japan') 
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S") 
        japon_time["text"]="Time :"+ current_time 
        japon_time.after(200,self.times)
 
obj_india = India()
india_btn=Button(root,text="Show Time",command=obj_india.times) 
india_btn.place(relx=0.2,rely=0.6, anchor= CENTER)

obj_mexico = Mex()
mexico_btn=Button(root,text="Show Time",command=obj_mexico.times) 
mexico_btn.place(relx=0.7,rely=0.6, anchor= CENTER)

obj_cancun = cancun()
cancun_btn=Button(root,text="Show Time",command=obj_cancun.times) 
cancun_btn.place(relx=0.20,rely=0.97, anchor= CENTER)

obj_japon = japon()
japon_btn=Button(root,text="Show Time",command=obj_japon.times) 
japon_btn.place(relx=0.70,rely=0.97, anchor= CENTER)


root.mainloop()