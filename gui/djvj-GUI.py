from tkinter import *
from tkinter import filedialog, messagebox
import tkinter as tk
import time


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
        self.create_button.place(relx=.25, rely=.75, anchor="center")

        self.load_button = Button(self, text="Load\nShow", highlightbackground='#05F72D', fg="#05F72D",
                                  font=("Courier", 48), height=5, width=10, command=self.load)
        self.load_button.place(relx=.5, rely=.75, anchor="center")

        self.default_button = Button(self, text="Default\nShow", highlightbackground='#05F72D', fg="#05F72D",
                                     font=("Courier", 48), height=5, width=10, command=self.default)
        self.default_button.place(relx=.75, rely=.75, anchor="center")

        # after all the main screen is set up, get rid of it so the splash screen can show
        self.withdraw()

        # display splash screen
        splash = SplashScreen(self)
        # for 6 seconds
        time.sleep(6)
        # kill splash screen
        splash.destroy()
        # show main screen again
        self.deiconify()

    # defines what happens when you click on create
    # right now, just opens a blank screen with some text, later will let you start to create a show
    def create(self):
        newwindow = Toplevel()
        newwindow.config(bg="#212121")
        newwindow.attributes('-fullscreen', True)
        self.label = Label(newwindow, text="Create Your Own Show", bg="#212121", fg="#05F72D", font=("Courier", 72))
        self.label.place(relx=.5, rely=.25, anchor="center")

    # defines what happens when you click on load
    # right now, opens up a file explorer and lets you choose a random file, later will let you choose a show file
    def load(self):
        filename = filedialog.askopenfilename(initialdir="/home/Documents", title="Select Show",
                                   filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        messagebox.showinfo("Load Show", "You selected the " + filename + " show")

    # defines what happens when you click on default
    # right now, just opens a blank screen with some text, later will show the default show
    def default(self):
        newwindow = Toplevel()
        newwindow.config(bg="#212121")
        newwindow.attributes('-fullscreen', True)
        newwindow.label = Label(newwindow, text="This is what the\ndefault show looks like", bg="#212121", fg="#05F72D", font=("Courier", 60))
        newwindow.label.place(relx=.5, rely=.25, anchor="center")


my_gui = IntroScreen()
my_gui.mainloop()
