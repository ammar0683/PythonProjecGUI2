from tkinter import *
import csv

from tkinter import messagebox

def process():
    if username.get() == "" or email.get() == "" or password.get() == "" or mobile.get() == 0:
        messagebox.showerror("Error!", "Please Enter Valid username, email, password, and mobile")

    else:

        g="Male" if gender.get()==1 else "Female"
        javaScript = "JavaScript" if js.get() == 1 else ""
        python = "Python" if py.get() == 1 else ""
        java = "Java" if ja.get() == 1 else ""

        with open("User.txt","a") as f1:
            f1.write("\n"+username.get()+"\t"+password.get()+"\t"+email.get()+"\t"+str(mobile.get())+"\t"+g+"\t"+JavaScript+"\t"+Python+"\t"+Java)
            messagebox.showinfo("Submitted","All Data Added to the file!")
            f1.close()

        with open("User_data.csv","a") as f2:
            fwrite=csv.writer(f2)
            fwrite.writerow([username.get(),password.get(),email.get(),str(mobile.get),g,JavaScript,Python,Java])
            f2.close()
            messagebox.showinfo("Submitted","All Data Added is the CSV File!")
        '''
    s=username.get()+"\n"+email.get()+"\n"+password.get()+"\n"+str(mobile.get())+"\n"+str(g)
    messagebox.showinfo("Form Submitted!",s)
    print("Form is Processed!")
'''
root=Tk()
root.title("User Registration System")

username=StringVar()
password=StringVar()
email=StringVar()
mobile=IntVar()
gender=IntVar()
js=IntVar()
py=IntVar()
ja=IntVar()

l1=Label(root,text="User Registration Form",font=("Century",12,"bold"))
l1.grid(row=0,column=0,padx=10,pady=20,columnspan=2)

l2=Label(root,text="User Name",font=("Century",12,"bold"))
l2.grid(row=1,column=0,padx=10,pady=20)

Label(root,text="Email",font=("Century",12,"bold")).grid(row=2,column=0,padx=10)
Entry(root,font=("Century",12,"bold"),textvariable=email).grid(row=2,column=1,padx=10,pady=20,columnspan=2)

e1=Entry(root,font=("Century",12,"bold"),textvariable=username)
e1.grid(row=1,column=1,padx=10,pady=20,columnspan=2)

Label(root,text="Password",font=("Century",12,"bold")).grid(row=3,column=0,padx=10)
Entry(root,show="*",font=("Century",13,"bold"),textvariable=password).grid(row=3,column=1,padx=10,pady=20,columnspan=2)

Label(root,text="Mobile",font=("Century",12,"bold")).grid(row=4,column=0,padx=10)
Entry(root,font=("Century",12,"bold"),textvariable=mobile).grid(row=4,column=1,padx=10,pady=20,columnspan=2)

Label(root,text="Select Gender:",font=("Century",12,"bold")).grid(row=5,column=0,padx=10,pady=20)

r1=Radiobutton(root,value=1,text="Male",font=("Century",12,"bold"),variable=gender)
r1.grid(row=5,column=1)

r2=Radiobutton(root,value=2,text="Female",font=("Century",12,"bold"),variable=gender)
r2.grid(row=5,column=2)

c1=Checkbutton(root,text="JavaScript",font=("Century",12,"bold"),variable=js)
c1.grid(row=6,column=0)

c2=Checkbutton(root,text="Python",font=("Century",12,"bold"),variable=py)
c2.grid(row=6,column=1)

c3=Checkbutton(root,text="Java",font=("Century",12,"bold"),variable=ja)
c3.grid(row=6,column=2)

Button(root,text="Register User!",font=("Century",8,"bold"),padx=10,pady=10,command=process).grid(row=8,column=1,columnspan=2)
root.mainloop()

