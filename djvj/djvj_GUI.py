"""
Runs the GUI for the DJ-VJ app.
Displays a splash screen, then Create and Load Show buttons
Create Show screen functionality is built out, more to come!
"""

import pickle
import tkinter as tk
from tkinter import filedialog, messagebox, Button, Label, Entry, Canvas, PhotoImage, \
    StringVar, OptionMenu, NW, END
import time
import djvj.pitch

# global variable params, not sure where this is actually supposed to go
# but for right now it only works up here
Params = ""
show = list()
audio_attr = list()  # what the audio should listen for
rules = list()  # the rest of the parameters for the video queue
values = list()
video_loc = list()


class SplashScreen(tk.Toplevel):
    """ Displays the splash screen with the DJ-VJ loading screen """

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("DJ-VJ")
        # doesn't need to be full-screen, looks good smaller
        self.config(width=800, height=600)
        # this lets an image be used as the background
        canvas = Canvas(self, bg="#212121", width=730, height=450)
        canvas.place(x=0, y=0, relwidth=1, relheight=1)
        img = PhotoImage(file="./djvj/dj-vj.gif")
        canvas.create_image(30, 120, anchor=NW, image=img)
        # adds the "loading" label that makes it splash-screenish
        self.label = Label(self, text="Loading....", bg="#212121",
                           fg="#05F72D", font=("Courier", 72))
        self.label.place(relx=.5, rely=.12, anchor="center")
        # forces this window to be shown
        self.update()


class IntroScreen(tk.Tk):
    """
    The main navigation screen, which has the "Create Screen" and "Load Screen" buttons
    """

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
        self.create_button = Button(self, text="Create\nShow", bg='#05F72D', fg="#000000",
                                    highlightbackground='#05F72D', font=("Courier", 48),
                                    height=5, width=10, command=self.create)
        self.create_button.place(relx=.33, rely=.75, anchor="center")

        self.load_button = Button(self, text="Load\nShow", bg='#05F72D', fg="#000000",
                                  highlightbackground='#05F72D', font=("Courier", 48),
                                  height=5, width=10, command=self.load)
        self.load_button.place(relx=.66, rely=.75, anchor="center")

        #Allows for easy exit from Intro Screen
        self.exit_button = Button(self, text="X", bg='#05F72D', fg="#000000",
                                  highlightbackground='#05F72D', font=("Courier", 48),
                                  height=1, width=2, command=self.exit)
        self.exit_button.place(relx=.9, rely=.1, anchor="center")

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

    def load(self):
        """
        loads the user's chosen file, reads data,
        parses the data into audio_attr, rules, values, and videos
        and appends these lists to the show list that is used by main.py
        """
        filename = filedialog.askopenfilename(initialdir="/home/Documents", title="Select Show",
                                              filetypes=(("djvj files", "*.djvj"),
                                                         ("all files", "*.*")))
        data = pickle.load(open("%s" % filename, "rb"))
        mee = data.split("\n")
        mee.pop(0)
        for e in mee:
            li = e.split(" ")
            audio_attr.append(li[1])
            rules.append(li[2])
            values.append(li[3])
            video_loc.append(li[5])
            # appends all these lists to a larger list, used in main to send to show.py
        show.append(audio_attr)
        show.append(rules)
        show.append(values)
        show.append(video_loc)

        # right now, just for error checking
        messagebox.showinfo("Load Show", data)
        self.destroy()

    def create(self):
        """ pulls up create screen """
        CreateScreen(self)

    def exit(self):
        """ exits screen """
        self.destroy()


class CreateScreen(tk.Toplevel):
    """
    Users can create a .djvj file by adding parameters and setting target values
    They can also specify the file name/file save location when saving
    """

    # the actual video location
    video_location = ""
    # a shorter representation of the video path
    video = ""

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
              font=("Courier", 36)).place(relx=.15, rely=.25, anchor="center")
        # the sound attribute being tracked
        self.attr = StringVar(self)
        self.attr.set("           ")  # default value
        self.a = OptionMenu(self, self.attr, "pitch", "tempo")
        self.a.place(relx=.22, rely=.25, anchor="center")
        # the sign (ie greater than, less than, etc)
        self.sign = StringVar(self)
        self.sign.set(" ")  # default value
        self.s = OptionMenu(self, self.sign, ">", "<", "=")
        self.s.place(relx=.3, rely=.25, anchor="center")
        # the target value
        self.e1 = Entry(self)
        self.e1.place(relx=.4, rely=.25, anchor="center")

        Label(self, text=", ", bg="#212121", fg="#05F72D", font=("Courier", 36)) \
            .place(relx=.45, rely=.25, anchor="center")

        Label(self, text="play ", bg="#212121", fg="#05F72D", font=("Courier", 36)) \
            .place(relx=.5, rely=.25, anchor="center")

        Button(self, text='Choose Video', fg="#000000", command=self.choose_video) \
            .place(relx=.57, rely=.25, anchor="center")


        # buttons
        Button(self, text='Add Param', fg="#000000", command=self.addition) \
            .place(relx=.45, rely=.35, anchor="center")
        Button(self, text='Remove Param',fg="#000000", command=self.remove) \
            .place(relx=.55, rely=.35, anchor="center")
        Button(self, text='Create File',fg="#000000", command=self.create_file) \
            .place(relx=.5, rely=.43, anchor="center")

        # Allows for easy exit from Create Screen
        self.exit_button = Button(self, text="Back", bg='#05F72D', fg="#000000",
                                  highlightbackground='#05F72D', font=("Courier", 24),
                                  height=1, width=5, command=self.exit)
        self.exit_button.place(relx=.9, rely=.1, anchor="center")

        # shows running params
        self.display = Label(self, text="", bg="#212121",
                             fg="#05F72D", font=("Courier", 20))
        self.display.place(relx=.5, rely=.6, anchor="center")

    def addition(self):
        """ lets users add parameters """
        global video
        # basic error checking
        if self.attr.get() == "" or self.sign.get() == "" or self.e1.get() == "" or video == "":
            messagebox.showinfo("Error", "Please fill out all fields.")
            return

        global Params
        Params = Params + "\n" + "If " + self.attr.get() \
            + " " + self.sign.get() + " " + self.e1.get() \
            + " play " + video_path
        self.params_added()
        # clears all the fields
        self.e1.delete(0, END)
        self.attr.set("          ")
        self.sign.set(" ")

    def create_file(self):
        """ creates the file once users are finished """
        global Params
        # lets user choose name/save location
        filename = filedialog.asksaveasfilename(initialdir="/home/Documents",
                                                title="Save file location",
                                                filetypes=(("djvj files", "*.djvj"),
                                                           ("all files", "*.*")))
        # adds to file
        pickle.dump(Params, open("%s.djvj" % filename, "wb"))
        Params = ""
        time.sleep(2)
        self.destroy()

    def params_added(self):
        """ shows running total of params to be added """
        global Params
        self.display.configure(text="%s" % Params)

    def remove(self):
        """ removes last parameter added """
        global Params
        # basic error checking
        if Params == "":
            messagebox.showinfo("Error", "Parameters are empty!")
        idx = Params.rfind("\n")
        if idx >= 0:
            Params = Params[:idx]
        self.params_added()

    def choose_video(self):
        """ allows user to choose a video to play for a given parameter """
        global video, video_path
        video_path = filedialog.askopenfilename(initialdir="/home/Documents", title="Select file",
                                                filetypes=(("mov files", "*.MOV"),
                                                           ("mp4 files", "*.mp4"),
                                                           ("all files", "*.*")))
        print(video_path)
        video_list = video_path.split("/")
        video = video_list[len(video_list)-1]
        Label(self, text=video, bg="#212121", fg="#05F72D", font=("Courier", 24)) \
            .place(relx=.7, rely=.25, anchor="center")

    def exit(self):
        """ Warns user about exiting without saving. """
        # if user selects "Yes", unsaved = true
        # else, just close out of the message dialog
        unsaved = messagebox.askyesno("Unsaved Show", "The current show is unsaved. Would you like to exit?\n"
                                                      "Select \"Yes\" to exit without saving.\n"
                                                      "Select \"No\" to return to the show screen and save.")
        if unsaved:
            self.destroy()


def init():
    """ allows this code to be run from main.py """
    IntroScreen().mainloop()
