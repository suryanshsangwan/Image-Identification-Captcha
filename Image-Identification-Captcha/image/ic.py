from tkinter import *

def q():
    w=Tk()
    w.title("captcha")
    w.configure(bg="black")
    def close():
        exit()
    def wrong():
        w.destroy()
        w0=Tk()
        w0.title("verification")
        Label(w0,text="You are Bot") .grid(row=0, column=0, sticky=N)
        Button(w0,text="Exit",width=4,command=close) .grid(row=1,column=1,sticky=N)
        def retry():
            w0.destroy()
            q()
        Button(w0,text="Retry",width=5,command=retry) .grid(row=1,column=0,sticky=N)
        w0.mainloop()
    def correct():
        w.destroy()
        w1=Tk()
        w1.title("verification")
        Label(w1,text="You are Human") .grid(row=0, column=0, sticky=N)
        Button(w1,text="Exit",width=4,command=close) .grid(row=1,column=1,sticky=N)
        def retry():
            w1.destroy()
            q()
        Button(w1,text="Retry",width=5,command=retry) .grid(row=1,column=0,sticky=N)
        w1.mainloop()
#_____________________________________________________________________________#
    Bus1=PhotoImage(file="Bus1.gif")
    Label (w, image=Bus1, bg="black") .grid(row=0, column=0, sticky=N)
    Button(w,text="Select",width=6,command=correct) .grid(row=1,column=0,sticky=N)
#_____________________________________________________________________________#
    Dog1=PhotoImage(file="Dog1.gif")
    Label (w, image=Dog1, bg="black") .grid(row=0, column=1, sticky=N)
    Button(w,text="Select",width=6,command=wrong) .grid(row=1,column=1,sticky=N)
#_____________________________________________________________________________#
    Cat1=PhotoImage(file="Cat1.gif")
    Label (w, image=Cat1, bg="black") .grid(row=0, column=2, sticky=N)
    Button(w,text="Select",width=6,command=wrong) .grid(row=1,column=2,sticky=N)
#_____________________________________________________________________________#
    Label (w, text="Select Image of Bus", bg="black",fg="white",font="none 12 bold") .grid(row=2, column=1, sticky=W)
    Button(w,text="Exit",width=6,command=close) .grid(row=3,column=1,sticky=N)
    w.mainloop()
q();
