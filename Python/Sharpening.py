import os
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import cv2
import PIL
from PIL import ImageTk, Image



def binToDecimal():  
    file = open('res.txt', 'r')
    flag=0
    binario=""
    lista=[]
    while 1:       
        # read by character 
        char = file.read(1)           
        if not char:  
            break
        binario=binario+char
        if (flag<7):
            flag=flag+1
        else:
            flag=0
            try:
                elemento=(int(binario,2))
                lista.append(elemento)
                binario=""
            except:
                binario=""
                
    file.close()
    print(len(lista))
    return lista
    
def ver(n,m):
    newdata=binToDecimal()
    newPic = Image.new('L', [n-2,m-2])
    newPic.putdata(newdata)
    newPic.save('test.bmp')
    newPic.close()


def holamundo():
    print("Hola MUndo")

def create_file(data, name):
    f_out = open(name, 'w')
    str_data = ''
    for e in data:
        if e <= 9:
            str_data += '00'+str(e)
        elif 10 <= e <= 99:
            str_data += '0'+str(e)
        else:
            str_data += str(e)
    f_out.write(str_data)
    f_out.flush()
    f_out.close()

def runScript(n,m):

    os.system("nasm -f elf64 conv.asm -o conv.o")
    os.system("ld conv.o -o conv")
    os.system("./conv "+str(n)+" "+str(m))
    ver(n,m)

class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title ("Sharpening & Over-Sharpening")
        self.minsize(1080,720)
       # self.wm_iconbitmap('icon.ico')
        self.var=IntVar()

        self.labelFrame = ttk.LabelFrame(self,text="Open a FILE")
        self.labelFrame.grid(column = 0, row=1, padx=20,pady=20)
        
        self.button()
        self.radioButton()

    def radioEvent(self):
        radSelected= self.radValues.get()
        if (radSelected==1):
            self.createCanvasImage('foto.png')
            holamundo()
            print(1)
        elif (radSelected==2):
            self.createCanvasImage('foto2.jpg')
            print(2)
        elif (radSelected==3):
            ver(364,681)
            self.createCanvasImage('test.bmp')
            print(3)
        else:
            print ("Nada")
        
    def createCanvasImage(self,path):

        self.canvas = Canvas(self, bg="black",height =500,width=500)
        self.canvas.grid (column = 10, row =10)
        
        self.image=Image.open(path)
        m,n=self.image.size
        print("m: "+str(m)+ " r: "+str(n) )
        self.image2=self.image.resize((500,500))

        self.canvas.image= ImageTk.PhotoImage(self.image2)
        self.canvas.create_image(0,0,image=self.canvas.image,anchor='nw')
        
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Browse A File", command = self.fileDialog)
        self.button.grid (column = 1, row =1)

    def radioButton(self):
        self.radValues=IntVar()
        self.r1 = ttk.Radiobutton(self.labelFrame, text = "Normal", variable=self.radValues, value=1, command = self.radioEvent)
        self.r1.grid (column = 4, row =1)
        
        self.r2 = ttk.Radiobutton(self.labelFrame, text = "Sharpening", variable=self.radValues,value=2, command = self.radioEvent)
        self.r2.grid (column = 4, row =5)
        
        self.r3 = ttk.Radiobutton(self.labelFrame, text = "Over-Sharpening", variable=self.radValues,value=3, command = self.radioEvent)
        self.r3.grid (column = 4, row =10)
        
        
    def fileDialog(self):
        self.filename = filedialog.askopenfilename (initialdir = "/", title = "Select a File",filetypes=(('png','*.png'),
                                                ('bmp','*.bmp'),('jpeg','*.jpeg'),('Todos os arquivos','*.*')))

        self.foto = Image.open(self.filename)
        self.foto = self.foto.convert('L')
        m,n=self.foto.size
        print("m: "+str(m)+ " n: "+str(n) )
        rows = self.foto.size[0]
        cols = self.foto.size[0]
        data = self.foto.getdata()
        self.foto.close()
        create_file(data, 'mybin.txt')
        create_file([], 'res.txt')
        runScript(n,m)


if __name__ == '__main__':
    root = Root()
    root.mainloop()
