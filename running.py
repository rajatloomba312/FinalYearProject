from flask import Flask, render_template
#import os
from tkinter import *
app=Flask(__name__)
@app.route('/')
def index():
	return render_template("home.html")
@app.route('/submit')
def submit():
    import os
    from tkinter import messagebox
    
    
    def helloCallBack():
        os.system('python object_detection_app.py');
    def about():
    	txt="Object detection is a computer technology related to computer vision and image processing that deals with detecting instances of semantic objects of a certain class (such as humans, buildings, or cars) in digital images and videos."
    	messagebox.showinfo("Project", txt)
    
    def dev():
    	messagebox.showinfo("Developers", "Deepak(14001001013)\n\nRishabh Bansal(14001001044)\n\nRishabh Yadav(14001001045)\n\nShivani Kuchhal(14001001051)")
    def stop():
    	exit()
    def mentorss():
    	messagebox.showinfo("Mentors", "Prof. Sanjeev Indora\n\nDr. Sukhdeep Sangwan")
    root = Tk()
    root.title("Project")
    root.geometry('800x500')
    
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='About', menu=filemenu)
    filemenu.add_command(label='Developers', command=dev)
    filemenu.add_separator()
    filemenu.add_command(label='Mentors', command=mentorss)
    filemenu.add_separator()
    filemenu.add_command(label='Project', command=about)
    
    w = Label(root, text="Object Detection and Recognition",font='Helvetica 32 bold')
    w.place(x=40,y=10)
    button = Button(root, text="QUIT", fg="red",command=stop,font='Helvetica 8 bold')
    button.config(height = 10, width = 20,highlightcolor='red',highlightbackground="red",highlightthickness=4)
    button.place(x=150,y=200)
    slogan = Button(root,text="Start",fg="green",command=helloCallBack)
    slogan.config(height = 10, width = 20)
    slogan.place(x=450,y=200)
    #wq = Label(root, text="Object Detection and Recognition",font='Helvetica 18 bold')
    #wq.place(x=300, y=200)
    root.mainloop()
    mainloop()
    return render_template("home.html")

if __name__=='__main__':
    app.run(debug=True)