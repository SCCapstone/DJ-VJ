"""
Runs the GUI for the DJ-VJ app.
Displays a splash screen, then Create and Load Show buttons
Create Show screen functionality is built out, more to come!
"""
import sys
import pickle
import tkinter as tk
from tkinter import filedialog, messagebox, Button, Label, Entry, Canvas, PhotoImage, \
    StringVar, OptionMenu, NW, END
import time
import os
import djvj.Bugger as bugger 

# global variables
RULES = ""  # running string of all rules added
moments = list()  # groups of rules for the show
current_mom = list()
moment_list = list()
moment_case = False

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
        # get relative path for splash screen file
        splash = resource_path("dj-vj.gif")
        # print(splash)
        img = PhotoImage(file=splash)

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
        # makes full-screen
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

        # Allows for easy exit from Intro Screen
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
        data = ""
        messagebox.showinfo(
            "Load a Show", "Please load a .djvj file to start the show!")
        filename = filedialog.askopenfilename(initialdir="/home/Documents", title="Select Show",
                                              filetypes=(("djvj files", "*.djvj"),
                                                         ("all files", "*.*")))
        try:
            data = pickle.load(open("%s" % filename, "rb"))
        except pickle.UnpicklingError:
            messagebox.showerror("ERROR", "Error: Corrupt .djvj file. Please select a valid file.")
        except FileNotFoundError:
            messagebox.showerror("ERROR", "No .djvj file selected")
        if data != "":
            rule_list = data.split("\n")
            error = False   # not a invalid path
            rule_list.pop(0)
            curr_mom = list()   # a list of the rules in the current moment
            for rule in rule_list:
                single_mom = list()  # create a list of rules for this moment
                print(rule)
                if "Moment" in rule:   # switch to a new moment
                    if curr_mom:
                        moments.append(curr_mom)
                        curr_mom = list()   # clear the list
                else:
                    attribute = rule.split("\t")

                    single_mom.append(attribute[1])
                    single_mom.append(attribute[2])
                    single_mom.append(attribute[3])
                    if os.path.exists(attribute[5]):
                        single_mom.append(attribute[5])
                    else:
                        messagebox.showerror("ERROR", "Error: File path %s does not exist.\n"
                                                      "Please choose a file with "
                                                      "valid file paths." % attribute[5])
                        error = True
                        break

                    curr_mom.append(single_mom)

            if error:
                self.load()
            else:
                # right now, just for error checking
                messagebox.showinfo("Load Show", "The rules for this video are:\n" + data)
                messagebox.showinfo("Video Controls", "To pause the video, press \"p\""
                                                      "\nTo resume the paused video, press \"r\""
                                                      "\nTo end the program, press \"k\"")
                self.destroy()

    def create(self):
        """ pulls up create screen """
        CreateScreen(self)

    def exit(self):
        """ exits screen """
        self.destroy()
        sys.exit()


class CreateScreen(tk.Toplevel):
    """
    Users can create a .djvj file by adding rules and setting target values
    They can also specify the file name/file save location when saving
    """
    VIDEO_PATH = ""

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title = "Create Screen"
        # sets background of screen
        self.config(bg="#212121")
        # makes full-screen
        self.attributes('-fullscreen', True)

        Label(self, text="Create a Show!", bg="#212121",
              fg="#05F72D", font=("Courier", 48)).place(relx=.5, rely=.06, anchor="center")
        Label(self, text="Add rules to your show by filling out the form below.\n"
                         "To add a rules, select \"Add Rule\""
                         "\n Moments are groups of rules "
                         "for the show to interpret together.\n"
                         "To add a new \"moment\" to your show, "
                         "select \"Add Moment\", and then add rules "
                         "to that moment. \n When finished, "
                         "click \"Create Show\".", bg="#212121", fg="#05F72D",
              font=("Courier", 18)).place(relx=.5, rely=.17, anchor="center")
        Label(self, text="If", bg="#212121", fg="#05F72D",
              font=("Courier", 36)).place(relx=.35, rely=.3, anchor="center")
        # the sound attribute being tracked
        self.attr = StringVar(self)
        self.attr.set("           ")  # default value
        self.set_attribute = OptionMenu(
            self, self.attr, "pitch", "tempo", "time")
        self.set_attribute.place(relx=.42, rely=.3, anchor="center")
        # the sign (ie greater than, less than, etc)
        self.sign = StringVar(self)
        self.sign.set(" ")  # default value
        self.set_sign = OptionMenu(self, self.sign, ">", "<", "=")
        self.set_sign.place(relx=.48, rely=.3, anchor="center")
        # the target value
        self.target_value = Entry(self)
        self.target_value.place(relx=.6, rely=.3, anchor="center")

        Label(self, text=":", bg="#212121", fg="#05F72D", font=("Courier", 36)) \
            .place(relx=.68, rely=.3, anchor="center")

        # buttons
        Button(self, text='Add Rule', fg="#000000", command=self.addition) \
            .place(relx=.42, rely=.4, anchor="center")
        Button(self, text='Remove Rule', fg="#000000", command=self.remove) \
            .place(relx=.52, rely=.4, anchor="center")
        Button(self, text='Add Moment', fg="#000000", command=self.moment_check) \
            .place(relx=.62, rely=.4, anchor="center")
        Button(self, text='Create File', fg="#000000", command=self.create_file) \
            .place(relx=.52, rely=.47, anchor="center")

        # Allows for easy exit from Create Screen
        self.exit_button = Button(self, text="Back", bg='#05F72D', fg="#000000",
                                  highlightbackground='#05F72D', font=("Courier", 24),
                                  height=1, width=5, command=self.exit)
        self.exit_button.place(relx=.9, rely=.1, anchor="center")

        self.w = Canvas(self, width=self.winfo_width(), height=1000)
        self.w.place(relx=.25, rely=.5)

        # shows running rules
        self.display = Label(self.w, text="", bg="#212121",
                             fg="#05F72D", font=("Courier", 16))
        self.display.pack()

        self.add_moment()

    def moment_check(self):
        global moment_list
        reason_for_moment_error = bugger.give_list_of_error()

        last_check = bugger.moment_to_list_comapare(moment_list)
        if last_check == True:
            moment_copy = bugger.add_moment_to_moment()
            moment_copy = moment_copy.copy()
            moment_list.append(moment_copy)
            bugger.clear_moment_list()
            self.add_moment()
        else:

            message = str(bugger.give_current_moment()) + " Collides with moment "+ str(reason_for_moment_error)
            messagebox.showerror("Error", message)

    def add_moment(self):
        """ Separates groups of rules """
        global RULES
        messagebox.showinfo(
            "Add a Moment", "Please choose a video to associate with this moment.")

        global VIDEO_PATH

        smideo_path = filedialog.askopenfilename(initialdir="/home/Documents",
                                                title="Select video for current moment",
                                                filetypes=(("mov files", "*.MOV"),
                                                           ("mp4 files", "*.mp4"),
                                                           ("all files", "*.*")))

        if smideo_path == "":
            if RULES == "":
                messagebox.showerror("Error", "No video selected for first moment.")
                self.destroy()
            else:
                messagebox.showerror("Error", "No video selected. Staying in current moment.")
        else:
            VIDEO_PATH = smideo_path
            RULES = RULES + "\n Moment -- Video: " + VIDEO_PATH
            self.rule_added()

    def addition(self):
        """ lets users add rules """
        # basic error checking
        if self.attr.get() == "" or self.sign.get() == "" \
                or self.target_value.get() == "":
            messagebox.showinfo("Error", "Please fill out all fields.")
            return

        try:
            type(int(self.target_value.get()))
        except ValueError:
            messagebox.showinfo("Error", "Please enter an integer.")
            self.target_value.delete(0, END)
            return

        new_rule = "If\t" + self.attr.get() \
            + "\t" + self.sign.get() + "\t" + self.target_value.get() \
            + "\t play\t"

        global RULES
        global moment_list
        global moment_case

        #appends attribute to list 
        current_mom.append(self.attr.get())
        #append sign to list 
        current_mom.append(self.sign.get())
        #append value to list 
        current_mom.append(self.target_value.get())
        #inititalize  
        bug = bugger.Bugger(current_mom, moment_list)
        #checks list for collisions
        list_case = bug.rule_check_in_list()
        #checks current moment for collision 
        temp_cm = current_mom.copy()
        moment_case = bug.rule_check_in_moment() 
        if moment_case == True and list_case == True:
            bugger.add_rule_to_moment(current_mom)
            current_mom.clear()
            moment_case = False
            RULES = RULES + "\n" + new_rule + VIDEO_PATH
            self.rule_added()
            self.target_value.delete(0, END)
            self.attr.set("          ")
            self.sign.set(" ")


        else:
            message = str(temp_cm) + " collides with rule: " + str(bugger.give_list_of_error()) 
            messagebox.showerror("Error", message)

    def create_file(self):
        """ creates the file once users are finished """
        global RULES
        RULES = RULES + "\nMoment"
        # lets user choose name/save location
        filename = filedialog.asksaveasfilename(initialdir="/home/Documents",
                                                title="Save file location")
        if filename != "":
            # adds to file
            pickle.dump(RULES, open("%s.djvj" % filename, "wb"))
            time.sleep(2)
            self.destroy()

    def rule_added(self):
        """ shows running total of rules to be added """
        global RULES
        self.display.configure(text="%s" % RULES)

    def remove(self):
        """ removes last rule added """
        global RULES
        # basic error checking
        if RULES == "":
            messagebox.showinfo("Error", "Rules are empty!")
        idx = RULES.rfind("\n")
        # take everything up until the second to last \n, which removes the last rule
        if idx >= 0:
            RULES = RULES[:idx]
        self.rule_added()

    def exit(self):
        """ Warns user about exiting without saving. """
        # if user selects "Yes", unsaved = true
        # else, just close out of the message dialog
        unsaved = messagebox.askyesno("Unsaved Show",
                                      "The current show is unsaved. Would you like to exit?\n"
                                      "Select \"Yes\" to exit without saving.\n "
                                      "Select \"No\" to return to the show screen to save.")
        if unsaved:
            global RULES
            RULES = ""
            self.destroy()


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    src: https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./djvj")

    return os.path.join(base_path, relative_path)


def init():
    """ allows this code to be run from main.py """
    IntroScreen().mainloop()
