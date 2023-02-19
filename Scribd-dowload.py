
from tkinter import *
from tkinter import filedialog, messagebox
import requests
import os
import sys, os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import N
from tkinter import *
import urllib.request
import re

path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)

# def select_path(event):
#     global output_path

#     # window.withdraw()
#     output_path = filedialog.askdirectory()
#     path_entry.delete(0, END)
#     path_entry.insert(0, output_path)
#     # window.deiconify()


def make_label(master, x, y, h, w, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0) # don't shrink
    f.place(x=x, y=y)

    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)

    return label


 ############################################
def getlink():
        connect='https://www.scribd.com/'
        problsub='embeds/'
        ect='/content?start_page=1&view_mode=scroll&access_key=key-fFexxf7r1bzEfWu3HKwf'
        crssub="coursevideos/"
        url = key_entry.get() #get url 

        match = re.search(r'/(\d+)/', url)
        if match:
            number = match.group(1)
        print(number)  # In ra chuỗi số tương ứng với mỗi URL
        
        

        url_end=connect+problsub+number+ect
        response = requests.get(url_end)
        print(response)
        try:
                messagebox.showinfo(title="Scribd Dowloader by _Liesy",
                                message="Downloading starts...")
                file = filedialog.asksaveasfile(initialdir="C:\\",
                                                defaultextension='.html',
                                                filetypes=[
                                                    ("html file",".html"),
                                                ])
                if file is None:
                    return
                
                
                file=str(file)
                file_duongdandaluu=file[file.rfind("'C:")+1:file.rfind("html'")+4]
                print(file_duongdandaluu)
                
                
                
                with open(file_duongdandaluu, "w", encoding="utf-8") as file1:
                    file1.write(response.text)   
            
                messagebox.showinfo(title="Scribd Dowloader by _Liesy",
                                message="Download completed...!!")
            
        except Exception as e:
                print(e)
    ###############################################
        
        # #Python GUI save a file
        # file = filedialog.asksaveasfile(initialdir="C:\\",
        #                                 defaultextension='.html',
        #                                 encoding='utf-8',
        #                                 filetypes=[
        #                                     ("html file",".html"),
        #                                 ])
        # if file is None:
        #     return
        
        # #get the name file
        # file=str(file)
        # file_x=file[file.rfind("/")+1:file.rfind(".mp4")+3]#name of file
        
        # #dowload video files
        # file_duongdandaluu=file[file.rfind("'C:")+1:file.rfind("p4'")+2] #link duong dan da save
        # with open(file_duongdandaluu, "w", encoding="utf-8") as file1:
        #     file1.write(response.text)   
################################################
#GUI
window = Tk()
window.title("Scribd Dowloader by _Liesy")
window.iconbitmap("image\icon1.ico")
window.geometry("1000x600")
window.configure(bg = "#FFFFFF")
##khai bao bien thong bao
thongbao=Text(window,height=1,width=15)
thongbao.grid(row=2, column=1)
###########
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"image\maxresdefault.png") #chi duoc png
background = canvas.create_image(
    500, 235.0,
    image=background_img)



canvas.create_text(
    525, 350,
    text = "INPUT YOUR LINK",
    fill = "#ffffff",
    font = ("Roboto-Light", int(14.0)))

canvas.create_text(
    98, 563,
    text = "Made By Liesy ^^",
    fill = "#ffffff",
    font = ("Roboto-Thin", int(12.0)))





key_entry_img = PhotoImage(file = f"image\img_textBox2.png")
key_entry_bg = canvas.create_image(
    520, 400,
    image = key_entry_img)
# url=path_entry.get()
key_entry = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

key_entry.place(
    x = 380, y = 376,
    width = 268.0,
    height = 49)



img0 = PhotoImage(file = f"image\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = getlink,# use dev functions
    relief = "flat")

b0.place(
    x = 455, y = 450,
    width = 123,
    height = 49)



window.resizable(False, False)
window.mainloop()
