#from easygui import *= ambil semua jadi g perlu menambahkan kata turtle di kode bawahnya,lebih besar

#import turtle= harus pake kata turtle, lebih hemat space

#import turtle 
#print(dir(turtle))= melihat semua data dari modul yang kita import

#import easygui
#print(help(easygui.msgbox))= untuk mengetahui fumgsi dari bagian suatu modul

from easygui import *
from random import *
while True: 

    aksi=["batu","gunting","kertas"]
    choice1=buttonbox("pilih!","batu,gunting,kertas",aksi)  
    computer=choice(aksi)
    
    
    if (choice1 == computer):
        msgbox("seri")
    
    elif (choice1 == "batu"):
        if (computer == "gunting"):
            msgbox("menang")
        else:    
            msgbox("kalah")
    
    elif (choice1 == "kertas"):
        if(computer == "batu"):
            msgbox("menang")
        else:    
            msgbox("kalah")

    elif (choice1 == "gunting"):
        if(computer == "kertas"):
            msgbox("menang")
        else:    
            msgbox("kalah")


        break          

    
                

    

