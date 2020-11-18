from tkinter import *
import smtplib
import tkinter.messagebox
import threading



class Emails:
    def __init__(self,root):
        self.root=root
        self.root.title("Email Sender")
        self.root.iconbitmap("logo11.ico")
        self.root.geometry("600x500")
        self.root.resizable(0,0)



        semail=StringVar()
        spassword=StringVar()
        remail=StringVar()
        subject=StringVar()



        def on_enter1(e):
            but_send['background']="black"
            but_send['foreground']="cyan"
  
        def on_leave1(e):
            but_send['background']="SystemButtonFace"
            but_send['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"




        def clear():
            semail.set("")
            spassword.set("")
            remail.set("")
            subject.set("")
            ent_text.delete('1.0','end')




        def send():
            try:
                if semail.get()!="":
                    if spassword.get()!="":
                        if remail.get()!="":
                            if subject.get()!="":
                                s=smtplib.SMTP_SSL('smtp.gmail.com',465)
                                s.login(semail.get(),spassword.get())
                                message = 'Subject: {}\n\n{}'.format(subject.get(),ent_text.get('1.0','end'))
                                s.sendmail(semail.get(),remail.get(),message)
                                s.quit()                                
                            else:
                                tkinter.messagebox.showerror("Error","Please Enter Subject")
                        else:
                            tkinter.messagebox.showerror("Error","Please Enter Reciver Email")
                    else:
                        tkinter.messagebox.showerror("Error","Please Enter Sender Password")
                else:
                    tkinter.messagebox.showerror("Error","Please Enter Sender Email")
             
            except expression as identifier:
                tkinter.messagebox.showerror("Error",identifier)

        
        def thread_send():
            t=threading.Thread(target=send)
            t.start()

#================frame====================================
        
        mainframe=Frame(self.root,width=600,height=500,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=594,height=150,relief="ridge",bd=3,bg="black")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=594,height=290,relief="ridge",bd=3)
        secondframe.place(x=0,y=150)

        thirdframe=Frame(mainframe,width=594,height=55,relief="ridge",bd=3,bg="black")
        thirdframe.place(x=0,y=440)


#==========================firstframe================================================#
        
        lab_Email=Label(firstframe,text="Sender Email",font=('times new roman',14),bg="black",fg="white")
        lab_Email.place(x=30,y=20)

        lab_password=Label(firstframe,text="Sender Password",font=('times new roman',14),bg="black",fg="white")
        lab_password.place(x=30,y=90)

        ent_email=Entry(firstframe,width=40,relief="ridge",bd=3,font=('times new roman',14),textvariable=semail)
        ent_email.place(x=200,y=20)

        ent_password=Entry(firstframe,width=40,relief="ridge",bd=3,font=('times new roman',14),textvariable=spassword)
        ent_password.place(x=200,y=90)

#=========================seondframe=================================================#
        
        lab_Subject=Label(secondframe,text="Enter Subject",font=('times new roman',14))
        lab_Subject.place(x=30,y=20)

        ent_subject=Entry(secondframe,width=40,relief="ridge",bd=3,font=('times new roman',14),textvariable=subject)
        ent_subject.place(x=200,y=20)


        lab_text=Label(secondframe,text="Enter Message",font=('times new roman',14))
        lab_text.place(x=230,y=70)

        ent_text=Text(secondframe,width=65,height=7,relief="ridge",bd=3)
        ent_text.place(x=30,y=100)


        lab_receiver_email=Label(secondframe,text="Enter Reciver Email",font=('times new roman',14))
        lab_receiver_email.place(x=30,y=240)

        ent_receiver_email=Entry(secondframe,width=40,relief="ridge",bd=3,font=('times new roman',14),textvariable=remail)
        ent_receiver_email.place(x=200,y=240)



#=========================thirdframe=================================================#

        but_send=Button(thirdframe,width=20,text="Send",font=('times new roman',14),cursor="hand2",command=thread_send)
        but_send.place(x=30,y=5)
        but_send.bind("<Enter>",on_enter1)
        but_send.bind("<Leave>",on_leave1)

        but_clear=Button(thirdframe,width=20,text="Clear",font=('times new roman',14),cursor="hand2",command=clear)
        but_clear.place(x=350,y=5)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)
        




if __name__ == "__main__":
    root=Tk()
    app=Emails(root)
    root.mainloop()