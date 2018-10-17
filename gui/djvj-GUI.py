from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
import time
import pickle


# the splash screen for DJ-VJ
class SplashScreen(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("DJ-VJ")
        # doesn't need to be full-screen, looks good smaller
        self.config(width=800, height=600)
        # this lets me use an image as the background
        canvas = Canvas(self, bg="#212121", width=730, height=450)
        canvas.place(x=0, y=0, relwidth=1, relheight=1)
        img = PhotoImage(file="dj-vj.gif")
        canvas.create_image(30, 120, anchor=NW, image=img)
        #adds the "loading" label that makes it splash-screenish
        self.label = Label(self, text="Loading....", bg="#212121", fg="#05F72D", font=("Courier", 72))
        self.label.place(relx=.5, rely=.12, anchor="center")
        # forces this window to be shown
        self.update()


# the main screen
class IntroScreen(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # sets title bar
        self.title("DJ-VJ")

        # sets background of screen
        self.config(bg="#212121")
        # makes fullscreen
        self.attributes('-fullscreen', True)

        # this creates text and customizes it
        self.label = Label(self, text="Welcome to DJ-VJ!", bg="#212121", fg="#05F72D", font=("Courier", 72))
        # sets it in the middle of the screen, about 1/4 of the way down
        self.label.place(relx=.5, rely=.25, anchor="center")

        # creates the buttons for create, load, and use default show
        self.create_button = Button(self, text="Create\nShow", highlightbackground='#05F72D', fg="#05F72D",
                                    font=("Courier", 48), height=5, width=10, command=self.create)
        self.create_button.place(relx=.33, rely=.75, anchor="center")

        self.load_button = Button(self, text="Load\nShow", highlightbackground='#05F72D', fg="#05F72D",
                                  font=("Courier", 48), height=5, width=10, command=self.load)
        self.load_button.place(relx=.66, rely=.75, anchor="center")

        ### COMMENTED OUT FOR EASY TESTING ###

        # after all the main screen is set up, get rid of it so the splash screen can show
        #self.withdraw()


        # # display splash screen
        # splash = SplashScreen(self)
        # # for 6 seconds
        # time.sleep(6)
        # # kill splash screen
        # splash.destroy()
        # # show main screen again
        # self.deiconify()

    # defines what happens when you click on create
    def create(self):
        newwindow = Toplevel()
        newwindow.config(bg="#212121")
        newwindow.attributes('-fullscreen', True)
        self.label = Label(newwindow, text="Create Your Own Show", bg="#212121", fg="#05F72D", font=("Courier", 72))
        self.label.place(relx=.5, rely=.25, anchor="center")
        self.newfile(newwindow)

    # creates the new file type, .djvj
    # right now, just takes in a user-created file name and the text the user wants in the file.
    # later, will add support for parameters and the like
    def newfile(self, newwindow):
        def create_file():
            # error checking to handle blank submission boxes
            if(e1.get()=="") or (e2.get() == ""):
                print("NULL")
                messagebox.showinfo("Error", "Please fill out the boxes!")
                return
            # creates a .djvj file with the user's submitted file name/data
            pickle.dump(str(e2.get()), open("%s.djvj" % e1.get(), "wb"))
            messagebox.showinfo("New File", "File " + e1.get() + " created!")
            e1.delete(0, END)
            e2.delete(0, END)
            # closes the window
            newwindow.destroy()

        # creates entry box
        self.label = Label(newwindow, text="File Name:", bg="#212121", fg="#05F72D", font=("Courier", 36))\
            .place(relx=.35, rely=.5, anchor="center")
        e1 = Entry(newwindow)
        e1.place(relx=.5, rely=.5, anchor="center")

        self.label = Label(newwindow, text="File Text:", bg="#212121", fg="#05F72D", font=("Courier", 36))\
            .place(relx=.35, rely=.6, anchor="center")
        e2 = Entry(newwindow)
        e2.place(relx=.5, rely=.6, anchor="center")

        self.button = Button(newwindow, text='Create', bg="#212121", fg="#05F72D", font=("Courier", 24),\
                             command=create_file).place(relx=.5, rely=.75, anchor="center")


    # defines what happens when you click on load
    # right now, only lets you select .djvj files and prints out the data that's in them. will do more later
    def load(self):
        filename = filedialog.askopenfilename(initialdir="/home/Documents", title="Select Show",
                                   filetypes=(("djvj files", "*.djvj"), ("all files", "*.*")))
        data = pickle.load(open("%s" % filename, "rb"))
        messagebox.showinfo("Load Show", data)


my_gui = IntroScreen()
my_gui.mainloop()
