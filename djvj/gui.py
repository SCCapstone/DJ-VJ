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
import os

# global variable params
PARAMS = ""
show = list()
audio_attr = list()  # what the audio should listen for
rules = list()  # <, >, =
values = list()  # what threshold the change happens at
video_loc = list()  # video path
working_file_path = ""


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
        self.create_button.place(relx=.2, rely=.75, anchor="center")

        self.edit_button = Button(self, text="Edit\nShow", bg='#05F72D', fg="#000000",
                                  highlightbackground='#05F72D', font=("Courier", 48),
                                  height=5, width=10, command=self.edit)
        self.edit_button.place(relx=.5, rely=.75, anchor="center")

        self.load_button = Button(self, text="Load\nShow", bg='#05F72D', fg="#000000",
                                  highlightbackground='#05F72D', font=("Courier", 48),
                                  height=5, width=10, command=self.load)
        self.load_button.place(relx=.8, rely=.75, anchor="center")

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





##########################################################################################################################
    def edit(self): 
        
        filename = filedialog.askopenfilename(initialdir="/home/Documents", title="Select Show",
                                              filetypes=(("djvj files", "*.djvj"),
                                                         ("all files", "*.*")))
        global working_file_path
        working_file_path = filename
        data = pickle.load(open("%s" % filename, "rb"))
        param_list = data.split("\n")
        param_list.pop(0)
        i = 0
        global PARAMS
        for parameter in param_list:
            attribute = parameter.split(" ")
            audio_attr.append(attribute[1])
            rules.append(attribute[2])
            values.append(attribute[3])
            video_loc.append(attribute[5])
            PARAMS = PARAMS + "\n" + "If " + audio_attr[i] \
            + " " + rules[i] + " " + values[i] \
            + " play " + video_loc[i]
            i+=1
            #write parameters to a text file
        '''
            with open(filename + '_params.txt', 'w') as f:
                j=0
                for parameter in param_list:
                    f.write("%s\n" % param_list[j])
                    j+=1
            print(i, ": ", param_list[i])
            i+=1

        #read parameters from text file 
        with open(filename + '_params.txt', 'r') as f:
            for line in f:
                print(line)
        print("-----------")
        print("param_list:")
        print(param_list)
        print("-----------")

        print("show:")
        print(show)
        print("-----------")

        print("audio_attr")
        print(audio_attr)
        print("-----------")


        print("rules:")
        print(rules)
        print("-----------")


        print("values:")
        print(values)
        print("-----------")

        print("video_loc:")
        print(video_loc)
        print("-----------")
        '''
        

        EditScreen(self)





        #EditScreen(self)
        
        #write list of parameters to a file, edit manually, read back into 
        #open the file, allow user to alter
        #read the file and update params



        '''
        param_choice = input("Enter the number of the parameter would you like to edit" + '\n')
        num_choice = int(param_choice)
        print(param_list[num_choice])
        attr_choice = input("What would you like to change?" + '\n' +
                            "0 : " + audio_attr[num_choice] + '\n' +
                            "1 : " + rules[num_choice] + '\n' +
                            "2 : " + values[num_choice] + '\n' +
                            "3 : " + video_loc[num_choice] + '\n')
        num_attr_choice = int(attr_choice)
        if(num_attr_choice == 0):
            new_audio_attr = input("enter 'pitch' or 'tempo': ")
            audio_attr[num_choice] = "tempo"
            print("New Parameter: " + param_list[0])
        '''
########################################################################################################################



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
        param_list = data.split("\n")
        param_list.pop(0)
        for parameter in param_list:
            attribute = parameter.split(" ")
            audio_attr.append(attribute[1])
            rules.append(attribute[2])
            values.append(attribute[3])
            video_loc.append(attribute[5])
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




class EditScreen(tk.Toplevel):
    """
    Users can create a .djvj file by adding parameters and setting target values
    They can also specify the file name/file save location when saving
    """
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title = "Edit Screen"
        # sets background of screen
        self.config(bg="#212121")
        # makes full-screen
        self.attributes('-fullscreen', True)

        Label(self, text="Add new parameters: ", bg="#212121",
              fg="#05F72D", font=("Courier", 28)).place(relx=.2, rely=.1, anchor="center")

        Label(self, text="If", bg="#212121", fg="#05F72D",
              font=("Courier", 36)).place(relx=.15, rely=.25, anchor="center")
        # the sound attribute being tracked
        self.attr = StringVar(self)
        self.attr.set("           ")  # default value
        self.set_attribute = OptionMenu(self, self.attr, "pitch", "tempo")
        self.set_attribute.place(relx=.22, rely=.25, anchor="center")
        # the sign (ie greater than, less than, etc)
        self.sign = StringVar(self)
        self.sign.set(" ")  # default value
        self.set_sign = OptionMenu(self, self.sign, ">", "<", "=")
        self.set_sign.place(relx=.3, rely=.25, anchor="center")
        # the target value
        self.target_value = Entry(self)
        self.target_value.place(relx=.4, rely=.25, anchor="center")

        Label(self, text=", ", bg="#212121", fg="#05F72D", font=("Courier", 36)) \
            .place(relx=.45, rely=.25, anchor="center")

        Label(self, text="play ", bg="#212121", fg="#05F72D", font=("Courier", 36)) \
            .place(relx=.5, rely=.25, anchor="center")

        Button(self, text='Choose Video', fg="#000000", command=self.choose_video) \
            .place(relx=.57, rely=.25, anchor="center")

        self.video_fullname = StringVar(self)
        self.video = StringVar(self)
        Label(self, textvariable=self.video, bg="#212121", fg="#05F72D", font=("Courier", 24)) \
            .place(relx=.8, rely=.25, anchor="center")

        # buttons
        Button(self, text='Add as New Param', fg="#000000", command=self.addition) \
            .place(relx=.45, rely=.35, anchor="center")
        Button(self, text='Remove Param', fg="#000000", command=self.remove) \
            .place(relx=.55, rely=.35, anchor="center")
        Button(self, text='Save Changes', fg="#000000", command=self.save_changes) \
            .place(relx=.45, rely=.43, anchor="center")
        Button(self, text='Print Params to Console', fg="#000000", command=self.print_params) \
            .place(relx=.55, rely=.43, anchor="center")
        
        Label(self, text="Select parameter to edit or delete:", bg="#212121",
              fg="#05F72D", font=("Courier", 28)).place(relx=.3, rely=.5, anchor="center")

        # Allows for easy exit from Create Screen
        self.exit_button = Button(self, text="Back", bg='#05F72D', fg="#000000",
                                  highlightbackground='#05F72D', font=("Courier", 24),
                                  height=1, width=5, command=self.exit)
        self.exit_button.place(relx=.9, rely=.1, anchor="center")

        # shows running params
        i = 0
        global PARAMS
        for x in audio_attr:
        #for i in range(5):
            a = audio_attr[i]
            b = rules[i]
            c = values[i]
            d = video_loc[i]
            b = Button(self, text="if %s %s %s play %s" % (a,b,c,d), command = lambda param_index = i: self.select_param(param_index))
            b.pack()
            b.place(relx = .15, rely = .55+(i/20))
            i += 1

    def select_param(self, p_index):
        '''
        TODO: open box to prompt user if they want to delete or edit param
        '''
        short_filename = os.path.basename(video_loc[p_index])
        self.attr.set(audio_attr[p_index])
        self.sign.set(rules[p_index])
        self.target_value.delete(0, END)
        self.target_value.insert(0, values[p_index])
        self.video.set(short_filename)
        self.video_fullname.set(video_loc[p_index])


    def addition(self):
        """ lets users add parameters """
        # basic error checking
        if self.attr.get() == "" or self.sign.get() == "" \
                or self.target_value.get() == "" or self.video.get() == "":
            messagebox.showinfo("Error", "Please fill out all fields.")
            return
        try:
            type(int(self.target_value.get()))
        except ValueError:
            messagebox.showinfo("Error", "Please enter an integer.")
            self.target_value.delete(0, END)
            return

        global PARAMS
        PARAMS = PARAMS + "\n" + "If " + self.attr.get() \
            + " " + self.sign.get() + " " + self.target_value.get() \
            + " play " + self.video_fullname.get()


        #messagebox.showinfo("Parameter Added", "If " + self.attr.get() \
        #    + " " + self.sign.get() + " " + self.target_value.get() \
        #    + " play " + self.video_fullname.get())

        ###########################self.params_added()
        # clears all the fields
        self.target_value.delete(0, END)
        self.attr.set("          ")
        self.sign.set(" ")
        self.video.set("")

    def save_changes(self):
        """ creates the file once users are finished """
        with open(working_file_path, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(PARAMS, output, pickle.HIGHEST_PROTOCOL)
        #global PARAMS
        # lets user choose name/save location
        #filename = filedialog.asksaveasfilename(initialdir="/home/Documents",
        #                                        title="Save file location",
        #                                        filetypes=(("djvj files", "*.djvj"),
        #                                                   ("all files", "*.*")))
        #if filename != "":
            # adds to file
        #    pickle.dump(PARAMS, open("%s.djvj" % filename, "wb"))
        #    time.sleep(2)
        #    self.destroy()

    ##########################3def params_added(self):
        ##########################""" shows running total of params to be added """
        #################################global PARAMS
        ###############################################self.display.configure(text="%s" % PARAMS)

    def print_params(self):
        global PARAMS
        print("CURRENT PARAMETERS: ")
        print("*************************************************************************")
        i = 0
        print("attributes:")
        for x in audio_attr:
            print(audio_attr[i] +" "+ rules[i] +" "+ values[i] + " " + video_loc[i])
            i+=1
        print("parameters:")
        print(PARAMS)
        print("*************************************************************************")

    def remove(self):
        """ removes selected parameter """
        global PARAMS
        print("Global params before deletion: ")
        print(PARAMS)

        print("All attr before deletion: ")
        i = 0
        for x in audio_attr:
            print(audio_attr[i] +" "+ rules[i] +" "+ values[i] + " " + video_loc[i])
            i+=1


        print("removing parameters...")
        a = self.attr.get()
        b = self.sign.get()
        c = self.target_value.get()
        d = self.video_fullname.get()
        e = self.video.get()

        j=0
        for x in audio_attr:
            if audio_attr[j] == a and rules[j] == b and values[j] == c and (video_loc[j] == d or video_loc[j] == e ):
                print("found parameter. deleting now...")
                audio_attr.pop(j)
                rules.pop(j)
                values.pop(j)
                video_loc.pop(j)
            j+=1

        print("All attr after deletion: ")
        k = 0
        for x in audio_attr:
            print(audio_attr[k] +" "+ rules[k] +" "+ values[k] + " " + video_loc[k])
            k+=1

    def choose_video(self):
        """ allows user to choose a video to play for a given parameter """
        global VIDEO_PATH
        VIDEO_PATH = filedialog.askopenfilename(initialdir="/home/Documents", title="Select file",
                                                filetypes=(("mov files", "*.MOV"),
                                                           ("mp4 files", "*.mp4"),
                                                           ("all files", "*.*")))
        print(VIDEO_PATH)
        video_list = VIDEO_PATH.split("/")
        # shortens full path to just the video name
        shortened_video = video_list[len(video_list)-1]
        self.video.set(shortened_video)

    def exit(self):
        """ Warns user about exiting without saving. """
        # if user selects "Yes", unsaved = true
        # else, just close out of the message dialog
        unsaved = messagebox.askyesno("Unsaved Show",
                                      "The current show is unsaved. Would you like to exit?\n"
                                      "Select \"Yes\" to exit without saving.\n "
                                      "Select \"No\" to return to the show screen to save.")
        if unsaved:
            self.destroy()



























class CreateScreen(tk.Toplevel):
    """
    Users can create a .djvj file by adding parameters and setting target values
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

        Label(self, text="Create a Show! Add Parameters: ", bg="#212121",
              fg="#05F72D", font=("Courier", 36)).place(relx=.5, rely=.1, anchor="center")

        Label(self, text="If", bg="#212121", fg="#05F72D",
              font=("Courier", 36)).place(relx=.15, rely=.25, anchor="center")
        # the sound attribute being tracked
        self.attr = StringVar(self)
        self.attr.set("           ")  # default value
        self.set_attribute = OptionMenu(self, self.attr, "pitch", "tempo")
        self.set_attribute.place(relx=.22, rely=.25, anchor="center")
        # the sign (ie greater than, less than, etc)
        self.sign = StringVar(self)
        self.sign.set(" ")  # default value
        self.set_sign = OptionMenu(self, self.sign, ">", "<", "=")
        self.set_sign.place(relx=.3, rely=.25, anchor="center")
        # the target value
        self.target_value = Entry(self)
        self.target_value.place(relx=.4, rely=.25, anchor="center")

        Label(self, text=", ", bg="#212121", fg="#05F72D", font=("Courier", 36)) \
            .place(relx=.45, rely=.25, anchor="center")

        Label(self, text="play ", bg="#212121", fg="#05F72D", font=("Courier", 36)) \
            .place(relx=.5, rely=.25, anchor="center")

        Button(self, text='Choose Video', fg="#000000", command=self.choose_video) \
            .place(relx=.57, rely=.25, anchor="center")

        self.video = StringVar(self)
        Label(self, textvariable=self.video, bg="#212121", fg="#05F72D", font=("Courier", 24)) \
            .place(relx=.8, rely=.25, anchor="center")

        # buttons
        Button(self, text='Add Param', fg="#000000", command=self.addition) \
            .place(relx=.45, rely=.35, anchor="center")
        Button(self, text='Remove Param', fg="#000000", command=self.remove) \
            .place(relx=.55, rely=.35, anchor="center")
        Button(self, text='Create File', fg="#000000", command=self.create_file) \
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
        # basic error checking
        if self.attr.get() == "" or self.sign.get() == "" \
                or self.target_value.get() == "" or self.video.get() == "":
            messagebox.showinfo("Error", "Please fill out all fields.")
            return

        try:
            type(int(self.target_value.get()))
        except ValueError:
            messagebox.showinfo("Error", "Please enter an integer.")
            self.target_value.delete(0, END)
            return

        global PARAMS
        PARAMS = PARAMS + "\n" + "If " + self.attr.get() \
            + " " + self.sign.get() + " " + self.target_value.get() \
            + " play " + VIDEO_PATH
        self.params_added()
        # clears all the fields
        self.target_value.delete(0, END)
        self.attr.set("          ")
        self.sign.set(" ")
        self.video.set("")

    def create_file(self):
        """ creates the file once users are finished """
        global PARAMS
        # lets user choose name/save location
        filename = filedialog.asksaveasfilename(initialdir="/home/Documents",
                                                title="Save file location",
                                                filetypes=(("djvj files", "*.djvj"),
                                                           ("all files", "*.*")))
        if filename != "":
            # adds to file
            pickle.dump(PARAMS, open("%s.djvj" % filename, "wb"))
            time.sleep(2)
            self.destroy()

    def params_added(self):
        """ shows running total of params to be added """
        global PARAMS
        self.display.configure(text="%s" % PARAMS)

    def remove(self):
        """ removes last parameter added """
        global PARAMS
        # basic error checking
        if PARAMS == "":
            messagebox.showinfo("Error", "Parameters are empty!")
        idx = PARAMS.rfind("\n")
        # take everything up until the second to last \n, which removes the last param
        if idx >= 0:
            PARAMS = PARAMS[:idx]
        self.params_added()

    def choose_video(self):
        """ allows user to choose a video to play for a given parameter """
        global VIDEO_PATH
        VIDEO_PATH = filedialog.askopenfilename(initialdir="/home/Documents", title="Select file",
                                                filetypes=(("mov files", "*.MOV"),
                                                           ("mp4 files", "*.mp4"),
                                                           ("all files", "*.*")))
        print(VIDEO_PATH)
        video_list = VIDEO_PATH.split("/")
        # shortens full path to just the video name
        shortened_video = video_list[len(video_list)-1]
        self.video.set(shortened_video)

    def exit(self):
        """ Warns user about exiting without saving. """
        # if user selects "Yes", unsaved = true
        # else, just close out of the message dialog
        unsaved = messagebox.askyesno("Unsaved Show",
                                      "The current show is unsaved. Would you like to exit?\n"
                                      "Select \"Yes\" to exit without saving.\n "
                                      "Select \"No\" to return to the show screen to save.")
        if unsaved:
            self.destroy()


def init():
    """ allows this code to be run from main.py """
    IntroScreen().mainloop()
