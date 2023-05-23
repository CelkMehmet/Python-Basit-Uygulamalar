#Kütüphaneleri yükle
import re
from tkinter import *
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tkinter.simpledialog import *

root = Tk()
root.title('Diochlet Notepad')
root.resizable(0, 0)
#Not Penceresini Kaydırabilir yapmak için 
notepad = ScrolledText(root, width = 90, height = 40)
DosyaName = ' '


#Dosya Menüsünün Özelliklerini Belirliyoruz 
def cmdYeni():   
    global DosyaName
    if len(notepad.get('1.0', END+'-1c'))>0:
        if messagebox.askyesno("Notepad", "Değişiklikler Kaydedilsin mi ?"):
            cmdKaydet()
        else:
            notepad.delete(0.0, END)
    root.title("Notepad")
def cmdAç():     
    fd = filedialog.askAçDosya(parent = root, mode = 'r')
    t = fd.read()     
    notepad.delete(0.0, END)
    notepad.insert(0.0, t)
    
def cmdSave():     
    fd = filedialog.askKaydetasDosya(mode = 'w', defaultextension = '.txt')
    if fd!= None:
        data = notepad.get('1.0', END)
    try:
        fd.write(data)
    except:
        messagebox.showerror(title="Error", message = "KDosya Kaydedilemedi!")
     
def cmdSaveas():     
    fd = filedialog.askKaydetasDosya(mode='w', defaultextension = '.txt')
    t = notepad.get(0.0, END)    
    try:
        fd.write(t.rstrip())
    except:
        messagebox.showerror(title="Hata", message = "Dosya Kaydedilemiyor!")
def cmdExit():     
    if messagebox.askyesno("Notepad", "Çıkmak  istediğine emin misin ?"):
        root.destroy()
def cmdCut():     
    notepad.event_generate("<<Kes>>")
def cmdCopy():    
    notepad.event_generate("<<Kopyala>>")
def cmdPaste():     
    notepad.event_generate("<<Yapıştır>>")
def cmdClear():    
    notepad.event_generate("<<Temizle>>")
       
def cmdFind():    
    notepad.tag_remove("Found",'1.0', END)
    find = SimpleDialog.askstring("Ara", "Şunu Ara:")
    if find:
        idx = '1.0'     
    while 1:
        idx = notepad.search(find, idx, nocase = 1, stopindex = END)
        if not idx:
            break
        lastidx = '%s+%dc' %(idx, len(find))
        notepad.tag_add('Found', idx, lastidx)
        idx = lastidx
    notepad.tag_config('Found', foreground = 'white', background = 'blue')
    notepad.bind("<1>", click)
def click(event):    
    notepad.tag_config('Found',background='white',foreground='black')
def cmdSelectAll():     
    notepad.event_generate("<<Tümünü Seç>>")
    
def cmdTimeDate():    
    now = datetime.now()
    
    dtString = now.strftime("%d/%m/%Y %H:%M:%S")
    label = messagebox.showinfo("Tarih", dtString)
def cmdAbout():     
    label = messagebox.showinfo("Hakkında", "Dicohlet tarafından oluşturuldu!")
    
    
notepadMenu = Menu(root)
root.configure(menu=notepadMenu)

DosyaMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Dosya', menu = DosyaMenu)

DosyaMenu.add_command(label='Yeni', command = cmdYeni)
DosyaMenu.add_command(label='Aç...', command = cmdAç)
DosyaMenu.add_command(label='Kaydet', command = cmdSave)
DosyaMenu.add_command(label=' Farklı Kaydet...', command = cmdSaveas)
DosyaMenu.add_separator()
DosyaMenu.add_command(label='Çıkış', command = cmdExit)

editMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Düzenle', menu = editMenu)

editMenu.add_command(label='Kes', command = cmdCut)
editMenu.add_command(label='Kopyala', command = cmdCopy)
editMenu.add_command(label='Yapıştır', command = cmdPaste)
editMenu.add_command(label='Sil', command = cmdClear)
editMenu.add_separator()
editMenu.add_command(label='Bul...', command = cmdFind)
editMenu.add_separator()
editMenu.add_command(label='Tümünü Seç', command = cmdSelectAll)
editMenu.add_command(label='Tarih', command = cmdTimeDate)

helpMenu = Menu(notepadMenu, tearoff = False)
notepadMenu.add_cascade(label='Yardım', menu = helpMenu)

helpMenu.add_command(label='Hakkında', command = cmdAbout)

notepad.pack()
root.mainloop()
