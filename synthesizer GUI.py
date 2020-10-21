from tkinter import*
import time
import datetime
import pygame

pygame.init()
root = Tk()
root.title("Music Box")
root.geometry('1352x700+0+0')
root.configure(background = 'white')

ABC =Frame(root, bg="powder blue", bd=20, relief= RIDGE)
ABC.grid()

ABC1 =Frame(ABC, bg="powder blue", bd=20, relief= RIDGE)
ABC1.grid()
ABC2 =Frame(ABC, bg="powder blue", bd=20, relief= RIDGE)
ABC2.grid()
ABC3 =Frame(ABC, bg="powder blue", bd=20, relief= RIDGE)
ABC3.grid()

str1 = StringVar()
str1.set("Ject Like Music")
Data1 = StringVar()
Time1=StringVar()

Data1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))
#============================Label with title =====================
Label(ABC1, text="Synthesizer",font=('arial',25,'bold'),padx=8,pady=8,bd=4,bg="powder blue",
fg="white",justify=CENTER).grid(row=0,column=0,columnspan=11)

#==================================================================
#txtDate=Entry(ABC1, textvariable=Data1, font=('arial',18,'bold'),bd=34,bg="powder blue",
#fg="white",width=28,justify=CENTER).grid(row=1,column=0,columnspan=1)

#txtDate=Entry(ABC1, textvariable=str1, font=('arial',18,'bold'),bd=34,bg="powder blue",
#fg="white",width=28,justify=CENTER).grid(row=1,column=1,columnspan=1)

#txtDate=Entry(ABC1, textvariable=Time1, font=('arial',18,'bold'),bd=34,bg="powder blue",
#fg="white",width=28,justify=CENTER).grid(row=1,column=2,columnspan=1)
btnCs=Button(ABC, height=2, width=6,bd=4, text="Rec", font=('arial',18,'bold'),bg="black",fg="white")
btnCs.grid(row=0,column=2,padx=5,pady=5)

btnCs=Button(ABC1, height=2, width=6,bd=4, text="sin", font=('arial',18,'bold'),bg="black",fg="white")
btnCs.grid(row=1,column=4,padx=5,pady=5)

btnCs=Button(ABC1, height=2, width=6,bd=4, text="square", font=('arial',18,'bold'),bg="black",fg="white")
btnCs.grid(row=1,column=5,padx=5,pady=5)

btnCs=Button(ABC1, height=2, width=6,bd=4, text="Triangle", font=('arial',18,'bold'),bg="black",fg="white")
btnCs.grid(row=1,column=6,padx=5,pady=5)

btnCs=Button(ABC1, height=2, width=4,bd=4, text="cos", font=('arial',18,'bold'),bg="black",fg="white")
btnCs.grid(row=1,column=7,padx=5,pady=5)

btnCs=Button(ABC1, height=2, width=4,bd=4, text="cord1", font=('arial',18,'bold'),bg="black",fg="white")
btnCs.grid(row=2,column=4,padx=5,pady=5)

btnCs=Button(ABC1, height=2, width=4,bd=4, text="cord2", font=('arial',18,'bold'),bg="black",fg="white")
btnCs.grid(row=2,column=5,padx=5,pady=5)

btnCs=Button(ABC1, height=2, width=4,bd=4, text="cord3", font=('arial',18,'bold'),bg="black",fg="white")
btnCs.grid(row=2,column=6,padx=5,pady=5)

btnCs=Button(ABC1, height=2, width=4,bd=4, text="cord4", font=('arial',18,'bold'),bg="black",fg="white")
btnCs.grid(row=2,column=7,padx=5,pady=5)

#==============================Black Button===============================
btnCs=Button(ABC3, height=6, width=6,bd=4, text="C#", font=('arial',18,'bold'),bg="black",fg="white")
btnCs.grid(row=0,column=1,padx=5,pady=5)

btnDs=Button(ABC3, height=6, width=6,bd=4 , text="D#", font=('arial',18,'bold'),bg="black",fg="white")
btnDs.grid(row=0,column=2,padx=5,pady=5)
btnSpace=Button(ABC3, state=DISABLED, width=2,height=6 ,bg = "powder blue",relief=FLAT)
btnSpace.grid(row=0,column=3,padx=0,pady=0)
btnFs=Button(ABC3, height=6, width=6,bd=4 , text="F#", font=('arial',18,'bold'),bg="black",fg="white")
btnFs.grid(row=0,column=4,padx=5,pady=5)

btnGs=Button(ABC3, height=6, width=6,bd=4 , text="G#", font=('arial',18,'bold'),bg="black",fg="white")
btnGs.grid(row=0,column=5,padx=5,pady=5)
btnBb=Button(ABC3, height=6, width=6,bd=4 , text="Bb", font=('arial',18,'bold'),bg="black",fg="white")
btnBb.grid(row=0,column=6,padx=5,pady=5)

#===============================White button==========================
btnC=Button(ABC3, height=6, width=8, text="C", font=('arial',18,'bold'),bg="white",fg="black")
btnC.grid(row=1,column=0,padx=5,pady=5)
btnD=Button(ABC3, height=6, width=8, text="D", font=('arial',18,'bold'),bg="white",fg="black")
btnD.grid(row=1,column=1,padx=5,pady=5)
btnE=Button(ABC3, height=6, width=8, text="E", font=('arial',18,'bold'),bg="white",fg="black")
btnE.grid(row=1,column=2,padx=5,pady=5)
btnF=Button(ABC3, height=6, width=8, text="F", font=('arial',18,'bold'),bg="white",fg="black")
btnF.grid(row=1,column=3,padx=5,pady=5)

btnG=Button(ABC3, height=6, width=8, text="G", font=('arial',18,'bold'),bg="white",fg="black")
btnG.grid(row=1,column=4,padx=5,pady=5)
btnA=Button(ABC3, height=6, width=8, text="A", font=('arial',18,'bold'),bg="white",fg="black")
btnA.grid(row=1,column=5,padx=5,pady=5)
btnB=Button(ABC3, height=6, width=8, text="B", font=('arial',18,'bold'),bg="white",fg="black")
btnB.grid(row=1,column=6,padx=5,pady=5)

#==================================================================


root.mainloop()