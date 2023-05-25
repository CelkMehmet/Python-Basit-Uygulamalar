#Kütüphaneleri ekliyoruz
from tkinter import *
import datetime
import time
import winsound

from pytz import HOUR

#
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("Tarihi gir:",date)
        print(now)
        if now == set_alarm_timer:
            print("Bu saatte uyan")
        winsound.PlaySound("wake_up_bitc.mp3",winsound.SND_ASYNC)
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
#   
clock = Tk()

clock.title("Diochlet ALarm Saati")
clock.geometry("400x200")
time_format=Label(clock, text= "Zamanı Girin!", fg="red",font="Arial").place(x=140,y=100)
addTime = Label(clock,text = "Saat  Dakika   Saniye",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "Uyanma  zamanı",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)


hour = StringVar()
min = StringVar()
sec = StringVar()


hourTime= Entry(clock,textvariable = hour,bg = "yellow",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "yellow",width = 15).place(x=140,y=30)
secTime = Entry(clock,textvariable = sec,bg = "yellow",width = 15).place(x=200,y=30)


submit = Button(clock,text = "Alarm Kur",bg="red",fg="yellow",width = 10,command = actual_time).place(x =140,y=70)

clock.mainloop()