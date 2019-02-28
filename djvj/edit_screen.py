"""class for editing parameters"""
from tkinter import filedialog, Button, Label, Entry, \
    OptionMenu, END, Frame, Listbox, Toplevel
import pickle
import time

PARAMS = ""

class EditShow():
    """Edit Show Class"""
    param_printout = ""
    parameter_prefix = "param_"
    attr_list = list()  # what the audio should listen for
    sign_list = list()  # <, >, =
    values_list = list()  # what threshold the change happens at
    vid_list = list()  # video path

    #variables used for final printout
    loaded_list = list()
    added_list = list()
    edited_list = list()
    deleted_list = list()

    def __init__(self, master, filename=''):
        self.master = master  # You'll want to keep a reference to your root window
        frame = Frame(master)
        frame.pack()
        # active_file = filename
        # character box
        Label(frame, text="Edit Show: %s"%filename).grid(row=0, column=0, rowspan=1, \
         columnspan=2)
        self.charbox = Listbox(frame, width=100)
        for chars in []:
            self.charbox.insert(END, chars)
        self.charbox.grid(row=1, column=0, rowspan=5)
        Button(frame, text="   Add   ", command=self.add_param).grid(row=1, column=1)
        Button(frame, text="Remove", command=self.remove_param).grid(row=2, column=1)
        Button(frame, text="    Edit    ", command=self.edit_param).grid(row=3, column=1)
        Button(frame, text=" Apply Changes ", command=self.apply_changes) \
                .grid(row=4, column=1)
        Button(frame, text="    Exit    ", command=frame.destroy).grid(row=5, column=1)

    def load_param(self, initial_attr='', initial_sign='', initial_value='', initial_vid=''):
        '''loads any existing parameters into edit screen'''
        output = "If %s %s %s play %s"%(initial_attr, initial_sign, initial_value, initial_vid)
        self.charbox.insert(END, output)
        self.attr_list.append(initial_attr)
        self.sign_list.append(initial_sign)
        self.values_list.append(initial_value)
        self.vid_list.append(initial_vid)
        self.loaded_list.append(output)



    def add_param(self, initial_attr='', initial_sign='', initial_value='', initial_vid=''):
        '''add parameter to show'''
        root = self.master
        t = Toplevel(root)  # Creates a new window
        t.title("Edit parameters")

        attribute_label = Label(t, text="Attribute:")
        attribute_entry = Entry(t)
        attribute_entry.insert(0, initial_attr)
        sign_label = Label(t, text="Sign:")
        sign_entry = Entry(t)
        sign_entry.insert(0, initial_sign)

        value_label = Label(t, text="Value:")
        value_entry = Entry(t)
        value_entry.insert(0, initial_value)
        vid_label = Label(t, text="Video:")
        vid_entry = Entry(t)
        vid_entry.insert(0, initial_vid)

        def create():
            '''adds new parameter to lists'''
            attr_name = attribute_entry.get()
            sign_name = sign_entry.get()
            value_name = value_entry.get()
            vid_name = vid_entry.get()
            output = "If %s %s %s play %s"%(attr_name, sign_name, value_name, vid_name)
            self.charbox.insert(END, output)
            self.attr_list.append(attr_name)
            self.sign_list.append(sign_name)
            self.values_list.append(value_name)
            self.vid_list.append(vid_name)
            self.added_list.append(output)
            t.destroy()

        create_button = Button(t, text="Create", command=create)
        cancel_button = Button(t, text="Cancel", command=t.destroy)

        attribute_label.grid(row=0, column=0)
        sign_label.grid(row=0, column=1)
        attribute_entry.grid(row=1, column=0)
        sign_entry.grid(row=1, column=1)

        value_label.grid(row=0, column=2)
        vid_label.grid(row=0, column=3)
        value_entry.grid(row=1, column=2)
        vid_entry.grid(row=1, column=3)

        create_button.grid(row=2, column=0)
        cancel_button.grid(row=2, column=1)
        return

    def get_attrs(self, index):
        ''' return attribute lists '''
        attr_name = self.attr_list[index]
        sign_name = self.sign_list[index]
        value_name = self.values_list[index]
        vid_name = self.vid_list[index]
        output = "%s %s %s %s"%(attr_name, sign_name, value_name, vid_name)
        return output

    def remove_param(self):
        ''' delete a parameter '''
        for index in self.charbox.curselection():
            item = self.charbox.get(int(index))
            output = ("Parameters deleted: %s"%item)
            self.deleted_list.append(output)
            self.charbox.delete(int(index))

    def edit_param(self):
        '''edit parameter content'''
        for index in self.charbox.curselection():
            item = self.charbox.get(int(index))
            item_list = item.split()
            self.charbox.delete(index)
        self.add_param(item_list[1], item_list[2], item_list[3], item_list[5]).create
        output = ("Parameters edited: %s"%item_list)
        self.edited_list.append(output)

    def apply_changes(self):
        '''save changes to file'''

        global PARAMS
        PARAMS = ""


        size = (self.charbox.size())
        for i in range(size):
            v_a = self.get_attr_name(i)
            v_b = self.get_sign(i)
            v_c = self.get_value(i)
            v_d = self.get_video(i)
            PARAMS = PARAMS + "\n" + "If " + v_a \
            + " " + v_b + " " + v_c \
            + " play " + v_d
        print(PARAMS)

        # lets user choose name/save location
        filename = filedialog.asksaveasfilename(initialdir="/home/Documents",
                                                title="Save file location",
                                                filetypes=(("djvj files", "*.djvj"),
                                                           ("all files", "*.*")))
        if filename != "":
            # adds to file
            pickle.dump(PARAMS, open("%s.djvj" % filename, "wb"))
            time.sleep(2)

        #return(self.loaded_list, self.added_list, self.edited_list, self.deleted_list)

    def get_attr_name(self, index):
        '''return name attribute'''
        attr_name = self.attr_list[index]
        out = attr_name
        return out

    def get_sign(self, index):
        '''return sign attribute'''
        attr_sign = self.sign_list[index]
        out = attr_sign
        return out

    def get_value(self, index):
        '''return value attribute'''
        attr_value = self.values_list[index]
        out = attr_value
        return out

    def get_video(self, index):
        '''return video attribute'''
        vid_name = self.vid_list[index]
        out = vid_name
        return out

    def print_report(self, loaded='', added='', edited='', deleted=''):
        '''
        prints out report of what is happening with edits, for programming purposes
        '''
        print("---------------------------------------------")
        print("-  Parameters loaded from existing file:    -")
        print("---------------------------------------------")
        print(*self.loaded_list, sep='\n')
        print()
        print()
        print("---------------------------------------------")
        print("-  Parameters added to existing file:       -")
        print("---------------------------------------------")
        print(*self.added_list, sep='\n')
        print()
        print()
        print("---------------------------------------------")
        print("-  Parameters edited from existing file:    -")
        print("---------------------------------------------")
        print(*self.edited_list, sep='\n')
        print()
        print()
        print("---------------------------------------------")
        print("-  Parameters deleted from existing file:   -")
        print("---------------------------------------------")
        print(*self.deleted_list, sep='\n')

def init(root):
    root = Tk()
    root.wm_title("DJVJ Edit Show")
    src = EditShow(root)
    root.mainloop()

#code used for faster testing
'''
root = Tk()
root.wm_title("DJVJ Edit Show")
src = EditShow(root)
src.load_param('pitch', '<', 100, 'movie_5')
root.mainloop()
'''
