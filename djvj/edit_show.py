import tkinter as tk
from tkinter import filedialog, Button, Label, Entry, \
    OptionMenu, END, Frame, Listbox, Toplevel, StringVar, Scrollbar, messagebox
import os
import pickle
import time


class EditShow(tk.Toplevel):
    """class for editing moments and rules of a show"""

    __moments = list()
    __edit_target = list()
    __list_of_rules = list()

    def __init__(self, master, moments):
        tk.Toplevel.__init__(self, master)
        self.set_moments(moments)
        print("MOMENTS FROM EDIT SCREEN")
        frame = Frame(self)
        frame.pack()
        Label(frame, text="Edit Show").grid(row=0, column=0, rowspan=1, columnspan=2)
        self.charbox = Listbox(frame, width=100)
        for chars in []:
            self.charbox.insert(END, chars)
        self.charbox.grid(row=1, column=0, rowspan=5)
        Label(frame, text="Add New Rule").grid(row=6, column=0)
        new_rule_frame = Frame(frame, height=100, width=100, borderwidth=2)
        new_rule_frame.grid(column=0, row=7, columnspan=2)

        Label(new_rule_frame, text="Select Moment: ").grid(row=0, column=0, rowspan=1, columnspan=1)

        self.mom_val = StringVar(self)
        self.mom_val.set(".....")  # default value
        self.set_mom = OptionMenu(
           new_rule_frame, self.mom_val, *self.get_num_moments())\
            .grid(row=0, column=1, rowspan=1, columnspan=1)

        Label(new_rule_frame, text="              ").grid(row=0, column=2, rowspan=1, columnspan=1)

        Label(new_rule_frame, text="If   ").grid(row=0, column=3, rowspan=1, columnspan=1)

        self.attr_val = StringVar(self)
        self.attr_val.set(".....")  # default value
        self.set_attribute = OptionMenu(
            new_rule_frame, self.attr_val, "pitch", "tempo", "time")\
            .grid(row=0, column=4, rowspan=1, columnspan=1)

        self.sign_val = StringVar(self)
        self.sign_val.set(".....")  # default value
        self.set_sign = OptionMenu(
            new_rule_frame, self.sign_val, ">", "<", "=")\
            .grid(row=0, column=5, rowspan=1, columnspan=1)

        self.target_val = Entry(new_rule_frame, width=10)
        self.target_val.grid(row=0, column=6, rowspan=1, columnspan=1)

        Label(new_rule_frame, text="   play   ").grid(row=0, column=7, rowspan=1, columnspan=1)

        Button(new_rule_frame, text="Choose Video", command=self.choose_video).grid(row=0, column=8)

        self.vid_scroll = Scrollbar(new_rule_frame, orient="horizontal")
        self.vid_scroll.grid(row=1, column=9)

        self.vid_label = StringVar(self)
        self.vid_label.set("...")
        self.vid_entry = Entry(new_rule_frame, textvariable=self.vid_label, state='disabled',
                               xscrollcommand=self.vid_scroll.set)
        self.vid_entry.grid(row=0, column=9, rowspan=1, columnspan=1)
        self.vid_scroll.config(command=self.vid_entry.xview)
        Label(frame, text="Edit Rule").grid(row=8, column=0)
        edit_rule_frame = Frame(frame, height=100, width=100, borderwidth=2)
        edit_rule_frame.grid(column=0, row=9, columnspan=2)
        Label(edit_rule_frame, text="  Moment:   ").grid(row=0, column=0, rowspan=1, columnspan=1)

        self.edit_mom_val = StringVar(self)
        self.edit_mom_val.set(".....")  # default value
        self.set_mom_edit = Entry(
            edit_rule_frame, textvariable=self.edit_mom_val, state='disabled')\
            .grid(row=0, column=1, rowspan=1, columnspan=1)

        Label(edit_rule_frame, text="                   ")\
            .grid(row=0, column=2, rowspan=1, columnspan=1)

        Label(edit_rule_frame, text="If   ").grid(row=0, column=3, rowspan=1, columnspan=1)

        self.attr_val_edit = StringVar(self)
        self.attr_val_edit.set(".....")  # default value
        self.set_attribute_edit = OptionMenu(
            edit_rule_frame, self.attr_val_edit, "pitch", "tempo", "time")\
            .grid(row=0, column=4, rowspan=1, columnspan=1)

        self.sign_val_edit = StringVar(self)
        self.sign_val_edit.set(".....")  # default value
        self.set_sign_edit = OptionMenu(
            edit_rule_frame, self.sign_val_edit, ">", "<", "=")\
            .grid(row=0, column=5, rowspan=1, columnspan=1)

        self.target_val_edit = Entry(edit_rule_frame, width=10)
        self.target_val_edit.grid(row=0, column=6, rowspan=1, columnspan=1)

        Label(edit_rule_frame, text="   play   ").grid(row=0, column=7, rowspan=1, columnspan=1)

        Button(edit_rule_frame, text="Choose Video", command=self.choose_video)\
            .grid(row=0, column=8)

        self.vid_scroll_edit = Scrollbar(edit_rule_frame, orient="horizontal")
        self.vid_scroll_edit.grid(row=1, column=9)

        self.vid_label_edit = StringVar(self)
        self.vid_label_edit.set("...")
        self.vid_entry_edit = Entry(edit_rule_frame, textvariable=self.vid_label_edit,
                                    state='disabled', xscrollcommand=self.vid_scroll.set)
        self.vid_entry_edit.grid(row=0, column=9, rowspan=1, columnspan=1)
        self.vid_scroll_edit.config(command=self.vid_entry.xview)

        self.load_list_params()

        Button(new_rule_frame, text="   Add   ", command=self.add_param).grid(row=0, column=10)
        Button(edit_rule_frame, text="   Confirm Edit   ",
               command=self.confirm_edit).grid(row=0, column=10)
        Button(edit_rule_frame, text="   Clear   ", command=self.clear_add).grid(row=2, column=10)

        Button(frame, text="Remove", command=self.remove_param).grid(row=2, column=1)
        Button(frame, text="    Edit    ", command=self.edit_param).grid(row=3, column=1)
        Button(frame, text=" Save ", command=self.save_changes) \
            .grid(row=4, column=1)
        Button(frame, text="    Exit    ", command=self.exit_editor).grid(row=5, column=1)
        print(self.get_moments())

    def set_moments(self, moments):
        """ constructor to set __moments """

        self.__moments = moments

    def get_moments(self):
        """ constructor to get __moments """

        return self.__moments

    def set_edit_target(self, t):
        """ constructor to set target rule for edit function """

        self.__edit_target = t

    def get_edit_target(self):
        """ constructor to get target rule for edit function """

        return self.__edit_target

    def get_num_moments(self):
        """ returns moment count for editor """

        num_moments_list = list()
        for i in range(len(self.__moments)):
            num_moments_list.append(i)
        return num_moments_list

    def exit_editor(self):
        """ destroys the editor window """

        self.destroy()

    def choose_video(self):
        """ allows user to choose video parameter """
        video_path = filedialog.askopenfilename(initialdir="/home/Documents",
                                                title="Select video for current moment",
                                                filetypes=(("mov files", "*.MOV"),
                                                           ("mp4 files", "*.mp4"),
                                                           ("all files", "*.*")))
        self.vid_entry.config(state="normal")
        self.vid_label.set(video_path)
        self.vid_entry.config(textvariable=self.vid_label)
        self.vid_entry.config(state="disabled")

    def load_list_params(self):
        """ loads importated parameters into list box """

        m = self.get_moments()
        self.charbox.delete(0, END)
        # global final_rules
        for x in range(len(m)):
            self.charbox.insert(END, " Moment -- Video: " + str(m[x][0][3]))
            for y in range(len(m[x])):
                z = str(m[x][y])
                self.charbox.insert(END, z)

    def clear_add(self):
        """ clears out the add new rule entries"""

        self.vid_entry.config(state="normal")
        self.vid_label.set("...")
        self.vid_entry.config(textvariable=self.vid_label)
        self.vid_entry.config(state="disabled")

        self.mom_val.set(".....")
        self.attr_val.set(".....")
        self.sign_val.set(".....")
        self.target_val.delete(0, "end")

    def add_param(self):
        """ function to add new rule"""

        updated_moment_list = self.get_moments()
        print("Printing from Add Param")
        print(updated_moment_list)

        add_rule = True
        invalid_string = ""
        current_moment = self.mom_val.get()
        new_attr = self.attr_val.get()
        new_sign = self.sign_val.get()
        new_tval = self.target_val.get()
        new_vid = self.vid_entry.get()

        new_list = list()
        if current_moment == ".....":
            print("MOMENT FALSE")
            invalid_string += ("Invalid moment. " + '\n')
            add_rule = False
        else:
            print("MOMENT TRUE")

        if new_attr in ('pitch', 'tempo', 'time'):
            print("ATTR TRUE")
            new_list.append(new_attr)
        else:
            print("ATTR FALSE")
            invalid_string += ("Invalid attribute. " + '\n')
            add_rule = False

        if new_sign in ('>', '<', '='):
            print("SIGN TRUE")
            new_list.append(new_sign)
        else:
            print("SIGN FALSE")
            invalid_string += ("Invalid sign. " + '\n')
            add_rule = False

        if new_tval is not '' and int(new_tval) > 0:
            print("TVAL TRUE")
            new_list.append(new_tval)
        else:
            print("TVAL FALSE")
            invalid_string += ("Invalid target value. " + '\n')
            add_rule = False

        if new_vid != "..." and os.path.exists(new_vid):
            print("VID PATH TRUE")
            new_list.append(new_vid)
        else:
            print("VID PATH FALSE")
            invalid_string += ("Invalid video path. " + '\n')
            add_rule = False

        if add_rule == True:
            print("new rule added")
            new_list_copy = new_list.copy()
            new_list.clear()
            updated_moment_list[int(current_moment)].append(new_list_copy)
            self.set_moments(updated_moment_list)
            self.load_list_params()

        if add_rule == False:
            messagebox.showerror("ERROR", "Please fix the following" + '\n' + invalid_string)

    def remove_param(self):
        """ function to remove a rule """
        updated_moment_list = self.get_moments()
        delete = False
        x = self.charbox.curselection()
        y = self.charbox.get(x)
        target = y
        x_index = ''
        remove_value = ''

        for x in range(len(updated_moment_list)):
            for y in range(len(updated_moment_list[x])):
                if str(updated_moment_list[x][y]) == str(target):
                    delete = True
                    x_index = int(x)
                    remove_value = updated_moment_list[x][y]

        if delete:
            print("item deleted")
            updated_moment_list[x_index].remove(remove_value)
            self.set_moments(updated_moment_list)
            self.load_list_params()
            delete = False

        else:
            messagebox.showerror("ERROR", "Could not delete selected item")

    def edit_param(self):
        """ function to populate edit fields """

        updated_moment_list = self.get_moments()
        print("Printing from Add Param")
        print(updated_moment_list)
        found = False
        x = self.charbox.curselection()
        y = self.charbox.get(x)
        target = y
        self.set_edit_target(target)
        x_index = ''
        value = ''

        for x in range(len(updated_moment_list)):
            for y in range(len(updated_moment_list[x])):
                if str(updated_moment_list[x][y]) == str(target):
                    found = True
                    x_index = int(x)
                    value = updated_moment_list[x][y]
        if found:
            print("Split Selection: ")
            self.edit_mom_val.set(x_index)
            self.attr_val_edit.set(value[0])
            self.sign_val_edit.set(value[1])
            self.target_val_edit.insert(0, value[2])
            self.vid_entry_edit.config(state="normal")
            self.vid_label_edit.set(value[3])
            self.vid_entry_edit.config(state="disabled")
        else:
            messagebox.showerror("ERROR", "Could not delete selected item")

    def confirm_edit(self):
        """ adds edited rule to list and deletes previous rule """

        updated_moment_list = self.get_moments()
        print("Printing from Add Param")
        print(updated_moment_list)

        add_rule = True
        invalid_string = ""
        current_moment = self.edit_mom_val.get()
        new_attr = self.attr_val_edit.get()
        new_sign = self.sign_val_edit.get()
        new_tval = self.target_val_edit.get()
        new_vid = self.vid_entry_edit.get()

        new_list = list()
        if current_moment == ".....":
            print("MOMENT FALSE")
            invalid_string += ("Invalid moment. " + '\n')
            add_rule = False
        else:
            print("MOMENT TRUE")

        if new_attr in ('pitch', 'tempo', 'time'):
            print("ATTR TRUE")
            new_list.append(new_attr)
        else:
            print("ATTR FALSE")
            invalid_string += ("Invalid attribute. " + '\n')
            add_rule = False

        if new_sign in ('>', '<', '='):
            print("SIGN TRUE")
            new_list.append(new_sign)
        else:
            print("SIGN FALSE")
            invalid_string += ("Invalid sign. " + '\n')
            add_rule = False

        if new_tval is not '' and int(new_tval) > 0:
            print("TVAL TRUE")
            new_list.append(new_tval)
        else:
            print("TVAL FALSE")
            invalid_string += ("Invalid target value. " + '\n')
            add_rule = False

        if new_vid != "..." and os.path.exists(new_vid):
            print("VID PATH TRUE")
            new_list.append(new_vid)
        else:
            print("VID PATH FALSE")
            invalid_string += ("Invalid video path. " + '\n')
            add_rule = False

        if add_rule == True:
            print("new rule added")
            new_list_copy = new_list.copy()
            new_list.clear()
            updated_moment_list[int(current_moment)].append(new_list_copy)
            self.set_moments(updated_moment_list)

        if add_rule == False:
            messagebox.showerror("ERROR", "Please fix the following" + '\n' + invalid_string)

        delete = False

        target = self.get_edit_target()

        x_index = ''
        remove_value = ''

        for x in range(len(updated_moment_list)):
            for y in range(len(updated_moment_list[x])):
                if str(updated_moment_list[x][y]) == str(target):
                    delete = True
                    x_index = int(x)
                    remove_value = updated_moment_list[x][y]

        if delete:
            print("item deleted")
            updated_moment_list[x_index].remove(remove_value)
            self.set_moments(updated_moment_list)
            self.load_list_params()
            delete = False

        else:
            messagebox.showerror("ERROR", "Could not delete selected item")

        self.load_list_params()

        print("MOMENTS AFTER EDIT:")
        print(self.get_moments())

    def save_changes(self):
        """parses list entries to create usable string, saved as new file to be used by used by gui"""

        ss = ''
        retstr = ''
        for items in range(self.charbox.size()):
            if "Moment" in self.charbox.get(items):
                retstr += ("\n Moment -- Video: " + str(self.charbox.get(items)))
            else:
                ss = str(self.charbox.get(items, END))
                ss = ss.strip('[]')
                x = str(ss)
                x = x.replace("[", "")
                x = x.replace("]", "")
                x = x.strip(' ')
                x = x.replace("'", "")
                x = x.replace(" ", "")
                x = x.replace("(", "")
                charstr = ''
                charlist = ''
                for c in range(len(x)):
                    if (str(x[c]) != "[" and str(x[c]) != "\""):

                        charstr += str(x[c])
                charlist = str(charstr).split(",")
                isolated_rule = ''
                for l in range(len(charstr)):
                    isolated_rule = ("If\t" + str(charlist[0]) + "\t" +
                                     str(charlist[1]) + "\t" +
                                     str(charlist[2]) + "\tplay\t" + str(charlist[3]))
                retstr += "\n" + isolated_rule
        retstr += "\n Moment"
        print(retstr)

        filename = filedialog.asksaveasfilename(initialdir="/home/Documents",
                                                title="Save file location",
                                                filetypes=(("djvj files", "*.djvj"),
                                                           ("all files", "*.*")))
        if filename != "":
            # adds to file
            pickle.dump(retstr, open("%s.djvj" % filename, "wb"))
            time.sleep(2)

        self.destroy()
