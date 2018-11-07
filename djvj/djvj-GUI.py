"""
Runs the GUI for the DJ-VJ app.
Displays a splash screen, then Create and Load Show buttons
Create Show screen functionality is built out, more to come!
"""
import pickle
import tkinter as tk
from tkinter import filedialog, messagebox, Button, Label, Entry, Canvas, PhotoImage,\
                    StringVar, OptionMenu, NW, END
import time

# global variable params, not sure where this is actually supposed to go
# but for right now it only works up here
Params = ""

"""
Displays the splash screen with the DJ-VJ loading screen
"""
class SplashScreen(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("DJ-VJ")
        # doesn't need to be full-screen, looks good smaller
        self.config(width=800, height=600)
        # this lets an image be used as the background
        canvas = Canvas(self, bg="#212121", width=730, height=450)
        canvas.place(x=0, y=0, relwidth=1, relheight=1)
        img = PhotoImage(file="dj-vj.gif")
        canvas.create_image(30, 120, anchor=NW, image=img)
        # adds the "loading" label that makes it splash-screenish
        self.label = Label(self, text="Loading....", bg="#212121",
                           fg="#05F72D", font=("Courier", 72))
        self.label.place(relx=.5, rely=.12, anchor="center")
        # forces this window to be shown
        self.update()


"""
The main navigation screen, which has the "Create Screen" and "Load Screen" buttons
"""

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
        self.label = Label(self, text="Welcome to DJ-VJ!", bg="#212121",
                           fg="#05F72D", font=("Courier", 72))
        # sets it in the middle of the screen, about 1/4 of the way down
        self.label.place(relx=.5, rely=.25, anchor="center")

        # creates the buttons for create, load, and use default show
        self.create_button = Button(self, text="Create\nShow", bg='#05F72D', fg="#05F72D",
                                    font=("Courier", 48), height=5, width=10, command=self.create)
        self.create_button.place(relx=.33, rely=.75, anchor="center")

        self.load_button = Button(self, text="Load\nShow", bg='#05F72D', fg="#05F72D",
                                  font=("Courier", 48), height=5, width=10, command=self.load)
        self.load_button.place(relx=.66, rely=.75, anchor="center")

        ### COMMENTED OUT FOR EASY TESTING ###
        #
        # # after all the main screen is set up, get rid of it so the splash screen can show
        # self.withdraw()
        #
        #
        # # display splash screen
        # splash = SplashScreen(self)
        # # for 6 seconds
        # time.sleep(6)
        # # kill splash screen
        # splash.destroy()
        # # show main screen again
        # self.deiconify()

    # defines what happens when you click on load
    # right now, only lets you select .djvj files, prints out the data
    # will do more later
    def load(self):
        filename = filedialog.askopenfilename(initialdir="/home/Documents", title="Select Show",
                                              filetypes=(("djvj files", "*.djvj"),
                                                         ("all files", "*.*")))
        data = pickle.load(open("%s" % filename, "rb"))
        messagebox.showinfo("Load Show", data)
        print(data)

    # calls the CreateScreen class (come back and play around with this later)
    def create(self):
        CreateScreen(self)


"""
Users can create a .djvj file by adding parameters and setting target values
They can also specify the file name/file save location when saving
"""

class CreateScreen(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title = "Create Screen"
        # sets background of screen
        self.config(bg="#212121")
        # makes fullscreen
        self.attributes('-fullscreen', True)

        Label(self, text="Create a Show! Add Parameters: ", bg="#212121",
              fg="#05F72D", font=("Courier", 36)).place(relx=.5, rely=.1, anchor="center")

        Label(self, text="If", bg="#212121", fg="#05F72D",
              font=("Courier", 36)).place(relx=.35, rely=.25, anchor="center")
        # the sound attribute being tracked
        self.attr = StringVar(self)
        self.attr.set("           ")  # default value
        self.a = OptionMenu(self, self.attr, "pitch", "tempo", "amplitude")
        self.a.place(relx=.42, rely=.25, anchor="center")
        # the sign (ie greater than, less than, etc)
        self.sign = StringVar(self)
        self.sign.set(" ")  # default value
        self.s = OptionMenu(self, self.sign, ">", "<", "=")
        self.s.place(relx=.5, rely=.25, anchor="center")
        # the target value
        self.e1 = Entry(self)
        self.e1.place(relx=.6, rely=.25, anchor="center")

        Label(self, text=":", bg="#212121", fg="#05F72D", font=("Courier", 36)) \
            .place(relx=.65, rely=.25, anchor="center")

        # buttons
        Button(self, text='Add Param', command=self.addition)\
            .place(relx=.45, rely=.35, anchor="center")
        Button(self, text='Remove Param', command=self.remove)\
            .place(relx=.55, rely=.35, anchor="center")
        Button(self, text='Create File', command=self.create_file)\
            .place(relx=.5, rely=.43, anchor="center")

        # shows running params
        self.display = Label(self, text="", bg="#212121", fg="#05F72D", font=("Courier", 20))
        self.display.place(relx=.5, rely=.6, anchor="center")

    def addition(self):
        # basic error checking
        if self.attr.get() == "" or self.sign.get() == "" or self.e1.get() == "":
            messagebox.showinfo("Error", "Please fill out all fields.")
            return
        global Params
        Params = Params + "\n" + "If " + self.attr.get() + \
                 " " + self.sign.get() + " " + self.e1.get()
        self.params_added()
        # clears all the fields
        self.e1.delete(0, END)
        self.attr.set("          ")
        self.sign.set(" ")

    # creates the show file
    def create_file(self):
        global Params
        # lets user choose name/save location
        filename = filedialog.asksaveasfilename(initialdir="/home/Documents",
                                                title="Save file location",
                                                filetypes=(("djvj files", "*.djvj"),
                                                           ("all files", "*.*")))
        # adds to file
        pickle.dump(Params, open("%s.djvj" % filename, "wb"))
        # unnecessary rn, just shows that data stays the same
        data = pickle.load(open("%s.djvj" % filename, "rb"))
        print(data)

        time.sleep(1)
        self.destroy()

    # shows running total of params to be added
    def params_added(self):
        global Params
        self.display.configure(text="%s" % Params)

    # will remove last param added
    def remove(self):
        global Params
        # basic error checking
        if Params == "":
            messagebox.showinfo("Error", "Parameters are empty!")
        idx = Params.rfind("\n")
        if idx >= 0:
            Params = Params[:idx]
        self.params_added()


IntroScreen().mainloop()